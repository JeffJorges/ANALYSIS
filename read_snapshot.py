from struct import *
from collections import namedtuple
import numpy as np

def read_snapshot(fname):
  with open(fname, 'r') as fp:
    data = fp.read()
    header = namedtuple("header", "N Npart Mass Mass0 Mass1 Mass2 Mass3 Mass4 Mass5 a z FlagSfr FlagFeedback Nall0 Nall1 Nall2 Nall3 Nall4 Nall5 FlagCooling NumFiles BoxSize Omega_0 Omega_L h FlagMultphase FlagStellarAge FlagSfrHistogram")
    o = 4
    #s = "%lsf" % (header.nx)
    #x  = np.asarray(unpack(s,data[o:o+4*header.nx]))
    s = "%lsi" % (6)
    header.Npart = np.asarray(unpack(s,data[o:o+4*6]),dtype=int)

    #header.Npart0 = int(unpack("i", data[o:o+4])[0])
    o += 4*6
    #header.Npart1 = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Npart2 = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Npart3 = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Npart4 = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Npart5 = int(unpack("i", data[o:o+4])[0])
    #o += 4

    s = "%lsd" % (6)
    header.Mass = np.asarray(unpack(s,data[o:o+8*6]))
    o += 8*6

    #header.Mass0  = float(unpack("d", data[o:o+8])[0])
    #o += 8

    #header.Mass1  = float(unpack("d", data[o:o+8])[0])
    #o += 8

    #header.Mass2  = float(unpack("d", data[o:o+8])[0])
    #o += 8

    #header.Mass3  = float(unpack("d", data[o:o+8])[0])
    #o += 8

    #header.Mass4  = float(unpack("d", data[o:o+8])[0])
    #o += 8

    #header.Mass5  = float(unpack("d", data[o:o+8])[0])
    #o += 8

    header.a  = float(unpack("d", data[o:o+8])[0])
    o += 8
    a = header.a

    header.z  = float(unpack("d", data[o:o+8])[0])
    o += 8
    z = header.z

    header.FlagSfr  = int(unpack("i", data[o:o+4])[0])
    o += 4

    header.FlagFeedback  = int(unpack("i", data[o:o+4])[0])
    o += 4

    s = "%lsi" % (6)
    header.Nall = np.asarray(unpack(s,data[o:o+4*6]),dtype=int)
    o += 4*6

    #header.Nall0  = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Nall1  = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Nall2  = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Nall3  = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Nall4  = int(unpack("i", data[o:o+4])[0])
    #o += 4

    #header.Nall5  = int(unpack("i", data[o:o+4])[0])
    #o += 4    

    header.FlagCooling  = int(unpack("i", data[o:o+4])[0])
    o += 4

    header.NumFiles  = int(unpack("i", data[o:o+4])[0])
    o += 4

    header.BoxSize  = float(unpack("d", data[o:o+8])[0])
    o += 8
    #size = header.BoxSize

    header.Omega_0  = float(unpack("d", data[o:o+8])[0])
    o += 8

    header.Omega_L  = float(unpack("d", data[o:o+8])[0])
    o += 8

    header.h  = float(unpack("d", data[o:o+8])[0])
    o += 8

    header.FlagMultiphase  = int(unpack("i", data[o:o+4])[0])
    header.FlagStellarAge  = int(unpack("i", data[o:o+4])[0])
    header.FlagSfrHistogram  = int(unpack("i", data[o:o+4])[0])

    header.N = np.sum(header.Npart,dtype=int)

    #fill
    o += 84
    o += 4
    dummy = int(unpack("i", data[o:o+4])[0])
    #print("dummy = ",dummy)

    #positions
    #dummy
    o += 4
    s = "%lsf" % (3*header.N)
    #print(s)
    x = np.asarray(unpack(s,data[o:o+3*header.N*4]))
    #print("x info=",x[0],x.min(),x.max())
    x = np.resize(x,(header.N,3))
    o += 3*header.N*4
    #dummy
    o += 4

    #velocity
    #dummy
    o += 4
    s = "%lsf" % (3*header.N)
    #print(s)
    v = np.asarray(unpack(s,data[o:o+3*header.N*4]))
    o += 3*header.N*4
    #dummy
    o += 4

    #ids
    #dummy
    o += 4
    s = "%lsi" % (header.N)
    #print(s)
    #print(4*header.N)
    ids = np.asarray(unpack(s,data[o:o+4*header.N]),dtype=int)
    o += header.N*4
    #dummy
    o += 4

    #dummy
    #o += 4
    #coordinates
    #o  = 48
    #s = "%lsf" % (header.nx)
    #x  = np.asarray(unpack(s,data[o:o+4*header.nx]))

  #print_header(header)
  return header, x, v, ids#, z, a, size

def print_header(header):
  print("N     = ",header.N)
  print("Npart = ",header.Npart)
  print("Mass  = ",header.Mass)
  #print(header.Npart0)
  #print(header.Npart1)
  #print(header.Npart2)
  #print(header.Npart3)
  #print(header.Npart4)
  #print(header.Npart5)
  #print(header.Mass0)
  #print(header.Mass1)
  #print(header.Mass2)
  #print(header.Mass3)
  #print(header.Mass4)
  #print(header.Mass5)
  print("a = ",header.a)
  print("z = ",header.z)
  print("FlagSfr = ",header.FlagSfr)
  print("FlagFeedback = ",header.FlagFeedback)
  print("Nall = ",header.Nall)
  #print(header.Nall1)
  #print(header.Nall2)
  #print(header.Nall3)
  #print(header.Nall4)
  #print(header.Nall5)
  print("FlagCooling = ",header.FlagCooling)
  print("Numfiles = ",header.NumFiles)
  print("BoxSize = ",header.BoxSize)
  print("Omega_0 = ",header.Omega_0)
  print("Omega_L = ",header.Omega_L)
  print("h       = ",header.h)
  print("FlagMultiphase = ",header.FlagMultiphase)
  print("FlagStellarAge = ",header.FlagStellarAge)
  print("FlagSfrHistogram = ",header.FlagSfrHistogram)






