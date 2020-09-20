# Explain script here!
#
#
#
#
######################
# Modules 

import numpy as np
from matplotlib import pyplot as plt
import os
import sys
import subprocess
from termcolor import colored,cprint
import pandas as pd
######################


def histPlot(X, bins=10, xlow=1,xhigh=10, plotlabel='', savelabel='',
             xlabel='', ylabel='NOT PROVIDED', plotColor='#E55334'):
    '''
    Make Histogram plot
    Y:
    X:
    '''
    plt.rc('axes', linewidth=2)
    plt.rc('lines', markeredgewidth=2)
    plt.rc('font', **{'sans-serif': ['Helvetica']})
    fig = plt.figure(figsize=(10, 8))  # set figure dimensions
    ax1 = fig.add_subplot(1, 1, 1)  # allows us to build more complex plots
    for tick in ax1.xaxis.get_major_ticks():
        tick.label1.set_fontsize(20)  # scale for publication needs
        tick.label1.set_fontname('Helvetica')
    for tick in ax1.yaxis.get_major_ticks():
        tick.label1.set_fontsize(20)  # scale for publication needs
        tick.label1.set_fontname('Helvetica')
    plt.ylabel(ylabel, size=22)
    plt.xlabel(xlabel, size=22)
    plt.hist(X, bins=bins, range=(xlow,xhigh), label=plotlabel,
             color=plotColor)  # best to use HTML color codes: https://htmlcolorcodes.com
    plt.legend(numpoints=1, fontsize=18, loc='best')
    fig.tight_layout()
    plt.savefig(savelabel + '.png', format='png',
                bbox_inches='tight', dpi=300)
    plt.show()


cprint('-----> Beginning MSA Sort Plotting','green',attrs=['bold'])

# MSA_text=colored("MSA_Input (Must already be sorted and filtered...)",'cyan',
# 				  attrs=['bold'])
# MSA = input(MSA_text)

MSA_text=colored("MSA_Input (Must be in fasta format..): ",'cyan',
				  attrs=['bold'])
MSA = input(MSA_text)

# cmd = " cat ClustalOmegaOutput3_SortedSpecies.txt | awk '{print $1}' > test1.txt ; " \
#       "cat ClustalOmegaOutput3_SortedSpecies.txt | awk '{print $2,$3,$4,$5,$6}' > test2.txt ; " \
#       "paste test1.txt test2.txt > MSA_SpeciesFreq.txt ; " \
#       "rm -r test1.txt ; rm -r text2.txt "

# need to add this in
# cat ACTase_RegDomain_Ref_Ecoli_Blast_trimmed2_ClustalOmegaOutput3.fasta | awk -F'[][]' '{print $2}' | sort | uniq -c > ClustalOmegaOutput3_SortedSpecies.txt

cmd = " cat %s | awk '{print $1}' > test1.txt ; " \
      "cat %s | awk '{print $2,$3,$4,$5,$6}' > test2.txt ; " \
      "paste test1.txt test2.txt > MSA_SpeciesFreq.txt ; " \
      "rm -r test1.txt ; rm -r test2.txt " %(MSA,MSA)


# cmd = '%s'%MSA
# cprint(cmd, 'green',attrs=['bold'])

proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

data=np.loadtxt('MSA_SpeciesFreq.txt', skiprows=1, dtype=str, delimiter='\t')

# Should generate a histogram of num. of species vs # of occurences
# as well as a simplier (but probably uglier) plot of # of occurences vs species label (maybe make species label a number..)

n=len(data)

freq=[]
spec=[]
for k in data:
    freq.append(float(k[0]))
    spec.append(k[1])

# freq=[float(i) for i in freq]
# print(type(map(float,freq)))
# print(type(freq))
# print(freq[0:5])

# plt.hist(freq, bins=10, range=(1,10))
# plt.hist(freq, bins=10, range=(10,250))
# plt.show()

# plt.hist(freq, bins=10, range=(10,250),density=True, color='#E55334')
# plt.show()

# print(np.sum(freq))
# sum = np.sum(freq)
# freq_perc = (freq/sum)*100


# n=len(freq)
# plt.hist(freq,label=spec)
# plt.show()

#########################
# Occurence as a Function of Species.. Thinking about how to clean this up

# print(type(spec),len(spec),len(freq))
#
# plt.plot(spec, freq)
# plt.xticks(rotation=90)
# plt.show()

#################################
#################################
#################################

# Generate Plot with species label, therefore larger bin sizes (easier for general visualization..)

# histPlot(X=freq,bins=10,xlow=1,xhigh=10,plotlabel='Low Occurence Species',xlabel='No. of Repeat Entries',
#          ylabel='Sequences in MSA',savelabel='MSA_SpeciesFreq_LowOccurence')
#
# histPlot(X=freq,bins=25,xlow=10,xhigh=250,plotlabel='High Occurence Species',xlabel='No. of Repeat Entries',
#          ylabel='Sequences in MSA',plotColor='#D43762',savelabel='MSA_SpeciesFreq_HighOccurence')

# Generate plot with occurences as a function of individual species..
## this plot will be messy!

#################################
#################################
#################################
