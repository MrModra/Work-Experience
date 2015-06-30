#! /usr/bin/env python

#
# Analyse image to count and record number and size of bright spots.
#
# Tyler Modra - tylermodra@gmail.com
#
# Copyright Tyler Modra.
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies. The
# author makes no representations about the suitability of
# this software for any purpose. It is provided "as is"
# without express or implied warranty.

import sys
import getopt
import numpy as np
import pylab
import mahotas as mh


#print 'number of arguments:', len(sys.argv), "arguments"
#print 'argument list:', str(sys.argv)

vebose = 0

def scan(inputfile):
   image = mh.imread(inputfile)

   thresh =  100 #changes the threshold for blob detection

   labeled, nr_objects = mh.label(image > thresh)

   #print "%s has %d blobs" % (inputfile, nr_objects)
   
   size = mh.labeled.labeled_size(labeled)
   
   count = 1
   
   total = 0
   
   while count <= nr_objects:
      
      total = total + size[count] 
      
      if vebose == 1:
         print size[count]
      
      count = count + 1
      
   if vebose == 1:
      print "%s has a total of %d pixels" % (inputfile, total)
   
   return (nr_objects, total, thresh);
   



def main(argv):
 
   try:
      opts, args = getopt.getopt(argv,"i:ho:",["ifile=","ofile="])
   
   except getopt.GetoptError:
      print 'arguments.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
     
   if len(sys.argv) != 5:
      print "%s -i <inputfile> -o <outputfile>" % sys.argv[0]
      exit(2)
      
   for opt, arg in opts:
      
      if opt == '-h':
         print 'arguments.py -i <inputfile>'
         sys.exit()
      
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      
      elif opt in ("-o", "--ofile"):
         outputfile = arg
         
   
   print 'Input file is:', inputfile
   
   print 'Output file is:', outputfile
   
   output = open('output.csv', 'w+')
   
   numofblobs, sizeofblobs, thresh = scan(inputfile)
   
   output.write("%s, %d, %d" % (inputfile, numofblobs, sizeofblobs))
   
   print "%s has %d blobs covering %d pixels. Threshold = %d" % (inputfile, numofblobs, sizeofblobs, thresh)
   
   output.close()

if __name__ == "__main__":
   main(sys.argv[1:])



   
