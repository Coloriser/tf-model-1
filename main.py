import brisk
import chroma_ex as ce
import helper as hp
import numpy as np

extracted_features =  brisk.get_features('col.jpg')
input_x = hp.to_single_dimensional_array(extracted_features)

print "input_x :",np.array(input_x)
print "len of x",len(input_x)

chroma = ce.extract_A('col.jpg')
input_y = hp.to_single_dimensional_array(chroma)
print "input_y :",np.array(input_y)
print "len of input_y",len(input_y)