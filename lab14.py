# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 06:38:04 2020

@author: Daniyal Kabir
"""

import csv
from matplotlib import pylab

#opens our data files and skips the header/US overall rows
raw_data = csv.reader( open("STC_2014_STC005.csv") )
header = next(raw_data,None)
header = next(raw_data,None)
header = next(raw_data,None)

#initializes our data data storage

tax_info = {}

#assigns states/sales tax percentage to a dictionary

for row in raw_data:
    tax_info[ row[ 2 ] ] = 100 * ( int( row[ 5 ] ) / int( row[ 3 ] ) )



#translates our dictionary into lists we can use for graphing

states = [ key for key in tax_info ]
ratios = [ value[1] for value in tax_info.items() ]

#generates our indices based on the length of one of our lists

indices = [ i for i in range( len( ratios ) ) ]

#configures our export image size

pylab.figure(figsize=(20,15))

#determines labels/visual graph limits



pylab.title( "Ratio of Sales Tax to All State Taxes by State" )
pylab.ylabel('Ratio')
pylab.xlabel('State')
pylab.ylim([0,100])

#tells pylabs what the tick names/bar values will be

pylab.xticks( indices, states, rotation=90 )

pylab.bar( indices, ratios, .7, align="center" )




pylab.savefig('bar.png')