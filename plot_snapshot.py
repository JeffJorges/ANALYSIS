#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LogNorm
#np.set_printoptions(threshold=np.inf)
import sys

		
plt.ioff()
num = 0
if (len(sys.argv)>1):
	num = int(sys.argv[1])
num = "%03d" % num
name = 'snapshot_'+num
print
print(name)
fname = name+'_npData.npy'
print('Loading: \t'+fname),
Data = np.load(fname)
print('[Done]')

z = Data[1]
a = Data[2]
size = Data[3]
image = Data[0]
num_px = Data[4]

mini = 1
maxi = 4435

print('Ploting: \t'),
#fig = plt.figure(figsize=(fsize,fsize*wy/wx))
fig, (xy, xz, yz) = plt.subplots(1, 3)

#subplot(3, 1, 3)
cxy = xy.imshow(image[0], cmap=cm.viridis, aspect='equal',norm=LogNorm(vmin=mini, vmax=maxi))
xy.set_xlim(0,num_px)
xy.set_ylim(0,num_px)
xy.set_title('XY Projection')
#xy.axis('off')
print('XY-Done'),

#subplot(3, 2, 3)
cxz = xz.imshow(image[1], cmap=cm.inferno, aspect='equal',norm=LogNorm(vmin=mini, vmax=maxi))
xz.set_xlim(0,num_px)
xz.set_ylim(0,num_px)
xz.set_title('XZ Projection')
#xz.axis('off')
print('XZ-Done'),

#subplot(3, 3, 3)
cyz = yz.imshow(image[2], cmap=cm.gist_rainbow, aspect='equal',norm=LogNorm(vmin=mini, vmax=maxi))
yz.set_xlim(0,num_px)
yz.set_ylim(0,num_px)
yz.set_title('YZ Projection')
#yz.axis('off')
print('YZ-Done')

print('Configuring: \t'),
lt = .15
bm = .1
rt = 1-2*lt
tp = .05
fig.subplots_adjust(right=0.95, top=0.95, bottom=0.1, left=0)
cbar = fig.add_axes([lt,bm,rt,tp])
fig.colorbar(cyz, cax=cbar, ticks=[mini, maxi/2, maxi], orientation='horizontal')
plt.figtext(0.01, 0.01, "Z = {0:.2f},  Scale Factor= {1:.4f}".format(z, a))
cbar.set_xticklabels(['Density:  Low', '', 'High'])

s = "snapshot_"+num+".png"
print('[Done]')
print('Saving: \t'+s),
plt.savefig(s, dpi=750, facecolor='darkgray', bbox_inches="tight")
print('[Done]')
print
