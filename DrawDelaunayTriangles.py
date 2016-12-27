import cv2
import numpy as np
import random
import sys


# Draw Delaunay triangles

def draw_DelaunayTri(im,subdiv,delaunay_color):
        triangleList = subdiv.getTriangleList();
        size = im.shape
        r =(0,0,size[1],size[0])
        for t in triangleList:
                pt1 = (t[0],t[1])
                pt2 = (t[2],t[3])
                pt3 = (t[4],t[5])
                if rect_contains(r,pt1) and rect_contains(r,pt2) and rect_contains(r,pt3):
                        cv2.line(im,pt1,pt2,delaunay_color,1,8,0)
                        cv2.line(im,pt2,pt3,delaunay_color,1,8,0)
                        cv2.line(im,pt3,pt1,delaunay_color,1,8,0)

# Check if a point is inside a rectangle
def rect_contains(rect,point):
        if point[0] <rect[0]:
                return False
        elif point[1] < rect[1] :
           return False
        elif point[0] > rect[2] :
                return False
        elif point[1] > rect[3] :
                return False
        return True

#Draw a point
def draw_point(img,p,color):
        cv2.circle(img,p,2,color,1,8,0)

delaunay_color =(255,10,10)
points_color = (0,0,255)

im1 = cv2.imread('girlsface-cropx.jpg')

im1_orig = im1.copy()

size = im1.shape
rect1=(0,0,size[1],size[0])

rect2=(0,0,size[1],size[0])
subdiv1 = cv2.Subdiv2D(rect1)
subdiv2 = cv2.Subdiv2D(rect2)

points =[];

# read points from text file

with open('filea1xy.txt') as file:
        for line in file :
                x,y =line.split()
                points.append((int(x),int(y)))

#Insert points into subdiv

for p in points :
        subdiv1.insert(p)
        
# draw dalaunay triangles
draw_DelaunayTri(im1,subdiv1,delaunay_color);

for p in points:
        draw_point(im1,p,points_color);

cv2.imwrite('delaunay_1x.jpg',im1)

