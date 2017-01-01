from os import path
import sys
import numpy as np
import cv2

def get_features(file_name):

    # alternative detectors, descriptors, matchers, parameters ==> different results
    detector = cv2.BRISK(thresh=10, octaves=1)
    extractor = cv2.DescriptorExtractor_create('BRISK')  # non-patented. Thank you!
    matcher = cv2.BFMatcher(cv2.NORM_L2SQR)


    # Object Features
    obj_original = cv2.imread(path.join(file_name),cv2.CV_LOAD_IMAGE_COLOR)

    #error checking
    if obj_original is None:
        print 'Couldn\'t find the object image with the provided path.'
        sys.exit()


    # basic feature detection works in grayscale
    obj = cv2.cvtColor(obj_original, cv2.COLOR_BGR2GRAY)



    # keypoints are "interesting" points in an image:
    obj_keypoints = detector.detect(obj, None)


    # this lines up each keypoint with a mathematical description
    obj_keypoints, obj_descriptors = extractor.compute(obj, obj_keypoints)


    return obj_descriptors

#akheel code
# print 'Keypoints : ',obj_keypoints 
# print 'Number of Keypoints : ',len(obj_keypoints)
# print 'Number of Descriptors : ',len(obj_descriptors)
# print 'Descriptors : ',obj_descriptors
