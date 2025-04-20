from SpliceGrapher.SpliceGraph         import *
from SpliceGrapher.formats.GTFLoader   import *
from SpliceGrapher.formats.loader import loadGeneModels

from glob import glob
from optparse import OptionParser
import os, sys, warnings, numpy
import math
import numpy as np
import operator
import pickle
from numpy import mean, absolute
import copy, random

event_type = sys.argv[1]
dirPath = sys.argv[2]

#--------------------------------------------------------#
sample = {}
final_list = []
gfiles = glob(dirPath+'/*/*.gff')
for gfile in gfiles:
    graph = getFirstGraph(gfile)
    if graph.hasAS():
            AS_Events = graph.distinctAltEvents()
            for entry in AS_Events:
                    key = entry[2]
                    if key == event_type:
                        if '_' in graph.chromosome:
                            continue
                        if graph.strand == '+':
                            final_list.append([key,entry[0],entry[1],graph.name,graph.strand,graph.chromosome])
                        else:
                            final_list.append([key,entry[1],entry[0],graph.name,graph.strand,graph.chromosome])
                    if key in sample:
                        sample[key] += 1
                    else:
                        sample[key] = 1

with open ('AS_Landscape_Dict_'+event_type+'.pickle','wb') as f:
        pickle.dump(sample,f)

np.savetxt(event_type+'_events.txt',final_list,delimiter='\t',fmt='%s')

#-----------------------------Now Extracting Information------------------------------#
#--------Top Level (All samples and replicates)------#
lst_big = [['Sample','A3','A5','AI','AT','IR','SE']]
for key in sample.keys():
    print key, sample[key]
