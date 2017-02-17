#!/usr/bin/python

# Sine Z^2 Julia Set.
# JM Thu  2 Feb 2017 16:43:53 GMT

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list 
import sys

start = timer()

X_MIN = -2.0
X_MAX =  2.0
Y_MIN = -1.0 
Y_MAX =  1.0 
offset     = 0.01
maxiter    = 95
calc_count = 0
rnum       = 93
lenlc      = len( colour_list ) 
C = complex ( -1.61, -0.1 )
#C          = complex ( -0.7691574125898175, 0.1167394219557992 ) 
# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
print 'Offset: {0:.8f}'.format( offset )
print 'Offset: ', offset 

if ( len( sys.argv ) == 2 ):
	sys.exit()

white      = (255,255,255)
randcolour =  ( 255,248,230)
blue       = (0,0,255) 
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = cmath.sin( Z**2 ) + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
                if ( iter_count + rnum  >= lenlc ):
                        mycolour = colour_list[ iter_count % lenlc ]
                else:   
                        mycolour = colour_list[ iter_count + rnum  ]

		if ( iter_count <= 2 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 

		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Julia Fractal for sin( Z^2 ) ' + str( C ) + ' and rnum: ' + str( rnum )

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print 'Julia Fractal for sin( Z^2 ) ', C, 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count

fname = 'Julia_Sin_Zsq:' + str( C ) + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'
print 'Fname:', fname

img.show()
#img.save( fname )

