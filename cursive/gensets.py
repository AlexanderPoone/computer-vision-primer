from glob import glob
from random import randrange
from os import mkdir
from shutil import rmtree, copyfile
from tensorflow.image import resize_images
# Find characters that has more than one image
# Pick random character and remove it from the array

rmtree('gen_train',True)
rmtree('gen_test',True)
mkdir('gen_train')
mkdir('gen_test')

a = []
b = []
for x in glob('*.png'):
	if x[1] == '0':
		b.append(a)
		a = []
	a.append(x)
b.pop(0)
a = []
for x in reversed(range(len(b))):
	if len(b[x]) > 1:
		a.append(b.pop(x))
print(a)
print(b)

for x in range(len(a)):
	y = a[x].pop(randrange(len(a[x])))
	copyfile(y, 'gen_test/'+y)
	for y in a[x]:
		copyfile(y, 'gen_train/'+y)
print(a)

# from skimage import data
# from skimage import transform as tf
# from skimage.feature import (match_descriptors, corner_peaks, corner_harris,
#                              plot_matches, BRIEF)
# from skimage.color import rgb2gray
# import matplotlib.pyplot as plt



# img1 = rgb2gray(data.astronaut())
# tform = tf.AffineTransform(scale=(1.2, 1.2), translation=(0, -100))
# img2 = tf.warp(img1, tform)
# img3 = tf.rotate(img1, 25)

# keypoints1 = corner_peaks(corner_harris(img1), min_distance=5)
# keypoints2 = corner_peaks(corner_harris(img2), min_distance=5)
# keypoints3 = corner_peaks(corner_harris(img3), min_distance=5)

# extractor = BRIEF()

# extractor.extract(img1, keypoints1)
# keypoints1 = keypoints1[extractor.mask]
# descriptors1 = extractor.descriptors

# extractor.extract(img2, keypoints2)
# keypoints2 = keypoints2[extractor.mask]
# descriptors2 = extractor.descriptors

# extractor.extract(img3, keypoints3)
# keypoints3 = keypoints3[extractor.mask]
# descriptors3 = extractor.descriptors

# matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)
# matches13 = match_descriptors(descriptors1, descriptors3, cross_check=True)

# fig, ax = plt.subplots(nrows=2, ncols=1)

# plt.gray()

# plot_matches(ax[0], img1, img2, keypoints1, keypoints2, matches12)
# ax[0].axis('off')
# ax[0].set_title("Original Image vs. Transformed Image")

# plot_matches(ax[1], img1, img3, keypoints1, keypoints3, matches13)
# ax[1].axis('off')
# ax[1].set_title("Original Image vs. Transformed Image")


# plt.show()