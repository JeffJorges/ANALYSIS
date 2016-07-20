#!/usr/bin/env python
import sys

def scale(z):
    a = 1./(1+z)
    print "{0:.8}".format(a)

#Saves user input
z_start = int(sys.argv[1])
z_hires = int(sys.argv[2])
num_snaps_total = int(sys.argv[3])
num_snaps = (num_snaps_total-1)/2.

i = 1
steps = (z_start-z_hires)/num_snaps
z = float(z_start)
scale(z)
while(z-steps >= z_hires):
    z += -steps
    i += 1
    scale(z)

steps = z_hires/num_snaps
z = float(z_hires)
while(z-steps >= 0):
    z += -steps
    i += 1
    scale(z)

scale(0)
