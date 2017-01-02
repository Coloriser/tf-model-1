import pickle
import brisk
import helper as hp

#get list of images
# image_list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
image_list = ['small_col.jpg']

for image in image_list:
	extracted_features =  brisk.get_features(image)
	array = hp.to_single_dimensional_array(extracted_features)

	name = image.split(".")[0] + ".pickle"

	with open(name, "wb") as f:
		pickle.dump(array, f)

	print name," written."

# Reading from a pickle
# with open('filename.pickle', 'rb') as handle:
#     b = pickle.load(handle)