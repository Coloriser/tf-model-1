import brisk
# import argparse
from glob import glob
# import os
from os.path import exists, join, basename, splitext
import numpy


EXTENSIONS = [".jpg", ".bmp"]
DATASETPATH = 'dataset'
""" BRISK PARAMS """
MAXSIZE = 1024
VERBOSE = True
WRITE_VERBOSE = False  # no verbose reading atm





# def parse_arguments():						#argument parser -d for the pathlist
#     parser = argparse.ArgumentParser(description='Pre-works before the training')
#     parser.add_argument('-d', help='path to the dataset', required=False, default=DATASETPATH)
#     args = parser.parse_args()
#     return args

def get_imgfiles(path):						#gets image from the path
    all_files = []
    all_files.extend([join(path, basename(fname))
                    for fname in glob(path + "/*")
                    if splitext(fname)[-1].lower() in EXTENSIONS])
    print all_files
    return all_files

def process_images(input_files):
    print "BEGIN EXTRACTION"
    brisk_features_arr = []
    for i, fname in enumerate(input_files):
        brisk_fname = fname + '.brisk'
        if exists(brisk_fname) == False:
            print "step i: calculating brisk for", fname
            process_brisk(fname, brisk_fname)
        print "gathering brisk for", fname
        """ HAVE TO TEST THIS PART """
        descriptors = numpy.load(brisk_fname)
        brisk_features_arr.append(descriptors)
    return brisk_features_arr

def begin(datasetpath = DATASETPATH):
	print "---------------------"
	print "## loading the images and extracting the BRISK features"
	# args = parse_arguments()
	# datasetpath = args.d
	print "Searching for images at " + datasetpath
	all_files = []
	img_files = get_imgfiles(datasetpath)
	if img_files :
		all_files = all_files + img_files
		return process_images( img_files )
	else:
		print "No files found"
		return