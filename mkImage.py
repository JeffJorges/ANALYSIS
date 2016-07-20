#!/usr/bin/env python
import numpy as np
#np.set_printoptions(threshold=np.inf)
from read_snapshot import *
import sys

#Constants
num_px=512

def mkImage(positions, size, num_px=num_px):
	'''
	Name:   mkImage
	Input:  Positions(3D array), Size(Int), Number of pixels(Int)
	Output: Images(Array made of 3 2D array projections)
	Description: Reads in array of 3D position data and convets it into a 3D image
	             of how many particles are in a given pixel.
	'''
	#Initial Definitions
	#image_3d = np.zeros((num_px+1, num_px+1, num_px+1))
	image_xy = np.ones((num_px, num_px))
	image_xz = np.ones((num_px, num_px))
	image_yz = np.ones((num_px, num_px))
	num_particles = len(positions)
	px_per_size = float(num_px/size)
	#positions_px = np.around(positions*px_per_size, decimals=1)
	
	#Loop to count the particles in every pixel
	perc = int(num_particles/100)
	c = 0
	#print(perc)
        for i in xrange(num_particles):
		if((i%perc)==0):
			print('{}'.format(str(c)+'\tPercent Done', fill=' ', align ='^'))
			c += 1
		ix = positions[i,0] * px_per_size
		iy = positions[i,1] * px_per_size
		iz = positions[i,2] * px_per_size
		image_xy[ix, iy] += 1
                image_xz[ix, iz] += 1
		image_yz[iy, iz] += 1
	#print('=]')

	#Returns converted Arrays
	image_3d = np.array([image_xy, image_xz, image_yz])
	return image_3d


		
num = 0
if (len(sys.argv)>1):
	num = int(sys.argv[1])
num = "%03d" % num

print
fname = 'snapshot_'+num
print(fname)
print('Loading: \t'+fname),
header, x, v, ids = read_snapshot(fname)
z = header.z
a = header.a
size = header.BoxSize
print('[Done]')

print('===Converting Positions to Pixels===')
image = mkImage(x, size)
print('[Done]\n')

output = fname+'_npData'
print('Saving Image as: '+output),
data = np.array([image, z, a, size, num_px])
np.save(output, data)
print('[Done]')
print
