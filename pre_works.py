import brisk
import argparse
from glob import glob
# import os
from os.path import exists, join, basename, splitext
import numpy


EXTENSIONS = [".jpg", ".bmp", ".png", ".pgm", ".tif", ".tiff"]
DATASETPATH = 'dataset'
""" BRISK PARAMS """
MAXSIZE = 1024
VERBOSE = True
WRITE_VERBOSE = False  # no verbose reading atm





def parse_arguments():						#argument parser -d for the pathlist
    parser = argparse.ArgumentParser(description='Pre-works before the training')
    parser.add_argument('-d', help='path to the dataset', required=False, default=DATASETPATH)
    args = parser.parse_args()
    return args

def get_imgfiles(path):						#gets image from the path
    all_files = []
    all_files.extend([join(path, basename(fname))
                    for fname in glob(path + "/*")
                    if splitext(fname)[-1].lower() in EXTENSIONS])
    print all_files
    return all_files

def process_image(imagename, resultname="temp.brisk"):
	""" process an image and save the results in a .key ascii file"""
	print("working on " + imagename)
	# run extraction command
	extracted_features, keypoints = brisk.get_features( imagename, resultname)
	print( str(len(keypoints)) + " keypoints found.")
	return extracted_features
      



def extractBrisk(input_files):
    print "BEGIN EXTRACTION"
    all_features_dict = {}
    for i, fname in enumerate(input_files):
        features_fname = fname + '.brisk'
        if exists(features_fname) == False:
            print "calculating brisk for", fname
            extracted_features = process_image(fname, features_fname)
            print extracted_features.shape
        print "gathering brisk for", fname
        """ HAVE TO TEST THIS PART """
        descriptors = numpy.load(features_fname)
        print descriptors.shape
        all_features_dict[fname] = descriptors
    return all_features_dict



print "---------------------"
print "## loading the images and extracting the BRISK features"
args = parse_arguments()
datasetpath = args.d
print "Searching for images at " + datasetpath
all_files = []
all_features = {}
img_files = get_imgfiles(datasetpath)
if img_files :
	cat_features = extractBrisk(img_files)
	all_files = all_files + img_files
	all_features.update(cat_features)
else:
	print "No files found"
	




