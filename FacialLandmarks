import cv2
import dlib
import numpy
import matplotlib
from matplotlib import pyplot as plt


PREDICTOR_PATH="c:/users/heidi/Anaconda2/Lib/site-packages/nbpresent/tests/notebooks/data/shape_predictor_68_face_landmarks.dat"

SCALE_FACTOR=1
FEATHER_AMOUNT=11  

FACE_POINTS=list(range(17,68))
MOUTH_POINTS = list(range(48,61))
RIGHT_BROW_POINTS = list(range(17,22))
LEFT_BROW_POINTS = list(range(22,27))
RIGHT_EYE_POINTS = list(range(36,42))
LEFT_EYE_POINTS = list(range(42,48))
NOSE_POINTS = list(range(27,35))
JAW_POINTS = list(range(0,17))

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

def read_landmarks(im):
        rects = detector(im,1)
        return numpy.matrix([[p.x,p.y] for p in predictor(im, rects[0]).parts()])

def annotate_landmarks(im, landmarks):
        im = im.copy()
        for idx, point in enumerate(landmarks):
                pos = (point[0,0], point[0,1])
                cv2.circle(im,pos,2,color=(235,0,0))
        return im

def read_im_and_landmarks(fname):
        im = cv2.imread(fname,cv2.IMREAD_COLOR)
        im = cv2.resize(im, (im.shape[1] * SCALE_FACTOR,im.shape[0] * SCALE_FACTOR))
        s = read_landmarks(im)
        return im, s
        
im1,landmarks1 = read_im_and_landmarks('tswifty-cropx.jpg')
#im2,landmarks2 = read_im_and_landmarks('moustache_cropx.jpg')

annotate_1 = annotate_landmarks(im1,landmarks1)
#annotate_2 = annotate_landmarks(im2,landmarks2)

cv2.imwrite('annotate_tswifty.jpg',annotate_1)
#cv2.imwrite('annotate_im2ax.jpg',annotate_2)
