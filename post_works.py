import numpy as np
import skimage.color as color
import skimage.io as io


def reconstruct(l_arr,a_arr):

	b_arr = np.zeros( shape = l_arr.shape)

	img = np.vstack(([l_arr.T], [a_arr.T], [b_arr.T])).T
	rgb_image = color.lab2rgb(img)

	io.imsave("recon.jpg", rgb_image)


# For Testing ...

file_name = './dataset/small_col.jpg'

img_rgb = io.imread(file_name)	
img_lab = color.rgb2lab(img_rgb)

l_arr = img_lab[:,:,0]
a_arr = img_lab[:,:,1]

reconstruct(l_arr, a_arr)