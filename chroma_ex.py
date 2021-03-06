import numpy as np
import skimage.color as color
import skimage.io as io

def extract_A(file_name, resultname='temp.chroma'):
	img_rgb = io.imread(file_name)

	img_lab = color.rgb2lab(img_rgb) # convert image to lab color space
	img_l = img_lab[:,:,1] # pull out A channel

	img_l.dump(resultname)

	# img_lab[:,:,0]=0
	# img_lab[:,:,2]=0
	# io.imsave("Achannel.tiff", img_lab)
	
	return

def extract_B(file_name, resultname='temp.chroma'):
	img_rgb = io.imread(file_name)

	img_lab = color.rgb2lab(img_rgb) # convert image to lab color space
	img_l = img_lab[:,:,2] # pull out B channel

	# img_lab[:,:,0]=0
	# img_lab[:,:,1]=0
	# io.imsave("Bchannel.tiff", img_lab)
	
	return img_l	

def extract_AB(file_name, resultname='temp.chroma'):
	img_rgb = io.imread(file_name)

	img_lab = color.rgb2lab(img_rgb) # convert image to lab color space
	img_l = img_lab[:,:,1] # pull out AB channel

	# img_lab[:,:,0]=0
	# io.imsave("ABchannel.tiff", img_lab)
	
	return img_l	