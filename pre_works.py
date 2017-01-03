import brisk
import argparse
from glob import glob
# import os
from os.path import exists, join, basename, splitext
import numpy
from chroma_ex import extract_A


EXTENSIONS = [".jpg", ".bmp"]
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

def process_brisk(imagename, resultname="temp.brisk"):
	""" process an image and save the results in a .key ascii file"""
	print("(brisk)working on " + imagename)
	# run extraction command
	keypoints = brisk.get_features( imagename, resultname)
	print( str(len(keypoints)) + " keypoints found.")
	return

def process_chroma(imagename, resultname="temp.chroma"):
	""" process an image and save the results in a .key ascii file"""
	print("(chroma)working on " + imagename)
	# run extraction command
	chroma_features= extract_A( imagename, resultname)
	print chroma_features
	return

def process_images(input_files):
    print "BEGIN EXTRACTION"
    all_features_dict = {}
    for i, fname in enumerate(input_files):
        brisk_fname = fname + '.brisk'
        chroma_fname = fname + '.chroma'
        if exists(brisk_fname) == False:
            print "step i: calculating brisk for", fname
            process_brisk(fname, brisk_fname)
        if exists(chroma_fname) == False:
            print "step ii: calculating chroma for", fname
            process_chroma(fname, chroma_fname)
        print "gathering brisk for", fname
        """ HAVE TO TEST THIS PART """
        descriptors = numpy.load(brisk_fname)
        print "gathering chroma for", fname
        chroma = numpy.load(chroma_fname)
        print chroma.shape
        all_features_dict[fname] = descriptors
    return all_features_dict, chroma

print "---------------------"
print "## loading the images and extracting the BRISK features"
args = parse_arguments()
datasetpath = args.d
print "Searching for images at " + datasetpath
all_files = []
all_features = {}
img_files = get_imgfiles(datasetpath)
if img_files :
	brisk_features, chroma_features = process_images( img_files )
	all_files = all_files + img_files
	all_features.update(brisk_features)
else:
	print "No files found"
	




