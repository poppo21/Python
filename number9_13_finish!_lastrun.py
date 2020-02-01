#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on 2019_01_29_1548
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'exp01'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\15T5085\\Desktop\\Python_data\\number_touch\\number9_13_finish!.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1600, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='My Monitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "ready"
readyClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='C:\\Users\\15T5085\\Desktop\\Python_data\\number_touch\\test.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "routine_9_13"
routine_9_13Clock = core.Clock()
b_mouse_2_ = event.Mouse(win=win)
x, y = [None, None]
import random

#サイズ,色の指定
size = 75
color = 'white'
num_amount = 117 #default 135

#数字の設定
number_color = 'blue'
number = range(1,num_amount+1)
number_size = 45
#配置場所の指定
A = 0
B = size + 5
C = - B
D = 2*B
E = -D
F = 3*B
G = -F
H = 4*B
I = -H
J = 5*B
K = -J
L = 6*B
M = -L

x = [A,A,A,A,A,A,A,A,A,B,B,B,B,B,B,B,B,B,C,C,C,C,C,C,C,C,C,D,D,D,D,D,D,D,D,D,E,E,E,E,E,E,E,E,E,F,F,F,F,F,F,F,F,F,G,G,G,G,G,G,G,G,G,H,H,H,H,H,H,H,H,H,I,I,I,I,I,I,I,I,I,J,J,J,J,J,J,J,J,J,K,K,K,K,K,K,K,K,K,L,L,L,L,L,L,L,L,L,M,M,M,M,M,M,M,M,M]
y = [A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I,A,B,C,D,E,F,G,H,I]

position = range(num_amount)
random.shuffle(position)

#透過の初期値
Tr = [1 for i in range(num_amount)]

#各ますの配置場所の読み込み
target = 0
targetPx = [1 for i in range(num_amount)]
targetPy = [1 for i in range(num_amount)]
for i in range(num_amount):
    targetPx[i] = [x[position[i]]]
    targetPy[i] = [y[position[i]]]

click_miss = 0

#範囲指定
a = [size]
b_polygon_26_ = visual.Rect(
    win=win, name='b_polygon_26_',
    width=[size,size][0], height=[size,size][1],
    ori=0, pos=[x[position[0]], y[position[0]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
b_polygon_27_ = visual.Rect(
    win=win, name='b_polygon_27_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[1]], y[position[1]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
b_polygon_28_ = visual.Rect(
    win=win, name='b_polygon_28_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[2]], y[position[2]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
b_polygon_29_ = visual.Rect(
    win=win, name='b_polygon_29_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[3]], y[position[3]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
b_polygon_30_ = visual.Rect(
    win=win, name='b_polygon_30_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[4]], y[position[4]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
b_polygon_31_ = visual.Rect(
    win=win, name='b_polygon_31_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[5]], y[position[5]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)
b_polygon_32_ = visual.Rect(
    win=win, name='b_polygon_32_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[6]], y[position[6]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)
b_polygon_33_ = visual.Rect(
    win=win, name='b_polygon_33_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[7]], y[position[7]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-9.0, interpolate=True)
b_polygon_34_ = visual.Rect(
    win=win, name='b_polygon_34_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[8]], y[position[8]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-10.0, interpolate=True)
b_polygon_35_ = visual.Rect(
    win=win, name='b_polygon_35_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[9]], y[position[9]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-11.0, interpolate=True)
b_polygon_36_ = visual.Rect(
    win=win, name='b_polygon_36_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[10]], y[position[10]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-12.0, interpolate=True)
b_polygon_37_ = visual.Rect(
    win=win, name='b_polygon_37_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[11]], y[position[11]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-13.0, interpolate=True)
b_polygon_38_ = visual.Rect(
    win=win, name='b_polygon_38_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[12]], y[position[12]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-14.0, interpolate=True)
b_polygon_39_ = visual.Rect(
    win=win, name='b_polygon_39_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[13]], y[position[13]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-15.0, interpolate=True)
b_polygon_40_ = visual.Rect(
    win=win, name='b_polygon_40_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[14]], y[position[14]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-16.0, interpolate=True)
b_polygon_41_ = visual.Rect(
    win=win, name='b_polygon_41_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[15]], y[position[15]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-17.0, interpolate=True)
b_polygon_42_ = visual.Rect(
    win=win, name='b_polygon_42_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[16]], y[position[16]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-18.0, interpolate=True)
b_polygon_43_ = visual.Rect(
    win=win, name='b_polygon_43_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[17]], y[position[17]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-19.0, interpolate=True)
b_polygon_44_ = visual.Rect(
    win=win, name='b_polygon_44_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[18]], y[position[18]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-20.0, interpolate=True)
b_polygon_45_ = visual.Rect(
    win=win, name='b_polygon_45_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[19]], y[position[19]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-21.0, interpolate=True)
b_polygon_46_ = visual.Rect(
    win=win, name='b_polygon_46_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[20]], y[position[20]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-22.0, interpolate=True)
b_polygon_47_ = visual.Rect(
    win=win, name='b_polygon_47_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[21]], y[position[21]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-23.0, interpolate=True)
b_polygon_48_ = visual.Rect(
    win=win, name='b_polygon_48_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[22]], y[position[22]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-24.0, interpolate=True)
b_polygon_49_ = visual.Rect(
    win=win, name='b_polygon_49_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[23]], y[position[23]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-25.0, interpolate=True)
b_polygon_50_ = visual.Rect(
    win=win, name='b_polygon_50_',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[24]], y[position[24]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-26.0, interpolate=True)
b_text_26_ = visual.TextStim(win=win, name='b_text_26_',
    text=number[0],
    font='Arial',
    pos=[x[position[0]], y[position[0]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-27.0);
b_text_27_ = visual.TextStim(win=win, name='b_text_27_',
    text=number[1],
    font='Arial',
    pos=[x[position[1]], y[position[1]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-28.0);
b_text_28_ = visual.TextStim(win=win, name='b_text_28_',
    text=number[2],
    font='Arial',
    pos=[x[position[2]], y[position[2]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-29.0);
b_text_29_ = visual.TextStim(win=win, name='b_text_29_',
    text=number[3],
    font='Arial',
    pos=[x[position[3]], y[position[3]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-30.0);
b_text_30_ = visual.TextStim(win=win, name='b_text_30_',
    text=number[4],
    font='Arial',
    pos=[x[position[4]], y[position[4]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-31.0);
b_text_31_ = visual.TextStim(win=win, name='b_text_31_',
    text=number[5],
    font='Arial',
    pos=[x[position[5]], y[position[5]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-32.0);
b_text_32_ = visual.TextStim(win=win, name='b_text_32_',
    text=number[6],
    font='Arial',
    pos=[x[position[6]], y[position[6]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-33.0);
b_text_33_ = visual.TextStim(win=win, name='b_text_33_',
    text=number[7],
    font='Arial',
    pos=[x[position[7]], y[position[7]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-34.0);
b_text_34_ = visual.TextStim(win=win, name='b_text_34_',
    text=number[8],
    font='Arial',
    pos=[x[position[8]], y[position[8]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-35.0);
b_text_35_ = visual.TextStim(win=win, name='b_text_35_',
    text=number[9],
    font='Arial',
    pos=[x[position[9]], y[position[9]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-36.0);
b_text_36_ = visual.TextStim(win=win, name='b_text_36_',
    text=number[10],
    font='Arial',
    pos=[x[position[10]], y[position[10]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-37.0);
b_text_37_ = visual.TextStim(win=win, name='b_text_37_',
    text=number[11],
    font='Arial',
    pos=[x[position[11]], y[position[11]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-38.0);
b_text_38_ = visual.TextStim(win=win, name='b_text_38_',
    text=number[12],
    font='Arial',
    pos=[x[position[12]], y[position[12]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-39.0);
b_text_39_ = visual.TextStim(win=win, name='b_text_39_',
    text=number[13],
    font='Arial',
    pos=[x[position[13]], y[position[13]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-40.0);
b_text_40_ = visual.TextStim(win=win, name='b_text_40_',
    text=number[14],
    font='Arial',
    pos=[x[position[14]], y[position[14]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-41.0);
b_text_41_ = visual.TextStim(win=win, name='b_text_41_',
    text=number[15],
    font='Arial',
    pos=[x[position[15]], y[position[15]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-42.0);
b_text_42_ = visual.TextStim(win=win, name='b_text_42_',
    text=number[16],
    font='Arial',
    pos=[x[position[16]], y[position[16]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-43.0);
b_text_43_ = visual.TextStim(win=win, name='b_text_43_',
    text=number[17],
    font='Arial',
    pos=[x[position[17]], y[position[17]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-44.0);
b_text_44_ = visual.TextStim(win=win, name='b_text_44_',
    text=number[18],
    font='Arial',
    pos=[x[position[18]], y[position[18]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-45.0);
b_text_45_ = visual.TextStim(win=win, name='b_text_45_',
    text=number[19],
    font='Arial',
    pos=[x[position[19]], y[position[19]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-46.0);
b_text_46_ = visual.TextStim(win=win, name='b_text_46_',
    text=number[20],
    font='Arial',
    pos=[x[position[20]], y[position[20]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-47.0);
b_text_47_ = visual.TextStim(win=win, name='b_text_47_',
    text=number[21],
    font='Arial',
    pos=[x[position[21]], y[position[21]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-48.0);
b_text_48_ = visual.TextStim(win=win, name='b_text_48_',
    text=number[22],
    font='Arial',
    pos=[x[position[22]], y[position[22]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-49.0);
b_text_49_ = visual.TextStim(win=win, name='b_text_49_',
    text=number[23],
    font='Arial',
    pos=[x[position[23]], y[position[23]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-50.0);
b_text_50_ = visual.TextStim(win=win, name='b_text_50_',
    text=number[24],
    font='Arial',
    pos=[x[position[24]], y[position[24]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-51.0);
polygon_51 = visual.Rect(
    win=win, name='polygon_51',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[25]], y[position[25]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-52.0, interpolate=True)
polygon_52 = visual.Rect(
    win=win, name='polygon_52',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[26]], y[position[26]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-53.0, interpolate=True)
polygon_53 = visual.Rect(
    win=win, name='polygon_53',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[27]], y[position[27]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-54.0, interpolate=True)
polygon_54 = visual.Rect(
    win=win, name='polygon_54',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[28]], y[position[28]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-55.0, interpolate=True)
polygon_55 = visual.Rect(
    win=win, name='polygon_55',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[29]], y[position[29]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-56.0, interpolate=True)
polygon_56 = visual.Rect(
    win=win, name='polygon_56',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[30]], y[position[30]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-57.0, interpolate=True)
polygon_57 = visual.Rect(
    win=win, name='polygon_57',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[31]], y[position[31]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-58.0, interpolate=True)
polygon_58 = visual.Rect(
    win=win, name='polygon_58',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[32]], y[position[32]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-59.0, interpolate=True)
polygon_59 = visual.Rect(
    win=win, name='polygon_59',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[33]], y[position[33]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-60.0, interpolate=True)
polygon_60 = visual.Rect(
    win=win, name='polygon_60',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[34]], y[position[34]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-61.0, interpolate=True)
polygon_61 = visual.Rect(
    win=win, name='polygon_61',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[35]], y[position[35]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-62.0, interpolate=True)
text_51 = visual.TextStim(win=win, name='text_51',
    text=number[25],
    font='Arial',
    pos=[x[position[25]], y[position[25]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-63.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text=number[26],
    font='Arial',
    pos=[x[position[26]], y[position[26]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-64.0);
text_53 = visual.TextStim(win=win, name='text_53',
    text=number[27],
    font='Arial',
    pos=[x[position[27]], y[position[27]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-65.0);
text_54 = visual.TextStim(win=win, name='text_54',
    text=number[28],
    font='Arial',
    pos=[x[position[28]], y[position[28]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-66.0);
text_55 = visual.TextStim(win=win, name='text_55',
    text=number[29],
    font='Arial',
    pos=[x[position[29]], y[position[29]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-67.0);
text_56 = visual.TextStim(win=win, name='text_56',
    text=number[30],
    font='Arial',
    pos=[x[position[30]], y[position[30]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-68.0);
text_57 = visual.TextStim(win=win, name='text_57',
    text=number[31],
    font='Arial',
    pos=[x[position[31]], y[position[31]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-69.0);
text_58 = visual.TextStim(win=win, name='text_58',
    text=number[32],
    font='Arial',
    pos=[x[position[32]], y[position[32]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-70.0);
text_59 = visual.TextStim(win=win, name='text_59',
    text=number[33],
    font='Arial',
    pos=[x[position[33]], y[position[33]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-71.0);
text_60 = visual.TextStim(win=win, name='text_60',
    text=number[34],
    font='Arial',
    pos=[x[position[34]], y[position[34]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-72.0);
text_61 = visual.TextStim(win=win, name='text_61',
    text=number[35],
    font='Arial',
    pos=[x[position[35]], y[position[35]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-73.0);
polygon_62 = visual.Rect(
    win=win, name='polygon_62',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[36]], y[position[36]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-74.0, interpolate=True)
polygon_63 = visual.Rect(
    win=win, name='polygon_63',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[37]], y[position[37]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-75.0, interpolate=True)
polygon_64 = visual.Rect(
    win=win, name='polygon_64',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[38]], y[position[38]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-76.0, interpolate=True)
polygon_65 = visual.Rect(
    win=win, name='polygon_65',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[39]], y[position[39]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-77.0, interpolate=True)
polygon_66 = visual.Rect(
    win=win, name='polygon_66',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[40]], y[position[40]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-78.0, interpolate=True)
polygon_67 = visual.Rect(
    win=win, name='polygon_67',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[41]], y[position[41]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-79.0, interpolate=True)
polygon_68 = visual.Rect(
    win=win, name='polygon_68',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[42]], y[position[42]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-80.0, interpolate=True)
polygon_69 = visual.Rect(
    win=win, name='polygon_69',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[43]], y[position[43]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-81.0, interpolate=True)
polygon_70 = visual.Rect(
    win=win, name='polygon_70',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[44]], y[position[44]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-82.0, interpolate=True)
polygon_71 = visual.Rect(
    win=win, name='polygon_71',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[45]], y[position[45]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-83.0, interpolate=True)
polygon_72 = visual.Rect(
    win=win, name='polygon_72',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[46]], y[position[46]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-84.0, interpolate=True)
polygon_73 = visual.Rect(
    win=win, name='polygon_73',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[47]], y[position[47]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-85.0, interpolate=True)
polygon_74 = visual.Rect(
    win=win, name='polygon_74',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[48]], y[position[48]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-86.0, interpolate=True)
text_62 = visual.TextStim(win=win, name='text_62',
    text=number[36],
    font='Arial',
    pos=[x[position[36]], y[position[36]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-87.0);
text_63 = visual.TextStim(win=win, name='text_63',
    text=number[37],
    font='Arial',
    pos=[x[position[37]], y[position[37]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-88.0);
text_64 = visual.TextStim(win=win, name='text_64',
    text=number[38],
    font='Arial',
    pos=[x[position[38]], y[position[38]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-89.0);
text_65 = visual.TextStim(win=win, name='text_65',
    text=number[39],
    font='Arial',
    pos=[x[position[39]], y[position[39]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-90.0);
text_66 = visual.TextStim(win=win, name='text_66',
    text=number[40],
    font='Arial',
    pos=[x[position[40]], y[position[40]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-91.0);
text_67 = visual.TextStim(win=win, name='text_67',
    text=number[41],
    font='Arial',
    pos=[x[position[41]], y[position[41]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-92.0);
text_68 = visual.TextStim(win=win, name='text_68',
    text=number[42],
    font='Arial',
    pos=[x[position[42]], y[position[42]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-93.0);
text_69 = visual.TextStim(win=win, name='text_69',
    text=number[43],
    font='Arial',
    pos=[x[position[43]], y[position[43]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-94.0);
text_70 = visual.TextStim(win=win, name='text_70',
    text=number[44],
    font='Arial',
    pos=[x[position[44]], y[position[44]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-95.0);
text_71 = visual.TextStim(win=win, name='text_71',
    text=number[45],
    font='Arial',
    pos=[x[position[45]], y[position[45]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-96.0);
text_72 = visual.TextStim(win=win, name='text_72',
    text=number[46],
    font='Arial',
    pos=[x[position[46]], y[position[46]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-97.0);
text_73 = visual.TextStim(win=win, name='text_73',
    text=number[47],
    font='Arial',
    pos=[x[position[47]], y[position[47]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-98.0);
text_74 = visual.TextStim(win=win, name='text_74',
    text=number[48],
    font='Arial',
    pos=[x[position[48]], y[position[48]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-99.0);
polygon_75 = visual.Rect(
    win=win, name='polygon_75',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[49]], y[position[49]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-100.0, interpolate=True)
polygon_76 = visual.Rect(
    win=win, name='polygon_76',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[50]], y[position[50]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-101.0, interpolate=True)
polygon_77 = visual.Rect(
    win=win, name='polygon_77',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[51]], y[position[51]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-102.0, interpolate=True)
polygon_78 = visual.Rect(
    win=win, name='polygon_78',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[52]], y[position[52]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-103.0, interpolate=True)
polygon_79 = visual.Rect(
    win=win, name='polygon_79',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[53]], y[position[53]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-104.0, interpolate=True)
polygon_80 = visual.Rect(
    win=win, name='polygon_80',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[54]], y[position[54]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-105.0, interpolate=True)
polygon_81 = visual.Rect(
    win=win, name='polygon_81',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[55]], y[position[55]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-106.0, interpolate=True)
polygon_82 = visual.Rect(
    win=win, name='polygon_82',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[56]], y[position[56]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-107.0, interpolate=True)
polygon_83 = visual.Rect(
    win=win, name='polygon_83',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[57]], y[position[57]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-108.0, interpolate=True)
polygon_84 = visual.Rect(
    win=win, name='polygon_84',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[58]], y[position[58]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-109.0, interpolate=True)
polygon_85 = visual.Rect(
    win=win, name='polygon_85',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[59]], y[position[59]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-110.0, interpolate=True)
polygon_86 = visual.Rect(
    win=win, name='polygon_86',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[60]], y[position[60]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-111.0, interpolate=True)
polygon_87 = visual.Rect(
    win=win, name='polygon_87',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[61]], y[position[61]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-112.0, interpolate=True)
polygon_88 = visual.Rect(
    win=win, name='polygon_88',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[62]], y[position[62]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-113.0, interpolate=True)
text_75 = visual.TextStim(win=win, name='text_75',
    text=number[49],
    font='Arial',
    pos=[x[position[49]], y[position[49]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-114.0);
text_76 = visual.TextStim(win=win, name='text_76',
    text=number[50],
    font='Arial',
    pos=[x[position[50]], y[position[50]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-115.0);
text_77 = visual.TextStim(win=win, name='text_77',
    text=number[51],
    font='Arial',
    pos=[x[position[51]], y[position[51]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-116.0);
text_78 = visual.TextStim(win=win, name='text_78',
    text=number[52],
    font='Arial',
    pos=[x[position[52]], y[position[52]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-117.0);
text_79 = visual.TextStim(win=win, name='text_79',
    text=number[53],
    font='Arial',
    pos=[x[position[53]], y[position[53]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-118.0);
text_80 = visual.TextStim(win=win, name='text_80',
    text=number[54],
    font='Arial',
    pos=[x[position[54]], y[position[54]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-119.0);
text_81 = visual.TextStim(win=win, name='text_81',
    text=number[55],
    font='Arial',
    pos=[x[position[55]], y[position[55]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-120.0);
text_82 = visual.TextStim(win=win, name='text_82',
    text=number[56],
    font='Arial',
    pos=[x[position[56]], y[position[56]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-121.0);
text_83 = visual.TextStim(win=win, name='text_83',
    text=number[57],
    font='Arial',
    pos=[x[position[57]], y[position[57]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-122.0);
text_84 = visual.TextStim(win=win, name='text_84',
    text=number[58],
    font='Arial',
    pos=[x[position[58]], y[position[58]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-123.0);
text_85 = visual.TextStim(win=win, name='text_85',
    text=number[59],
    font='Arial',
    pos=[x[position[59]], y[position[59]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-124.0);
text_86 = visual.TextStim(win=win, name='text_86',
    text=number[60],
    font='Arial',
    pos=[x[position[60]], y[position[60]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-125.0);
text_87 = visual.TextStim(win=win, name='text_87',
    text=number[61],
    font='Arial',
    pos=[x[position[61]], y[position[61]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-126.0);
text_88 = visual.TextStim(win=win, name='text_88',
    text=number[62],
    font='Arial',
    pos=[x[position[62]], y[position[62]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-127.0);
polygon_89 = visual.Rect(
    win=win, name='polygon_89',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[63]], y[position[63]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-128.0, interpolate=True)
polygon_90 = visual.Rect(
    win=win, name='polygon_90',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[64]], y[position[64]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-129.0, interpolate=True)
polygon_91 = visual.Rect(
    win=win, name='polygon_91',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[65]], y[position[65]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-130.0, interpolate=True)
polygon_92 = visual.Rect(
    win=win, name='polygon_92',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[66]], y[position[66]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-131.0, interpolate=True)
polygon_93 = visual.Rect(
    win=win, name='polygon_93',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[67]], y[position[67]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-132.0, interpolate=True)
polygon_94 = visual.Rect(
    win=win, name='polygon_94',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[68]], y[position[68]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-133.0, interpolate=True)
polygon_95 = visual.Rect(
    win=win, name='polygon_95',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[69]], y[position[69]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-134.0, interpolate=True)
polygon_96 = visual.Rect(
    win=win, name='polygon_96',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[70]], y[position[70]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-135.0, interpolate=True)
polygon_97 = visual.Rect(
    win=win, name='polygon_97',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[71]], y[position[71]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-136.0, interpolate=True)
polygon_98 = visual.Rect(
    win=win, name='polygon_98',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[72]], y[position[72]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-137.0, interpolate=True)
polygon_99 = visual.Rect(
    win=win, name='polygon_99',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[73]], y[position[73]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-138.0, interpolate=True)
polygon_100 = visual.Rect(
    win=win, name='polygon_100',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[74]], y[position[74]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-139.0, interpolate=True)
polygon_101 = visual.Rect(
    win=win, name='polygon_101',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[75]], y[position[75]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-140.0, interpolate=True)
polygon_102 = visual.Rect(
    win=win, name='polygon_102',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[76]], y[position[76]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-141.0, interpolate=True)
polygon_103 = visual.Rect(
    win=win, name='polygon_103',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[77]], y[position[77]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-142.0, interpolate=True)
polygon_104 = visual.Rect(
    win=win, name='polygon_104',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[78]], y[position[78]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-143.0, interpolate=True)
polygon_105 = visual.Rect(
    win=win, name='polygon_105',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[79]], y[position[79]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-144.0, interpolate=True)
polygon_106 = visual.Rect(
    win=win, name='polygon_106',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[80]], y[position[80]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-145.0, interpolate=True)
polygon_107 = visual.Rect(
    win=win, name='polygon_107',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[81]], y[position[81]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-146.0, interpolate=True)
polygon_108 = visual.Rect(
    win=win, name='polygon_108',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[82]], y[position[82]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-147.0, interpolate=True)
polygon_109 = visual.Rect(
    win=win, name='polygon_109',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[83]], y[position[83]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-148.0, interpolate=True)
polygon_110 = visual.Rect(
    win=win, name='polygon_110',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[84]], y[position[84]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-149.0, interpolate=True)
polygon_111 = visual.Rect(
    win=win, name='polygon_111',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[85]], y[position[85]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-150.0, interpolate=True)
polygon_112 = visual.Rect(
    win=win, name='polygon_112',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[86]], y[position[86]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-151.0, interpolate=True)
polygon_113 = visual.Rect(
    win=win, name='polygon_113',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[87]], y[position[87]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-152.0, interpolate=True)
polygon_114 = visual.Rect(
    win=win, name='polygon_114',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[88]], y[position[88]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-153.0, interpolate=True)
polygon_115 = visual.Rect(
    win=win, name='polygon_115',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[89]], y[position[89]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-154.0, interpolate=True)
polygon_116 = visual.Rect(
    win=win, name='polygon_116',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[90]], y[position[90]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-155.0, interpolate=True)
text_89 = visual.TextStim(win=win, name='text_89',
    text=number[63],
    font='Arial',
    pos=[x[position[63]], y[position[63]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-156.0);
text_90 = visual.TextStim(win=win, name='text_90',
    text=number[64],
    font='Arial',
    pos=[x[position[64]], y[position[64]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-157.0);
text_91 = visual.TextStim(win=win, name='text_91',
    text=number[65],
    font='Arial',
    pos=[x[position[65]], y[position[65]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-158.0);
text_92 = visual.TextStim(win=win, name='text_92',
    text=number[66],
    font='Arial',
    pos=[x[position[66]], y[position[66]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-159.0);
text_93 = visual.TextStim(win=win, name='text_93',
    text=number[67],
    font='Arial',
    pos=[x[position[67]], y[position[67]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-160.0);
text_94 = visual.TextStim(win=win, name='text_94',
    text=number[68],
    font='Arial',
    pos=[x[position[68]], y[position[68]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-161.0);
text_95 = visual.TextStim(win=win, name='text_95',
    text=number[69],
    font='Arial',
    pos=[x[position[69]], y[position[69]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-162.0);
text_96 = visual.TextStim(win=win, name='text_96',
    text=number[70],
    font='Arial',
    pos=[x[position[70]], y[position[70]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-163.0);
text_97 = visual.TextStim(win=win, name='text_97',
    text=number[71],
    font='Arial',
    pos=[x[position[71]], y[position[71]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-164.0);
text_98 = visual.TextStim(win=win, name='text_98',
    text=number[72],
    font='Arial',
    pos=[x[position[72]], y[position[72]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-165.0);
text_99 = visual.TextStim(win=win, name='text_99',
    text=number[73],
    font='Arial',
    pos=[x[position[73]], y[position[73]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-166.0);
text_100 = visual.TextStim(win=win, name='text_100',
    text=number[74],
    font='Arial',
    pos=[x[position[74]], y[position[74]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-167.0);
text_101 = visual.TextStim(win=win, name='text_101',
    text=number[75],
    font='Arial',
    pos=[x[position[75]], y[position[75]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-168.0);
text_102 = visual.TextStim(win=win, name='text_102',
    text=number[76],
    font='Arial',
    pos=[x[position[76]], y[position[76]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-169.0);
text_103 = visual.TextStim(win=win, name='text_103',
    text=number[77],
    font='Arial',
    pos=[x[position[77]], y[position[77]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-170.0);
text_104 = visual.TextStim(win=win, name='text_104',
    text=number[78],
    font='Arial',
    pos=[x[position[78]], y[position[78]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-171.0);
text_105 = visual.TextStim(win=win, name='text_105',
    text=number[79],
    font='Arial',
    pos=[x[position[79]], y[position[79]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-172.0);
text_106 = visual.TextStim(win=win, name='text_106',
    text=number[80],
    font='Arial',
    pos=[x[position[80]], y[position[80]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-173.0);
text_107 = visual.TextStim(win=win, name='text_107',
    text=number[81],
    font='Arial',
    pos=[x[position[81]], y[position[81]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-174.0);
text_108 = visual.TextStim(win=win, name='text_108',
    text=number[82],
    font='Arial',
    pos=[x[position[82]], y[position[82]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-175.0);
text_109 = visual.TextStim(win=win, name='text_109',
    text=number[83],
    font='Arial',
    pos=[x[position[83]], y[position[83]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-176.0);
text_110 = visual.TextStim(win=win, name='text_110',
    text=number[84],
    font='Arial',
    pos=[x[position[84]], y[position[84]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-177.0);
text_111 = visual.TextStim(win=win, name='text_111',
    text=number[85],
    font='Arial',
    pos=[x[position[85]], y[position[85]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-178.0);
text_112 = visual.TextStim(win=win, name='text_112',
    text=number[86],
    font='Arial',
    pos=[x[position[86]], y[position[86]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-179.0);
text_113 = visual.TextStim(win=win, name='text_113',
    text=number[87],
    font='Arial',
    pos=[x[position[87]], y[position[87]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-180.0);
text_114 = visual.TextStim(win=win, name='text_114',
    text=number[88],
    font='Arial',
    pos=[x[position[88]], y[position[88]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-181.0);
text_115 = visual.TextStim(win=win, name='text_115',
    text=number[89],
    font='Arial',
    pos=[x[position[89]], y[position[89]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-182.0);
text_116 = visual.TextStim(win=win, name='text_116',
    text=number[90],
    font='Arial',
    pos=[x[position[90]], y[position[90]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-183.0);
polygon_117 = visual.Rect(
    win=win, name='polygon_117',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[91]], y[position[91]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-184.0, interpolate=True)
polygon_118 = visual.Rect(
    win=win, name='polygon_118',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[92]], y[position[92]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-185.0, interpolate=True)
polygon_119 = visual.Rect(
    win=win, name='polygon_119',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[93]], y[position[93]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-186.0, interpolate=True)
polygon_120 = visual.Rect(
    win=win, name='polygon_120',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[94]], y[position[94]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-187.0, interpolate=True)
polygon_121 = visual.Rect(
    win=win, name='polygon_121',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[95]], y[position[95]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-188.0, interpolate=True)
polygon_122 = visual.Rect(
    win=win, name='polygon_122',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[96]], y[position[96]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-189.0, interpolate=True)
polygon_123 = visual.Rect(
    win=win, name='polygon_123',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[97]], y[position[97]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-190.0, interpolate=True)
polygon_124 = visual.Rect(
    win=win, name='polygon_124',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[98]], y[position[98]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-191.0, interpolate=True)
polygon_125 = visual.Rect(
    win=win, name='polygon_125',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[99]], y[position[99]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-192.0, interpolate=True)
polygon_126 = visual.Rect(
    win=win, name='polygon_126',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[100]], y[position[100]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-193.0, interpolate=True)
polygon_127 = visual.Rect(
    win=win, name='polygon_127',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[101]], y[position[101]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-194.0, interpolate=True)
polygon_128 = visual.Rect(
    win=win, name='polygon_128',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[102]], y[position[102]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-195.0, interpolate=True)
polygon_129 = visual.Rect(
    win=win, name='polygon_129',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[103]], y[position[103]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-196.0, interpolate=True)
polygon_130 = visual.Rect(
    win=win, name='polygon_130',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[104]], y[position[104]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-197.0, interpolate=True)
polygon_131 = visual.Rect(
    win=win, name='polygon_131',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[105]], y[position[105]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-198.0, interpolate=True)
polygon_132 = visual.Rect(
    win=win, name='polygon_132',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[106]], y[position[106]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-199.0, interpolate=True)
polygon_133 = visual.Rect(
    win=win, name='polygon_133',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[107]], y[position[107]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-200.0, interpolate=True)
polygon_134 = visual.Rect(
    win=win, name='polygon_134',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[108]], y[position[108]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-201.0, interpolate=True)
polygon_135 = visual.Rect(
    win=win, name='polygon_135',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[109]], y[position[109]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-202.0, interpolate=True)
polygon_136 = visual.Rect(
    win=win, name='polygon_136',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[110]], y[position[110]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-203.0, interpolate=True)
polygon_137 = visual.Rect(
    win=win, name='polygon_137',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[111]], y[position[111]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-204.0, interpolate=True)
polygon_138 = visual.Rect(
    win=win, name='polygon_138',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[112]], y[position[112]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-205.0, interpolate=True)
polygon_139 = visual.Rect(
    win=win, name='polygon_139',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[113]], y[position[113]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-206.0, interpolate=True)
polygon_140 = visual.Rect(
    win=win, name='polygon_140',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[114]], y[position[114]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-207.0, interpolate=True)
polygon_141 = visual.Rect(
    win=win, name='polygon_141',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[115]], y[position[115]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-208.0, interpolate=True)
polygon_142 = visual.Rect(
    win=win, name='polygon_142',
    width=[size, size][0], height=[size, size][1],
    ori=0, pos=[x[position[116]], y[position[116]]],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=color, fillColorSpace='rgb',
    opacity=1.0, depth=-209.0, interpolate=True)
text_117 = visual.TextStim(win=win, name='text_117',
    text=number[91],
    font='Arial',
    pos=[x[position[91]], y[position[91]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-210.0);
text_118 = visual.TextStim(win=win, name='text_118',
    text=number[92],
    font='Arial',
    pos=[x[position[92]], y[position[92]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-211.0);
text_119 = visual.TextStim(win=win, name='text_119',
    text=number[93],
    font='Arial',
    pos=[x[position[93]], y[position[93]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-212.0);
text_120 = visual.TextStim(win=win, name='text_120',
    text=number[94],
    font='Arial',
    pos=[x[position[94]], y[position[94]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-213.0);
text_121 = visual.TextStim(win=win, name='text_121',
    text=number[95],
    font='Arial',
    pos=[x[position[95]], y[position[95]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-214.0);
text_122 = visual.TextStim(win=win, name='text_122',
    text=number[96],
    font='Arial',
    pos=[x[position[96]], y[position[96]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-215.0);
text_123 = visual.TextStim(win=win, name='text_123',
    text=number[97],
    font='Arial',
    pos=[x[position[97]], y[position[97]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-216.0);
text_124 = visual.TextStim(win=win, name='text_124',
    text=number[98],
    font='Arial',
    pos=[x[position[98]], y[position[98]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-217.0);
text_125 = visual.TextStim(win=win, name='text_125',
    text=number[99],
    font='Arial',
    pos=[x[position[99]], y[position[99]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-218.0);
text_126 = visual.TextStim(win=win, name='text_126',
    text=number[100],
    font='Arial',
    pos=[x[position[100]], y[position[100]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-219.0);
text_127 = visual.TextStim(win=win, name='text_127',
    text=number[101],
    font='Arial',
    pos=[x[position[101]], y[position[101]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-220.0);
text_128 = visual.TextStim(win=win, name='text_128',
    text=number[102],
    font='Arial',
    pos=[x[position[102]], y[position[102]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-221.0);
text_129 = visual.TextStim(win=win, name='text_129',
    text=number[103],
    font='Arial',
    pos=[x[position[103]], y[position[103]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-222.0);
text_130 = visual.TextStim(win=win, name='text_130',
    text=number[104],
    font='Arial',
    pos=[x[position[104]], y[position[104]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-223.0);
text_131 = visual.TextStim(win=win, name='text_131',
    text=number[105],
    font='Arial',
    pos=[x[position[105]], y[position[105]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-224.0);
text_132 = visual.TextStim(win=win, name='text_132',
    text=number[106],
    font='Arial',
    pos=[x[position[106]], y[position[106]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-225.0);
text_133 = visual.TextStim(win=win, name='text_133',
    text=number[107],
    font='Arial',
    pos=[x[position[107]], y[position[107]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-226.0);
text_134 = visual.TextStim(win=win, name='text_134',
    text=number[108],
    font='Arial',
    pos=[x[position[108]], y[position[108]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-227.0);
text_135 = visual.TextStim(win=win, name='text_135',
    text=number[109],
    font='Arial',
    pos=[x[position[109]], y[position[109]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-228.0);
text_136 = visual.TextStim(win=win, name='text_136',
    text=number[110],
    font='Arial',
    pos=[x[position[110]], y[position[110]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-229.0);
text_137 = visual.TextStim(win=win, name='text_137',
    text=number[111],
    font='Arial',
    pos=[x[position[111]], y[position[111]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-230.0);
text_138 = visual.TextStim(win=win, name='text_138',
    text=number[112],
    font='Arial',
    pos=[x[position[112]], y[position[112]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-231.0);
text_139 = visual.TextStim(win=win, name='text_139',
    text=number[113],
    font='Arial',
    pos=[x[position[113]], y[position[113]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-232.0);
text_140 = visual.TextStim(win=win, name='text_140',
    text=number[114],
    font='Arial',
    pos=[x[position[114]], y[position[114]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-233.0);
text_141 = visual.TextStim(win=win, name='text_141',
    text=number[115],
    font='Arial',
    pos=[x[position[115]], y[position[115]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-234.0);
text_142 = visual.TextStim(win=win, name='text_142',
    text=number[116],
    font='Arial',
    pos=[x[position[116]], y[position[116]]], height=number_size, wrapWidth=None, ori=0, 
    color=number_color, colorSpace='rgb', opacity=1.0,
    depth=-235.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
readyComponents = [key_resp_2, image]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_9_13"-------
    t = 0
    routine_9_13Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the b_mouse_2_
    gotValidClick = False  # until a click is received
    #timerの起動
    timer = core.Clock()
    
    #指標の取得
    
    number_touch = []
    number_time = []
    click_miss_list = []
    
    
    # keep track of which components have finished
    routine_9_13Components = [b_mouse_2_, b_polygon_26_, b_polygon_27_, b_polygon_28_, b_polygon_29_, b_polygon_30_, b_polygon_31_, b_polygon_32_, b_polygon_33_, b_polygon_34_, b_polygon_35_, b_polygon_36_, b_polygon_37_, b_polygon_38_, b_polygon_39_, b_polygon_40_, b_polygon_41_, b_polygon_42_, b_polygon_43_, b_polygon_44_, b_polygon_45_, b_polygon_46_, b_polygon_47_, b_polygon_48_, b_polygon_49_, b_polygon_50_, b_text_26_, b_text_27_, b_text_28_, b_text_29_, b_text_30_, b_text_31_, b_text_32_, b_text_33_, b_text_34_, b_text_35_, b_text_36_, b_text_37_, b_text_38_, b_text_39_, b_text_40_, b_text_41_, b_text_42_, b_text_43_, b_text_44_, b_text_45_, b_text_46_, b_text_47_, b_text_48_, b_text_49_, b_text_50_, polygon_51, polygon_52, polygon_53, polygon_54, polygon_55, polygon_56, polygon_57, polygon_58, polygon_59, polygon_60, polygon_61, text_51, text_52, text_53, text_54, text_55, text_56, text_57, text_58, text_59, text_60, text_61, polygon_62, polygon_63, polygon_64, polygon_65, polygon_66, polygon_67, polygon_68, polygon_69, polygon_70, polygon_71, polygon_72, polygon_73, polygon_74, text_62, text_63, text_64, text_65, text_66, text_67, text_68, text_69, text_70, text_71, text_72, text_73, text_74, polygon_75, polygon_76, polygon_77, polygon_78, polygon_79, polygon_80, polygon_81, polygon_82, polygon_83, polygon_84, polygon_85, polygon_86, polygon_87, polygon_88, text_75, text_76, text_77, text_78, text_79, text_80, text_81, text_82, text_83, text_84, text_85, text_86, text_87, text_88, polygon_89, polygon_90, polygon_91, polygon_92, polygon_93, polygon_94, polygon_95, polygon_96, polygon_97, polygon_98, polygon_99, polygon_100, polygon_101, polygon_102, polygon_103, polygon_104, polygon_105, polygon_106, polygon_107, polygon_108, polygon_109, polygon_110, polygon_111, polygon_112, polygon_113, polygon_114, polygon_115, polygon_116, text_89, text_90, text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, text_100, text_101, text_102, text_103, text_104, text_105, text_106, text_107, text_108, text_109, text_110, text_111, text_112, text_113, text_114, text_115, text_116, polygon_117, polygon_118, polygon_119, polygon_120, polygon_121, polygon_122, polygon_123, polygon_124, polygon_125, polygon_126, polygon_127, polygon_128, polygon_129, polygon_130, polygon_131, polygon_132, polygon_133, polygon_134, polygon_135, polygon_136, polygon_137, polygon_138, polygon_139, polygon_140, polygon_141, polygon_142, text_117, text_118, text_119, text_120, text_121, text_122, text_123, text_124, text_125, text_126, text_127, text_128, text_129, text_130, text_131, text_132, text_133, text_134, text_135, text_136, text_137, text_138, text_139, text_140, text_141, text_142]
    for thisComponent in routine_9_13Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_9_13"-------
    while continueRoutine:
        # get current time
        t = routine_9_13Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        #マウス情報の読み込み
        mousePos = b_mouse_2_.getPos()
        buttonStatus = b_mouse_2_.getPressed( )
        
        bx = [x + y for(x,y) in zip(targetPx[target],a)]
        sx = [k - j for(k,j) in zip(targetPx[target],a)]
        by = [x + y for(x,y) in zip(targetPy[target],a)]
        sy = [k - j for(k,j) in zip(targetPy[target],a)]
        
        
        #クリック判定
        if mousePos[0]  <  bx   and mousePos[0] > sx  and mousePos[1]  <  by   and mousePos[1] > sy and buttonStatus[0] == 1:
            Tr[target] = 0.4
            number_touch.append(target + 1)
            number_time.append(timer.getTime())
            click_miss_list.append(click_miss)
            click_miss = 0
            if target+1 < num_amount:
                target = target + 1
            else:
                continueRoutine = False
        elif buttonStatus[0] == 1:
            click_miss = click_miss + 1
        
        
        if timer.getTime() > 240:
            continueRoutine = False
        
        # *b_polygon_26_* updates
        if t >= 0.0 and b_polygon_26_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_26_.tStart = t
            b_polygon_26_.frameNStart = frameN  # exact frame index
            b_polygon_26_.setAutoDraw(True)
        if b_polygon_26_.status == STARTED:  # only update if drawing
            b_polygon_26_.setOpacity(Tr[0], log=False)
        
        # *b_polygon_27_* updates
        if t >= 0.0 and b_polygon_27_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_27_.tStart = t
            b_polygon_27_.frameNStart = frameN  # exact frame index
            b_polygon_27_.setAutoDraw(True)
        if b_polygon_27_.status == STARTED:  # only update if drawing
            b_polygon_27_.setOpacity(Tr[1], log=False)
        
        # *b_polygon_28_* updates
        if t >= 0.0 and b_polygon_28_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_28_.tStart = t
            b_polygon_28_.frameNStart = frameN  # exact frame index
            b_polygon_28_.setAutoDraw(True)
        if b_polygon_28_.status == STARTED:  # only update if drawing
            b_polygon_28_.setOpacity(Tr[2], log=False)
        
        # *b_polygon_29_* updates
        if t >= 0.0 and b_polygon_29_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_29_.tStart = t
            b_polygon_29_.frameNStart = frameN  # exact frame index
            b_polygon_29_.setAutoDraw(True)
        if b_polygon_29_.status == STARTED:  # only update if drawing
            b_polygon_29_.setOpacity(Tr[3], log=False)
        
        # *b_polygon_30_* updates
        if t >= 0.0 and b_polygon_30_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_30_.tStart = t
            b_polygon_30_.frameNStart = frameN  # exact frame index
            b_polygon_30_.setAutoDraw(True)
        if b_polygon_30_.status == STARTED:  # only update if drawing
            b_polygon_30_.setOpacity(Tr[4], log=False)
        
        # *b_polygon_31_* updates
        if t >= 0.0 and b_polygon_31_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_31_.tStart = t
            b_polygon_31_.frameNStart = frameN  # exact frame index
            b_polygon_31_.setAutoDraw(True)
        if b_polygon_31_.status == STARTED:  # only update if drawing
            b_polygon_31_.setOpacity(Tr[5], log=False)
        
        # *b_polygon_32_* updates
        if t >= 0.0 and b_polygon_32_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_32_.tStart = t
            b_polygon_32_.frameNStart = frameN  # exact frame index
            b_polygon_32_.setAutoDraw(True)
        if b_polygon_32_.status == STARTED:  # only update if drawing
            b_polygon_32_.setOpacity(Tr[6], log=False)
        
        # *b_polygon_33_* updates
        if t >= 0.0 and b_polygon_33_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_33_.tStart = t
            b_polygon_33_.frameNStart = frameN  # exact frame index
            b_polygon_33_.setAutoDraw(True)
        if b_polygon_33_.status == STARTED:  # only update if drawing
            b_polygon_33_.setOpacity(Tr[7], log=False)
        
        # *b_polygon_34_* updates
        if t >= 0.0 and b_polygon_34_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_34_.tStart = t
            b_polygon_34_.frameNStart = frameN  # exact frame index
            b_polygon_34_.setAutoDraw(True)
        if b_polygon_34_.status == STARTED:  # only update if drawing
            b_polygon_34_.setOpacity(Tr[8], log=False)
        
        # *b_polygon_35_* updates
        if t >= 0.0 and b_polygon_35_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_35_.tStart = t
            b_polygon_35_.frameNStart = frameN  # exact frame index
            b_polygon_35_.setAutoDraw(True)
        if b_polygon_35_.status == STARTED:  # only update if drawing
            b_polygon_35_.setOpacity(Tr[9], log=False)
        
        # *b_polygon_36_* updates
        if t >= 0.0 and b_polygon_36_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_36_.tStart = t
            b_polygon_36_.frameNStart = frameN  # exact frame index
            b_polygon_36_.setAutoDraw(True)
        if b_polygon_36_.status == STARTED:  # only update if drawing
            b_polygon_36_.setOpacity(Tr[10], log=False)
        
        # *b_polygon_37_* updates
        if t >= 0.0 and b_polygon_37_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_37_.tStart = t
            b_polygon_37_.frameNStart = frameN  # exact frame index
            b_polygon_37_.setAutoDraw(True)
        if b_polygon_37_.status == STARTED:  # only update if drawing
            b_polygon_37_.setOpacity(Tr[11], log=False)
        
        # *b_polygon_38_* updates
        if t >= 0.0 and b_polygon_38_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_38_.tStart = t
            b_polygon_38_.frameNStart = frameN  # exact frame index
            b_polygon_38_.setAutoDraw(True)
        if b_polygon_38_.status == STARTED:  # only update if drawing
            b_polygon_38_.setOpacity(Tr[12], log=False)
        
        # *b_polygon_39_* updates
        if t >= 0.0 and b_polygon_39_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_39_.tStart = t
            b_polygon_39_.frameNStart = frameN  # exact frame index
            b_polygon_39_.setAutoDraw(True)
        if b_polygon_39_.status == STARTED:  # only update if drawing
            b_polygon_39_.setOpacity(Tr[13], log=False)
        
        # *b_polygon_40_* updates
        if t >= 0.0 and b_polygon_40_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_40_.tStart = t
            b_polygon_40_.frameNStart = frameN  # exact frame index
            b_polygon_40_.setAutoDraw(True)
        if b_polygon_40_.status == STARTED:  # only update if drawing
            b_polygon_40_.setOpacity(Tr[14], log=False)
        
        # *b_polygon_41_* updates
        if t >= 0.0 and b_polygon_41_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_41_.tStart = t
            b_polygon_41_.frameNStart = frameN  # exact frame index
            b_polygon_41_.setAutoDraw(True)
        if b_polygon_41_.status == STARTED:  # only update if drawing
            b_polygon_41_.setOpacity(Tr[15], log=False)
        
        # *b_polygon_42_* updates
        if t >= 0.0 and b_polygon_42_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_42_.tStart = t
            b_polygon_42_.frameNStart = frameN  # exact frame index
            b_polygon_42_.setAutoDraw(True)
        if b_polygon_42_.status == STARTED:  # only update if drawing
            b_polygon_42_.setOpacity(Tr[16], log=False)
        
        # *b_polygon_43_* updates
        if t >= 0.0 and b_polygon_43_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_43_.tStart = t
            b_polygon_43_.frameNStart = frameN  # exact frame index
            b_polygon_43_.setAutoDraw(True)
        if b_polygon_43_.status == STARTED:  # only update if drawing
            b_polygon_43_.setOpacity(Tr[17], log=False)
        
        # *b_polygon_44_* updates
        if t >= 0.0 and b_polygon_44_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_44_.tStart = t
            b_polygon_44_.frameNStart = frameN  # exact frame index
            b_polygon_44_.setAutoDraw(True)
        if b_polygon_44_.status == STARTED:  # only update if drawing
            b_polygon_44_.setOpacity(Tr[18], log=False)
        
        # *b_polygon_45_* updates
        if t >= 0.0 and b_polygon_45_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_45_.tStart = t
            b_polygon_45_.frameNStart = frameN  # exact frame index
            b_polygon_45_.setAutoDraw(True)
        if b_polygon_45_.status == STARTED:  # only update if drawing
            b_polygon_45_.setOpacity(Tr[19], log=False)
        
        # *b_polygon_46_* updates
        if t >= 0.0 and b_polygon_46_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_46_.tStart = t
            b_polygon_46_.frameNStart = frameN  # exact frame index
            b_polygon_46_.setAutoDraw(True)
        if b_polygon_46_.status == STARTED:  # only update if drawing
            b_polygon_46_.setOpacity(Tr[20], log=False)
        
        # *b_polygon_47_* updates
        if t >= 0.0 and b_polygon_47_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_47_.tStart = t
            b_polygon_47_.frameNStart = frameN  # exact frame index
            b_polygon_47_.setAutoDraw(True)
        if b_polygon_47_.status == STARTED:  # only update if drawing
            b_polygon_47_.setOpacity(Tr[21], log=False)
        
        # *b_polygon_48_* updates
        if t >= 0.0 and b_polygon_48_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_48_.tStart = t
            b_polygon_48_.frameNStart = frameN  # exact frame index
            b_polygon_48_.setAutoDraw(True)
        if b_polygon_48_.status == STARTED:  # only update if drawing
            b_polygon_48_.setOpacity(Tr[22], log=False)
        
        # *b_polygon_49_* updates
        if t >= 0.0 and b_polygon_49_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_49_.tStart = t
            b_polygon_49_.frameNStart = frameN  # exact frame index
            b_polygon_49_.setAutoDraw(True)
        if b_polygon_49_.status == STARTED:  # only update if drawing
            b_polygon_49_.setOpacity(Tr[23], log=False)
        
        # *b_polygon_50_* updates
        if t >= 0.0 and b_polygon_50_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_polygon_50_.tStart = t
            b_polygon_50_.frameNStart = frameN  # exact frame index
            b_polygon_50_.setAutoDraw(True)
        if b_polygon_50_.status == STARTED:  # only update if drawing
            b_polygon_50_.setOpacity(Tr[24], log=False)
        
        # *b_text_26_* updates
        if t >= 0.0 and b_text_26_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_26_.tStart = t
            b_text_26_.frameNStart = frameN  # exact frame index
            b_text_26_.setAutoDraw(True)
        if b_text_26_.status == STARTED:  # only update if drawing
            b_text_26_.setOpacity(Tr[0], log=False)
        
        # *b_text_27_* updates
        if t >= 0.0 and b_text_27_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_27_.tStart = t
            b_text_27_.frameNStart = frameN  # exact frame index
            b_text_27_.setAutoDraw(True)
        if b_text_27_.status == STARTED:  # only update if drawing
            b_text_27_.setOpacity(Tr[1], log=False)
        
        # *b_text_28_* updates
        if t >= 0.0 and b_text_28_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_28_.tStart = t
            b_text_28_.frameNStart = frameN  # exact frame index
            b_text_28_.setAutoDraw(True)
        if b_text_28_.status == STARTED:  # only update if drawing
            b_text_28_.setOpacity(Tr[2], log=False)
        
        # *b_text_29_* updates
        if t >= 0.0 and b_text_29_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_29_.tStart = t
            b_text_29_.frameNStart = frameN  # exact frame index
            b_text_29_.setAutoDraw(True)
        if b_text_29_.status == STARTED:  # only update if drawing
            b_text_29_.setOpacity(Tr[3], log=False)
        
        # *b_text_30_* updates
        if t >= 0.0 and b_text_30_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_30_.tStart = t
            b_text_30_.frameNStart = frameN  # exact frame index
            b_text_30_.setAutoDraw(True)
        if b_text_30_.status == STARTED:  # only update if drawing
            b_text_30_.setOpacity(Tr[4], log=False)
        
        # *b_text_31_* updates
        if t >= 0.0 and b_text_31_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_31_.tStart = t
            b_text_31_.frameNStart = frameN  # exact frame index
            b_text_31_.setAutoDraw(True)
        if b_text_31_.status == STARTED:  # only update if drawing
            b_text_31_.setOpacity(Tr[5], log=False)
        
        # *b_text_32_* updates
        if t >= 0.0 and b_text_32_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_32_.tStart = t
            b_text_32_.frameNStart = frameN  # exact frame index
            b_text_32_.setAutoDraw(True)
        if b_text_32_.status == STARTED:  # only update if drawing
            b_text_32_.setOpacity(Tr[6], log=False)
        
        # *b_text_33_* updates
        if t >= 0.0 and b_text_33_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_33_.tStart = t
            b_text_33_.frameNStart = frameN  # exact frame index
            b_text_33_.setAutoDraw(True)
        if b_text_33_.status == STARTED:  # only update if drawing
            b_text_33_.setOpacity(Tr[7], log=False)
        
        # *b_text_34_* updates
        if t >= 0.0 and b_text_34_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_34_.tStart = t
            b_text_34_.frameNStart = frameN  # exact frame index
            b_text_34_.setAutoDraw(True)
        if b_text_34_.status == STARTED:  # only update if drawing
            b_text_34_.setOpacity(Tr[8], log=False)
        
        # *b_text_35_* updates
        if t >= 0.0 and b_text_35_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_35_.tStart = t
            b_text_35_.frameNStart = frameN  # exact frame index
            b_text_35_.setAutoDraw(True)
        if b_text_35_.status == STARTED:  # only update if drawing
            b_text_35_.setOpacity(Tr[9], log=False)
        
        # *b_text_36_* updates
        if t >= 0.0 and b_text_36_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_36_.tStart = t
            b_text_36_.frameNStart = frameN  # exact frame index
            b_text_36_.setAutoDraw(True)
        if b_text_36_.status == STARTED:  # only update if drawing
            b_text_36_.setOpacity(Tr[10], log=False)
        
        # *b_text_37_* updates
        if t >= 0.0 and b_text_37_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_37_.tStart = t
            b_text_37_.frameNStart = frameN  # exact frame index
            b_text_37_.setAutoDraw(True)
        if b_text_37_.status == STARTED:  # only update if drawing
            b_text_37_.setOpacity(Tr[11], log=False)
        
        # *b_text_38_* updates
        if t >= 0.0 and b_text_38_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_38_.tStart = t
            b_text_38_.frameNStart = frameN  # exact frame index
            b_text_38_.setAutoDraw(True)
        if b_text_38_.status == STARTED:  # only update if drawing
            b_text_38_.setOpacity(Tr[12], log=False)
        
        # *b_text_39_* updates
        if t >= 0.0 and b_text_39_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_39_.tStart = t
            b_text_39_.frameNStart = frameN  # exact frame index
            b_text_39_.setAutoDraw(True)
        if b_text_39_.status == STARTED:  # only update if drawing
            b_text_39_.setOpacity(Tr[13], log=False)
        
        # *b_text_40_* updates
        if t >= 0.0 and b_text_40_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_40_.tStart = t
            b_text_40_.frameNStart = frameN  # exact frame index
            b_text_40_.setAutoDraw(True)
        if b_text_40_.status == STARTED:  # only update if drawing
            b_text_40_.setOpacity(Tr[14], log=False)
        
        # *b_text_41_* updates
        if t >= 0.0 and b_text_41_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_41_.tStart = t
            b_text_41_.frameNStart = frameN  # exact frame index
            b_text_41_.setAutoDraw(True)
        if b_text_41_.status == STARTED:  # only update if drawing
            b_text_41_.setOpacity(Tr[15], log=False)
        
        # *b_text_42_* updates
        if t >= 0.0 and b_text_42_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_42_.tStart = t
            b_text_42_.frameNStart = frameN  # exact frame index
            b_text_42_.setAutoDraw(True)
        if b_text_42_.status == STARTED:  # only update if drawing
            b_text_42_.setOpacity(Tr[16], log=False)
        
        # *b_text_43_* updates
        if t >= 0.0 and b_text_43_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_43_.tStart = t
            b_text_43_.frameNStart = frameN  # exact frame index
            b_text_43_.setAutoDraw(True)
        if b_text_43_.status == STARTED:  # only update if drawing
            b_text_43_.setOpacity(Tr[17], log=False)
        
        # *b_text_44_* updates
        if t >= 0.0 and b_text_44_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_44_.tStart = t
            b_text_44_.frameNStart = frameN  # exact frame index
            b_text_44_.setAutoDraw(True)
        if b_text_44_.status == STARTED:  # only update if drawing
            b_text_44_.setOpacity(Tr[18], log=False)
        
        # *b_text_45_* updates
        if t >= 0.0 and b_text_45_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_45_.tStart = t
            b_text_45_.frameNStart = frameN  # exact frame index
            b_text_45_.setAutoDraw(True)
        if b_text_45_.status == STARTED:  # only update if drawing
            b_text_45_.setOpacity(Tr[19], log=False)
        
        # *b_text_46_* updates
        if t >= 0.0 and b_text_46_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_46_.tStart = t
            b_text_46_.frameNStart = frameN  # exact frame index
            b_text_46_.setAutoDraw(True)
        if b_text_46_.status == STARTED:  # only update if drawing
            b_text_46_.setOpacity(Tr[20], log=False)
        
        # *b_text_47_* updates
        if t >= 0.0 and b_text_47_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_47_.tStart = t
            b_text_47_.frameNStart = frameN  # exact frame index
            b_text_47_.setAutoDraw(True)
        if b_text_47_.status == STARTED:  # only update if drawing
            b_text_47_.setOpacity(Tr[21], log=False)
        
        # *b_text_48_* updates
        if t >= 0.0 and b_text_48_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_48_.tStart = t
            b_text_48_.frameNStart = frameN  # exact frame index
            b_text_48_.setAutoDraw(True)
        if b_text_48_.status == STARTED:  # only update if drawing
            b_text_48_.setOpacity(Tr[22], log=False)
        
        # *b_text_49_* updates
        if t >= 0.0 and b_text_49_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_49_.tStart = t
            b_text_49_.frameNStart = frameN  # exact frame index
            b_text_49_.setAutoDraw(True)
        if b_text_49_.status == STARTED:  # only update if drawing
            b_text_49_.setOpacity(Tr[23], log=False)
        
        # *b_text_50_* updates
        if t >= 0.0 and b_text_50_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_text_50_.tStart = t
            b_text_50_.frameNStart = frameN  # exact frame index
            b_text_50_.setAutoDraw(True)
        if b_text_50_.status == STARTED:  # only update if drawing
            b_text_50_.setOpacity(Tr[24], log=False)
        
        # *polygon_51* updates
        if t >= 0.0 and polygon_51.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_51.tStart = t
            polygon_51.frameNStart = frameN  # exact frame index
            polygon_51.setAutoDraw(True)
        if polygon_51.status == STARTED:  # only update if drawing
            polygon_51.setOpacity(Tr[25], log=False)
        
        # *polygon_52* updates
        if t >= 0.0 and polygon_52.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_52.tStart = t
            polygon_52.frameNStart = frameN  # exact frame index
            polygon_52.setAutoDraw(True)
        if polygon_52.status == STARTED:  # only update if drawing
            polygon_52.setOpacity(Tr[26], log=False)
        
        # *polygon_53* updates
        if t >= 0.0 and polygon_53.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_53.tStart = t
            polygon_53.frameNStart = frameN  # exact frame index
            polygon_53.setAutoDraw(True)
        if polygon_53.status == STARTED:  # only update if drawing
            polygon_53.setOpacity(Tr[27], log=False)
        
        # *polygon_54* updates
        if t >= 0.0 and polygon_54.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_54.tStart = t
            polygon_54.frameNStart = frameN  # exact frame index
            polygon_54.setAutoDraw(True)
        if polygon_54.status == STARTED:  # only update if drawing
            polygon_54.setOpacity(Tr[28], log=False)
        
        # *polygon_55* updates
        if t >= 0.0 and polygon_55.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_55.tStart = t
            polygon_55.frameNStart = frameN  # exact frame index
            polygon_55.setAutoDraw(True)
        if polygon_55.status == STARTED:  # only update if drawing
            polygon_55.setOpacity(Tr[29], log=False)
        
        # *polygon_56* updates
        if t >= 0.0 and polygon_56.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_56.tStart = t
            polygon_56.frameNStart = frameN  # exact frame index
            polygon_56.setAutoDraw(True)
        if polygon_56.status == STARTED:  # only update if drawing
            polygon_56.setOpacity(Tr[30], log=False)
        
        # *polygon_57* updates
        if t >= 0.0 and polygon_57.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_57.tStart = t
            polygon_57.frameNStart = frameN  # exact frame index
            polygon_57.setAutoDraw(True)
        if polygon_57.status == STARTED:  # only update if drawing
            polygon_57.setOpacity(Tr[31], log=False)
        
        # *polygon_58* updates
        if t >= 0.0 and polygon_58.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_58.tStart = t
            polygon_58.frameNStart = frameN  # exact frame index
            polygon_58.setAutoDraw(True)
        if polygon_58.status == STARTED:  # only update if drawing
            polygon_58.setOpacity(Tr[32], log=False)
        
        # *polygon_59* updates
        if t >= 0.0 and polygon_59.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_59.tStart = t
            polygon_59.frameNStart = frameN  # exact frame index
            polygon_59.setAutoDraw(True)
        if polygon_59.status == STARTED:  # only update if drawing
            polygon_59.setOpacity(Tr[33], log=False)
        
        # *polygon_60* updates
        if t >= 0.0 and polygon_60.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_60.tStart = t
            polygon_60.frameNStart = frameN  # exact frame index
            polygon_60.setAutoDraw(True)
        if polygon_60.status == STARTED:  # only update if drawing
            polygon_60.setOpacity(Tr[34], log=False)
        
        # *polygon_61* updates
        if t >= 0.0 and polygon_61.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_61.tStart = t
            polygon_61.frameNStart = frameN  # exact frame index
            polygon_61.setAutoDraw(True)
        if polygon_61.status == STARTED:  # only update if drawing
            polygon_61.setOpacity(Tr[35], log=False)
        
        # *text_51* updates
        if t >= 0.0 and text_51.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_51.tStart = t
            text_51.frameNStart = frameN  # exact frame index
            text_51.setAutoDraw(True)
        if text_51.status == STARTED:  # only update if drawing
            text_51.setOpacity(Tr[25], log=False)
        
        # *text_52* updates
        if t >= 0.0 and text_52.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_52.tStart = t
            text_52.frameNStart = frameN  # exact frame index
            text_52.setAutoDraw(True)
        if text_52.status == STARTED:  # only update if drawing
            text_52.setOpacity(Tr[26], log=False)
        
        # *text_53* updates
        if t >= 0.0 and text_53.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_53.tStart = t
            text_53.frameNStart = frameN  # exact frame index
            text_53.setAutoDraw(True)
        if text_53.status == STARTED:  # only update if drawing
            text_53.setOpacity(Tr[27], log=False)
        
        # *text_54* updates
        if t >= 0.0 and text_54.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_54.tStart = t
            text_54.frameNStart = frameN  # exact frame index
            text_54.setAutoDraw(True)
        if text_54.status == STARTED:  # only update if drawing
            text_54.setOpacity(Tr[28], log=False)
        
        # *text_55* updates
        if t >= 0.0 and text_55.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_55.tStart = t
            text_55.frameNStart = frameN  # exact frame index
            text_55.setAutoDraw(True)
        if text_55.status == STARTED:  # only update if drawing
            text_55.setOpacity(Tr[29], log=False)
        
        # *text_56* updates
        if t >= 0.0 and text_56.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_56.tStart = t
            text_56.frameNStart = frameN  # exact frame index
            text_56.setAutoDraw(True)
        if text_56.status == STARTED:  # only update if drawing
            text_56.setOpacity(Tr[30], log=False)
        
        # *text_57* updates
        if t >= 0.0 and text_57.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_57.tStart = t
            text_57.frameNStart = frameN  # exact frame index
            text_57.setAutoDraw(True)
        if text_57.status == STARTED:  # only update if drawing
            text_57.setOpacity(Tr[31], log=False)
        
        # *text_58* updates
        if t >= 0.0 and text_58.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_58.tStart = t
            text_58.frameNStart = frameN  # exact frame index
            text_58.setAutoDraw(True)
        if text_58.status == STARTED:  # only update if drawing
            text_58.setOpacity(Tr[32], log=False)
        
        # *text_59* updates
        if t >= 0.0 and text_59.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_59.tStart = t
            text_59.frameNStart = frameN  # exact frame index
            text_59.setAutoDraw(True)
        if text_59.status == STARTED:  # only update if drawing
            text_59.setOpacity(Tr[33], log=False)
        
        # *text_60* updates
        if t >= 0.0 and text_60.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_60.tStart = t
            text_60.frameNStart = frameN  # exact frame index
            text_60.setAutoDraw(True)
        if text_60.status == STARTED:  # only update if drawing
            text_60.setOpacity(Tr[34], log=False)
        
        # *text_61* updates
        if t >= 0.0 and text_61.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_61.tStart = t
            text_61.frameNStart = frameN  # exact frame index
            text_61.setAutoDraw(True)
        if text_61.status == STARTED:  # only update if drawing
            text_61.setOpacity(Tr[35], log=False)
        
        # *polygon_62* updates
        if t >= 0.0 and polygon_62.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_62.tStart = t
            polygon_62.frameNStart = frameN  # exact frame index
            polygon_62.setAutoDraw(True)
        if polygon_62.status == STARTED:  # only update if drawing
            polygon_62.setOpacity(Tr[36], log=False)
        
        # *polygon_63* updates
        if t >= 0.0 and polygon_63.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_63.tStart = t
            polygon_63.frameNStart = frameN  # exact frame index
            polygon_63.setAutoDraw(True)
        if polygon_63.status == STARTED:  # only update if drawing
            polygon_63.setOpacity(Tr[37], log=False)
        
        # *polygon_64* updates
        if t >= 0.0 and polygon_64.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_64.tStart = t
            polygon_64.frameNStart = frameN  # exact frame index
            polygon_64.setAutoDraw(True)
        if polygon_64.status == STARTED:  # only update if drawing
            polygon_64.setOpacity(Tr[38], log=False)
        
        # *polygon_65* updates
        if t >= 0.0 and polygon_65.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_65.tStart = t
            polygon_65.frameNStart = frameN  # exact frame index
            polygon_65.setAutoDraw(True)
        if polygon_65.status == STARTED:  # only update if drawing
            polygon_65.setOpacity(Tr[39], log=False)
        
        # *polygon_66* updates
        if t >= 0.0 and polygon_66.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_66.tStart = t
            polygon_66.frameNStart = frameN  # exact frame index
            polygon_66.setAutoDraw(True)
        if polygon_66.status == STARTED:  # only update if drawing
            polygon_66.setOpacity(Tr[40], log=False)
        
        # *polygon_67* updates
        if t >= 0.0 and polygon_67.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_67.tStart = t
            polygon_67.frameNStart = frameN  # exact frame index
            polygon_67.setAutoDraw(True)
        if polygon_67.status == STARTED:  # only update if drawing
            polygon_67.setOpacity(Tr[41], log=False)
        
        # *polygon_68* updates
        if t >= 0.0 and polygon_68.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_68.tStart = t
            polygon_68.frameNStart = frameN  # exact frame index
            polygon_68.setAutoDraw(True)
        if polygon_68.status == STARTED:  # only update if drawing
            polygon_68.setOpacity(Tr[42], log=False)
        
        # *polygon_69* updates
        if t >= 0.0 and polygon_69.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_69.tStart = t
            polygon_69.frameNStart = frameN  # exact frame index
            polygon_69.setAutoDraw(True)
        if polygon_69.status == STARTED:  # only update if drawing
            polygon_69.setOpacity(Tr[43], log=False)
        
        # *polygon_70* updates
        if t >= 0.0 and polygon_70.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_70.tStart = t
            polygon_70.frameNStart = frameN  # exact frame index
            polygon_70.setAutoDraw(True)
        if polygon_70.status == STARTED:  # only update if drawing
            polygon_70.setOpacity(Tr[44], log=False)
        
        # *polygon_71* updates
        if t >= 0.0 and polygon_71.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_71.tStart = t
            polygon_71.frameNStart = frameN  # exact frame index
            polygon_71.setAutoDraw(True)
        if polygon_71.status == STARTED:  # only update if drawing
            polygon_71.setOpacity(Tr[45], log=False)
        
        # *polygon_72* updates
        if t >= 0.0 and polygon_72.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_72.tStart = t
            polygon_72.frameNStart = frameN  # exact frame index
            polygon_72.setAutoDraw(True)
        if polygon_72.status == STARTED:  # only update if drawing
            polygon_72.setOpacity(Tr[46], log=False)
        
        # *polygon_73* updates
        if t >= 0.0 and polygon_73.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_73.tStart = t
            polygon_73.frameNStart = frameN  # exact frame index
            polygon_73.setAutoDraw(True)
        if polygon_73.status == STARTED:  # only update if drawing
            polygon_73.setOpacity(Tr[47], log=False)
        
        # *polygon_74* updates
        if t >= 0.0 and polygon_74.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_74.tStart = t
            polygon_74.frameNStart = frameN  # exact frame index
            polygon_74.setAutoDraw(True)
        if polygon_74.status == STARTED:  # only update if drawing
            polygon_74.setOpacity(Tr[48], log=False)
        
        # *text_62* updates
        if t >= 0.0 and text_62.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_62.tStart = t
            text_62.frameNStart = frameN  # exact frame index
            text_62.setAutoDraw(True)
        if text_62.status == STARTED:  # only update if drawing
            text_62.setOpacity(Tr[36], log=False)
        
        # *text_63* updates
        if t >= 0.0 and text_63.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_63.tStart = t
            text_63.frameNStart = frameN  # exact frame index
            text_63.setAutoDraw(True)
        if text_63.status == STARTED:  # only update if drawing
            text_63.setOpacity(Tr[37], log=False)
        
        # *text_64* updates
        if t >= 0.0 and text_64.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_64.tStart = t
            text_64.frameNStart = frameN  # exact frame index
            text_64.setAutoDraw(True)
        if text_64.status == STARTED:  # only update if drawing
            text_64.setOpacity(Tr[38], log=False)
        
        # *text_65* updates
        if t >= 0.0 and text_65.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_65.tStart = t
            text_65.frameNStart = frameN  # exact frame index
            text_65.setAutoDraw(True)
        if text_65.status == STARTED:  # only update if drawing
            text_65.setOpacity(Tr[39], log=False)
        
        # *text_66* updates
        if t >= 0.0 and text_66.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_66.tStart = t
            text_66.frameNStart = frameN  # exact frame index
            text_66.setAutoDraw(True)
        if text_66.status == STARTED:  # only update if drawing
            text_66.setOpacity(Tr[40], log=False)
        
        # *text_67* updates
        if t >= 0.0 and text_67.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_67.tStart = t
            text_67.frameNStart = frameN  # exact frame index
            text_67.setAutoDraw(True)
        if text_67.status == STARTED:  # only update if drawing
            text_67.setOpacity(Tr[41], log=False)
        
        # *text_68* updates
        if t >= 0.0 and text_68.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_68.tStart = t
            text_68.frameNStart = frameN  # exact frame index
            text_68.setAutoDraw(True)
        if text_68.status == STARTED:  # only update if drawing
            text_68.setOpacity(Tr[42], log=False)
        
        # *text_69* updates
        if t >= 0.0 and text_69.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_69.tStart = t
            text_69.frameNStart = frameN  # exact frame index
            text_69.setAutoDraw(True)
        if text_69.status == STARTED:  # only update if drawing
            text_69.setOpacity(Tr[43], log=False)
        
        # *text_70* updates
        if t >= 0.0 and text_70.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_70.tStart = t
            text_70.frameNStart = frameN  # exact frame index
            text_70.setAutoDraw(True)
        if text_70.status == STARTED:  # only update if drawing
            text_70.setOpacity(Tr[44], log=False)
        
        # *text_71* updates
        if t >= 0.0 and text_71.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_71.tStart = t
            text_71.frameNStart = frameN  # exact frame index
            text_71.setAutoDraw(True)
        if text_71.status == STARTED:  # only update if drawing
            text_71.setOpacity(Tr[45], log=False)
        
        # *text_72* updates
        if t >= 0.0 and text_72.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_72.tStart = t
            text_72.frameNStart = frameN  # exact frame index
            text_72.setAutoDraw(True)
        if text_72.status == STARTED:  # only update if drawing
            text_72.setOpacity(Tr[46], log=False)
        
        # *text_73* updates
        if t >= 0.0 and text_73.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_73.tStart = t
            text_73.frameNStart = frameN  # exact frame index
            text_73.setAutoDraw(True)
        if text_73.status == STARTED:  # only update if drawing
            text_73.setOpacity(Tr[47], log=False)
        
        # *text_74* updates
        if t >= 0.0 and text_74.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_74.tStart = t
            text_74.frameNStart = frameN  # exact frame index
            text_74.setAutoDraw(True)
        if text_74.status == STARTED:  # only update if drawing
            text_74.setOpacity(Tr[48], log=False)
        
        # *polygon_75* updates
        if t >= 0.0 and polygon_75.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_75.tStart = t
            polygon_75.frameNStart = frameN  # exact frame index
            polygon_75.setAutoDraw(True)
        if polygon_75.status == STARTED:  # only update if drawing
            polygon_75.setOpacity(Tr[49], log=False)
        
        # *polygon_76* updates
        if t >= 0.0 and polygon_76.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_76.tStart = t
            polygon_76.frameNStart = frameN  # exact frame index
            polygon_76.setAutoDraw(True)
        if polygon_76.status == STARTED:  # only update if drawing
            polygon_76.setOpacity(Tr[50], log=False)
        
        # *polygon_77* updates
        if t >= 0.0 and polygon_77.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_77.tStart = t
            polygon_77.frameNStart = frameN  # exact frame index
            polygon_77.setAutoDraw(True)
        if polygon_77.status == STARTED:  # only update if drawing
            polygon_77.setOpacity(Tr[51], log=False)
        
        # *polygon_78* updates
        if t >= 0.0 and polygon_78.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_78.tStart = t
            polygon_78.frameNStart = frameN  # exact frame index
            polygon_78.setAutoDraw(True)
        if polygon_78.status == STARTED:  # only update if drawing
            polygon_78.setOpacity(Tr[52], log=False)
        
        # *polygon_79* updates
        if t >= 0.0 and polygon_79.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_79.tStart = t
            polygon_79.frameNStart = frameN  # exact frame index
            polygon_79.setAutoDraw(True)
        if polygon_79.status == STARTED:  # only update if drawing
            polygon_79.setOpacity(Tr[53], log=False)
        
        # *polygon_80* updates
        if t >= 0.0 and polygon_80.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_80.tStart = t
            polygon_80.frameNStart = frameN  # exact frame index
            polygon_80.setAutoDraw(True)
        if polygon_80.status == STARTED:  # only update if drawing
            polygon_80.setOpacity(Tr[54], log=False)
        
        # *polygon_81* updates
        if t >= 0.0 and polygon_81.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_81.tStart = t
            polygon_81.frameNStart = frameN  # exact frame index
            polygon_81.setAutoDraw(True)
        if polygon_81.status == STARTED:  # only update if drawing
            polygon_81.setOpacity(Tr[55], log=False)
        
        # *polygon_82* updates
        if t >= 0.0 and polygon_82.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_82.tStart = t
            polygon_82.frameNStart = frameN  # exact frame index
            polygon_82.setAutoDraw(True)
        if polygon_82.status == STARTED:  # only update if drawing
            polygon_82.setOpacity(Tr[56], log=False)
        
        # *polygon_83* updates
        if t >= 0.0 and polygon_83.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_83.tStart = t
            polygon_83.frameNStart = frameN  # exact frame index
            polygon_83.setAutoDraw(True)
        if polygon_83.status == STARTED:  # only update if drawing
            polygon_83.setOpacity(Tr[57], log=False)
        
        # *polygon_84* updates
        if t >= 0.0 and polygon_84.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_84.tStart = t
            polygon_84.frameNStart = frameN  # exact frame index
            polygon_84.setAutoDraw(True)
        if polygon_84.status == STARTED:  # only update if drawing
            polygon_84.setOpacity(Tr[58], log=False)
        
        # *polygon_85* updates
        if t >= 0.0 and polygon_85.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_85.tStart = t
            polygon_85.frameNStart = frameN  # exact frame index
            polygon_85.setAutoDraw(True)
        if polygon_85.status == STARTED:  # only update if drawing
            polygon_85.setOpacity(Tr[59], log=False)
        
        # *polygon_86* updates
        if t >= 0.0 and polygon_86.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_86.tStart = t
            polygon_86.frameNStart = frameN  # exact frame index
            polygon_86.setAutoDraw(True)
        if polygon_86.status == STARTED:  # only update if drawing
            polygon_86.setOpacity(Tr[60], log=False)
        
        # *polygon_87* updates
        if t >= 0.0 and polygon_87.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_87.tStart = t
            polygon_87.frameNStart = frameN  # exact frame index
            polygon_87.setAutoDraw(True)
        if polygon_87.status == STARTED:  # only update if drawing
            polygon_87.setOpacity(Tr[61], log=False)
        
        # *polygon_88* updates
        if t >= 0.0 and polygon_88.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_88.tStart = t
            polygon_88.frameNStart = frameN  # exact frame index
            polygon_88.setAutoDraw(True)
        if polygon_88.status == STARTED:  # only update if drawing
            polygon_88.setOpacity(Tr[62], log=False)
        
        # *text_75* updates
        if t >= 0.0 and text_75.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_75.tStart = t
            text_75.frameNStart = frameN  # exact frame index
            text_75.setAutoDraw(True)
        if text_75.status == STARTED:  # only update if drawing
            text_75.setOpacity(Tr[49], log=False)
        
        # *text_76* updates
        if t >= 0.0 and text_76.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_76.tStart = t
            text_76.frameNStart = frameN  # exact frame index
            text_76.setAutoDraw(True)
        if text_76.status == STARTED:  # only update if drawing
            text_76.setOpacity(Tr[50], log=False)
        
        # *text_77* updates
        if t >= 0.0 and text_77.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_77.tStart = t
            text_77.frameNStart = frameN  # exact frame index
            text_77.setAutoDraw(True)
        if text_77.status == STARTED:  # only update if drawing
            text_77.setOpacity(Tr[51], log=False)
        
        # *text_78* updates
        if t >= 0.0 and text_78.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_78.tStart = t
            text_78.frameNStart = frameN  # exact frame index
            text_78.setAutoDraw(True)
        if text_78.status == STARTED:  # only update if drawing
            text_78.setOpacity(Tr[52], log=False)
        
        # *text_79* updates
        if t >= 0.0 and text_79.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_79.tStart = t
            text_79.frameNStart = frameN  # exact frame index
            text_79.setAutoDraw(True)
        if text_79.status == STARTED:  # only update if drawing
            text_79.setOpacity(Tr[53], log=False)
        
        # *text_80* updates
        if t >= 0.0 and text_80.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_80.tStart = t
            text_80.frameNStart = frameN  # exact frame index
            text_80.setAutoDraw(True)
        if text_80.status == STARTED:  # only update if drawing
            text_80.setOpacity(Tr[54], log=False)
        
        # *text_81* updates
        if t >= 0.0 and text_81.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_81.tStart = t
            text_81.frameNStart = frameN  # exact frame index
            text_81.setAutoDraw(True)
        if text_81.status == STARTED:  # only update if drawing
            text_81.setOpacity(Tr[55], log=False)
        
        # *text_82* updates
        if t >= 0.0 and text_82.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_82.tStart = t
            text_82.frameNStart = frameN  # exact frame index
            text_82.setAutoDraw(True)
        if text_82.status == STARTED:  # only update if drawing
            text_82.setOpacity(Tr[56], log=False)
        
        # *text_83* updates
        if t >= 0.0 and text_83.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_83.tStart = t
            text_83.frameNStart = frameN  # exact frame index
            text_83.setAutoDraw(True)
        if text_83.status == STARTED:  # only update if drawing
            text_83.setOpacity(Tr[57], log=False)
        
        # *text_84* updates
        if t >= 0.0 and text_84.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_84.tStart = t
            text_84.frameNStart = frameN  # exact frame index
            text_84.setAutoDraw(True)
        if text_84.status == STARTED:  # only update if drawing
            text_84.setOpacity(Tr[58], log=False)
        
        # *text_85* updates
        if t >= 0.0 and text_85.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_85.tStart = t
            text_85.frameNStart = frameN  # exact frame index
            text_85.setAutoDraw(True)
        if text_85.status == STARTED:  # only update if drawing
            text_85.setOpacity(Tr[59], log=False)
        
        # *text_86* updates
        if t >= 0.0 and text_86.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_86.tStart = t
            text_86.frameNStart = frameN  # exact frame index
            text_86.setAutoDraw(True)
        if text_86.status == STARTED:  # only update if drawing
            text_86.setOpacity(Tr[60], log=False)
        
        # *text_87* updates
        if t >= 0.0 and text_87.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_87.tStart = t
            text_87.frameNStart = frameN  # exact frame index
            text_87.setAutoDraw(True)
        if text_87.status == STARTED:  # only update if drawing
            text_87.setOpacity(Tr[61], log=False)
        
        # *text_88* updates
        if t >= 0.0 and text_88.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_88.tStart = t
            text_88.frameNStart = frameN  # exact frame index
            text_88.setAutoDraw(True)
        if text_88.status == STARTED:  # only update if drawing
            text_88.setOpacity(Tr[62], log=False)
        
        # *polygon_89* updates
        if t >= 0.0 and polygon_89.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_89.tStart = t
            polygon_89.frameNStart = frameN  # exact frame index
            polygon_89.setAutoDraw(True)
        if polygon_89.status == STARTED:  # only update if drawing
            polygon_89.setOpacity(Tr[63], log=False)
        
        # *polygon_90* updates
        if t >= 0.0 and polygon_90.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_90.tStart = t
            polygon_90.frameNStart = frameN  # exact frame index
            polygon_90.setAutoDraw(True)
        if polygon_90.status == STARTED:  # only update if drawing
            polygon_90.setOpacity(Tr[64], log=False)
        
        # *polygon_91* updates
        if t >= 0.0 and polygon_91.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_91.tStart = t
            polygon_91.frameNStart = frameN  # exact frame index
            polygon_91.setAutoDraw(True)
        if polygon_91.status == STARTED:  # only update if drawing
            polygon_91.setOpacity(Tr[65], log=False)
        
        # *polygon_92* updates
        if t >= 0.0 and polygon_92.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_92.tStart = t
            polygon_92.frameNStart = frameN  # exact frame index
            polygon_92.setAutoDraw(True)
        if polygon_92.status == STARTED:  # only update if drawing
            polygon_92.setOpacity(Tr[66], log=False)
        
        # *polygon_93* updates
        if t >= 0.0 and polygon_93.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_93.tStart = t
            polygon_93.frameNStart = frameN  # exact frame index
            polygon_93.setAutoDraw(True)
        if polygon_93.status == STARTED:  # only update if drawing
            polygon_93.setOpacity(Tr[67], log=False)
        
        # *polygon_94* updates
        if t >= 0.0 and polygon_94.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_94.tStart = t
            polygon_94.frameNStart = frameN  # exact frame index
            polygon_94.setAutoDraw(True)
        if polygon_94.status == STARTED:  # only update if drawing
            polygon_94.setOpacity(Tr[68], log=False)
        
        # *polygon_95* updates
        if t >= 0.0 and polygon_95.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_95.tStart = t
            polygon_95.frameNStart = frameN  # exact frame index
            polygon_95.setAutoDraw(True)
        if polygon_95.status == STARTED:  # only update if drawing
            polygon_95.setOpacity(Tr[69], log=False)
        
        # *polygon_96* updates
        if t >= 0.0 and polygon_96.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_96.tStart = t
            polygon_96.frameNStart = frameN  # exact frame index
            polygon_96.setAutoDraw(True)
        if polygon_96.status == STARTED:  # only update if drawing
            polygon_96.setOpacity(Tr[70], log=False)
        
        # *polygon_97* updates
        if t >= 0.0 and polygon_97.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_97.tStart = t
            polygon_97.frameNStart = frameN  # exact frame index
            polygon_97.setAutoDraw(True)
        if polygon_97.status == STARTED:  # only update if drawing
            polygon_97.setOpacity(Tr[71], log=False)
        
        # *polygon_98* updates
        if t >= 0.0 and polygon_98.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_98.tStart = t
            polygon_98.frameNStart = frameN  # exact frame index
            polygon_98.setAutoDraw(True)
        if polygon_98.status == STARTED:  # only update if drawing
            polygon_98.setOpacity(Tr[72], log=False)
        
        # *polygon_99* updates
        if t >= 0.0 and polygon_99.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_99.tStart = t
            polygon_99.frameNStart = frameN  # exact frame index
            polygon_99.setAutoDraw(True)
        if polygon_99.status == STARTED:  # only update if drawing
            polygon_99.setOpacity(Tr[73], log=False)
        
        # *polygon_100* updates
        if t >= 0.0 and polygon_100.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_100.tStart = t
            polygon_100.frameNStart = frameN  # exact frame index
            polygon_100.setAutoDraw(True)
        if polygon_100.status == STARTED:  # only update if drawing
            polygon_100.setOpacity(Tr[74], log=False)
        
        # *polygon_101* updates
        if t >= 0.0 and polygon_101.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_101.tStart = t
            polygon_101.frameNStart = frameN  # exact frame index
            polygon_101.setAutoDraw(True)
        if polygon_101.status == STARTED:  # only update if drawing
            polygon_101.setOpacity(Tr[75], log=False)
        
        # *polygon_102* updates
        if t >= 0.0 and polygon_102.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_102.tStart = t
            polygon_102.frameNStart = frameN  # exact frame index
            polygon_102.setAutoDraw(True)
        if polygon_102.status == STARTED:  # only update if drawing
            polygon_102.setOpacity(Tr[76], log=False)
        
        # *polygon_103* updates
        if t >= 0.0 and polygon_103.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_103.tStart = t
            polygon_103.frameNStart = frameN  # exact frame index
            polygon_103.setAutoDraw(True)
        if polygon_103.status == STARTED:  # only update if drawing
            polygon_103.setOpacity(Tr[77], log=False)
        
        # *polygon_104* updates
        if t >= 0.0 and polygon_104.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_104.tStart = t
            polygon_104.frameNStart = frameN  # exact frame index
            polygon_104.setAutoDraw(True)
        if polygon_104.status == STARTED:  # only update if drawing
            polygon_104.setOpacity(Tr[78], log=False)
        
        # *polygon_105* updates
        if t >= 0.0 and polygon_105.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_105.tStart = t
            polygon_105.frameNStart = frameN  # exact frame index
            polygon_105.setAutoDraw(True)
        if polygon_105.status == STARTED:  # only update if drawing
            polygon_105.setOpacity(Tr[79], log=False)
        
        # *polygon_106* updates
        if t >= 0.0 and polygon_106.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_106.tStart = t
            polygon_106.frameNStart = frameN  # exact frame index
            polygon_106.setAutoDraw(True)
        if polygon_106.status == STARTED:  # only update if drawing
            polygon_106.setOpacity(Tr[80], log=False)
        
        # *polygon_107* updates
        if t >= 0.0 and polygon_107.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_107.tStart = t
            polygon_107.frameNStart = frameN  # exact frame index
            polygon_107.setAutoDraw(True)
        if polygon_107.status == STARTED:  # only update if drawing
            polygon_107.setOpacity(Tr[81], log=False)
        
        # *polygon_108* updates
        if t >= 0.0 and polygon_108.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_108.tStart = t
            polygon_108.frameNStart = frameN  # exact frame index
            polygon_108.setAutoDraw(True)
        if polygon_108.status == STARTED:  # only update if drawing
            polygon_108.setOpacity(Tr[82], log=False)
        
        # *polygon_109* updates
        if t >= 0.0 and polygon_109.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_109.tStart = t
            polygon_109.frameNStart = frameN  # exact frame index
            polygon_109.setAutoDraw(True)
        if polygon_109.status == STARTED:  # only update if drawing
            polygon_109.setOpacity(Tr[83], log=False)
        
        # *polygon_110* updates
        if t >= 0.0 and polygon_110.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_110.tStart = t
            polygon_110.frameNStart = frameN  # exact frame index
            polygon_110.setAutoDraw(True)
        if polygon_110.status == STARTED:  # only update if drawing
            polygon_110.setOpacity(Tr[84], log=False)
        
        # *polygon_111* updates
        if t >= 0.0 and polygon_111.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_111.tStart = t
            polygon_111.frameNStart = frameN  # exact frame index
            polygon_111.setAutoDraw(True)
        if polygon_111.status == STARTED:  # only update if drawing
            polygon_111.setOpacity(Tr[85], log=False)
        
        # *polygon_112* updates
        if t >= 0.0 and polygon_112.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_112.tStart = t
            polygon_112.frameNStart = frameN  # exact frame index
            polygon_112.setAutoDraw(True)
        if polygon_112.status == STARTED:  # only update if drawing
            polygon_112.setOpacity(Tr[86], log=False)
        
        # *polygon_113* updates
        if t >= 0.0 and polygon_113.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_113.tStart = t
            polygon_113.frameNStart = frameN  # exact frame index
            polygon_113.setAutoDraw(True)
        if polygon_113.status == STARTED:  # only update if drawing
            polygon_113.setOpacity(Tr[87], log=False)
        
        # *polygon_114* updates
        if t >= 0.0 and polygon_114.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_114.tStart = t
            polygon_114.frameNStart = frameN  # exact frame index
            polygon_114.setAutoDraw(True)
        if polygon_114.status == STARTED:  # only update if drawing
            polygon_114.setOpacity(Tr[88], log=False)
        
        # *polygon_115* updates
        if t >= 0.0 and polygon_115.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_115.tStart = t
            polygon_115.frameNStart = frameN  # exact frame index
            polygon_115.setAutoDraw(True)
        if polygon_115.status == STARTED:  # only update if drawing
            polygon_115.setOpacity(Tr[89], log=False)
        
        # *polygon_116* updates
        if t >= 0.0 and polygon_116.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_116.tStart = t
            polygon_116.frameNStart = frameN  # exact frame index
            polygon_116.setAutoDraw(True)
        if polygon_116.status == STARTED:  # only update if drawing
            polygon_116.setOpacity(Tr[90], log=False)
        
        # *text_89* updates
        if t >= 0.0 and text_89.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_89.tStart = t
            text_89.frameNStart = frameN  # exact frame index
            text_89.setAutoDraw(True)
        if text_89.status == STARTED:  # only update if drawing
            text_89.setOpacity(Tr[63], log=False)
        
        # *text_90* updates
        if t >= 0.0 and text_90.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_90.tStart = t
            text_90.frameNStart = frameN  # exact frame index
            text_90.setAutoDraw(True)
        if text_90.status == STARTED:  # only update if drawing
            text_90.setOpacity(Tr[64], log=False)
        
        # *text_91* updates
        if t >= 0.0 and text_91.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_91.tStart = t
            text_91.frameNStart = frameN  # exact frame index
            text_91.setAutoDraw(True)
        if text_91.status == STARTED:  # only update if drawing
            text_91.setOpacity(Tr[65], log=False)
        
        # *text_92* updates
        if t >= 0.0 and text_92.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_92.tStart = t
            text_92.frameNStart = frameN  # exact frame index
            text_92.setAutoDraw(True)
        if text_92.status == STARTED:  # only update if drawing
            text_92.setOpacity(Tr[66], log=False)
        
        # *text_93* updates
        if t >= 0.0 and text_93.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_93.tStart = t
            text_93.frameNStart = frameN  # exact frame index
            text_93.setAutoDraw(True)
        if text_93.status == STARTED:  # only update if drawing
            text_93.setOpacity(Tr[67], log=False)
        
        # *text_94* updates
        if t >= 0.0 and text_94.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_94.tStart = t
            text_94.frameNStart = frameN  # exact frame index
            text_94.setAutoDraw(True)
        if text_94.status == STARTED:  # only update if drawing
            text_94.setOpacity(Tr[68], log=False)
        
        # *text_95* updates
        if t >= 0.0 and text_95.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_95.tStart = t
            text_95.frameNStart = frameN  # exact frame index
            text_95.setAutoDraw(True)
        if text_95.status == STARTED:  # only update if drawing
            text_95.setOpacity(Tr[69], log=False)
        
        # *text_96* updates
        if t >= 0.0 and text_96.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_96.tStart = t
            text_96.frameNStart = frameN  # exact frame index
            text_96.setAutoDraw(True)
        if text_96.status == STARTED:  # only update if drawing
            text_96.setOpacity(Tr[70], log=False)
        
        # *text_97* updates
        if t >= 0.0 and text_97.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_97.tStart = t
            text_97.frameNStart = frameN  # exact frame index
            text_97.setAutoDraw(True)
        if text_97.status == STARTED:  # only update if drawing
            text_97.setOpacity(Tr[71], log=False)
        
        # *text_98* updates
        if t >= 0.0 and text_98.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_98.tStart = t
            text_98.frameNStart = frameN  # exact frame index
            text_98.setAutoDraw(True)
        if text_98.status == STARTED:  # only update if drawing
            text_98.setOpacity(Tr[72], log=False)
        
        # *text_99* updates
        if t >= 0.0 and text_99.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_99.tStart = t
            text_99.frameNStart = frameN  # exact frame index
            text_99.setAutoDraw(True)
        if text_99.status == STARTED:  # only update if drawing
            text_99.setOpacity(Tr[73], log=False)
        
        # *text_100* updates
        if t >= 0.0 and text_100.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_100.tStart = t
            text_100.frameNStart = frameN  # exact frame index
            text_100.setAutoDraw(True)
        if text_100.status == STARTED:  # only update if drawing
            text_100.setOpacity(Tr[74], log=False)
        
        # *text_101* updates
        if t >= 0.0 and text_101.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_101.tStart = t
            text_101.frameNStart = frameN  # exact frame index
            text_101.setAutoDraw(True)
        if text_101.status == STARTED:  # only update if drawing
            text_101.setOpacity(Tr[75], log=False)
        
        # *text_102* updates
        if t >= 0.0 and text_102.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_102.tStart = t
            text_102.frameNStart = frameN  # exact frame index
            text_102.setAutoDraw(True)
        if text_102.status == STARTED:  # only update if drawing
            text_102.setOpacity(Tr[76], log=False)
        
        # *text_103* updates
        if t >= 0.0 and text_103.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_103.tStart = t
            text_103.frameNStart = frameN  # exact frame index
            text_103.setAutoDraw(True)
        if text_103.status == STARTED:  # only update if drawing
            text_103.setOpacity(Tr[77], log=False)
        
        # *text_104* updates
        if t >= 0.0 and text_104.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_104.tStart = t
            text_104.frameNStart = frameN  # exact frame index
            text_104.setAutoDraw(True)
        if text_104.status == STARTED:  # only update if drawing
            text_104.setOpacity(Tr[78], log=False)
        
        # *text_105* updates
        if t >= 0.0 and text_105.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_105.tStart = t
            text_105.frameNStart = frameN  # exact frame index
            text_105.setAutoDraw(True)
        if text_105.status == STARTED:  # only update if drawing
            text_105.setOpacity(Tr[79], log=False)
        
        # *text_106* updates
        if t >= 0.0 and text_106.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_106.tStart = t
            text_106.frameNStart = frameN  # exact frame index
            text_106.setAutoDraw(True)
        if text_106.status == STARTED:  # only update if drawing
            text_106.setOpacity(Tr[80], log=False)
        
        # *text_107* updates
        if t >= 0.0 and text_107.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_107.tStart = t
            text_107.frameNStart = frameN  # exact frame index
            text_107.setAutoDraw(True)
        if text_107.status == STARTED:  # only update if drawing
            text_107.setOpacity(Tr[81], log=False)
        
        # *text_108* updates
        if t >= 0.0 and text_108.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_108.tStart = t
            text_108.frameNStart = frameN  # exact frame index
            text_108.setAutoDraw(True)
        if text_108.status == STARTED:  # only update if drawing
            text_108.setOpacity(Tr[82], log=False)
        
        # *text_109* updates
        if t >= 0.0 and text_109.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_109.tStart = t
            text_109.frameNStart = frameN  # exact frame index
            text_109.setAutoDraw(True)
        if text_109.status == STARTED:  # only update if drawing
            text_109.setOpacity(Tr[83], log=False)
        
        # *text_110* updates
        if t >= 0.0 and text_110.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_110.tStart = t
            text_110.frameNStart = frameN  # exact frame index
            text_110.setAutoDraw(True)
        if text_110.status == STARTED:  # only update if drawing
            text_110.setOpacity(Tr[84], log=False)
        
        # *text_111* updates
        if t >= 0.0 and text_111.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_111.tStart = t
            text_111.frameNStart = frameN  # exact frame index
            text_111.setAutoDraw(True)
        if text_111.status == STARTED:  # only update if drawing
            text_111.setOpacity(Tr[85], log=False)
        
        # *text_112* updates
        if t >= 0.0 and text_112.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_112.tStart = t
            text_112.frameNStart = frameN  # exact frame index
            text_112.setAutoDraw(True)
        if text_112.status == STARTED:  # only update if drawing
            text_112.setOpacity(Tr[86], log=False)
        
        # *text_113* updates
        if t >= 0.0 and text_113.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_113.tStart = t
            text_113.frameNStart = frameN  # exact frame index
            text_113.setAutoDraw(True)
        if text_113.status == STARTED:  # only update if drawing
            text_113.setOpacity(Tr[87], log=False)
        
        # *text_114* updates
        if t >= 0.0 and text_114.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_114.tStart = t
            text_114.frameNStart = frameN  # exact frame index
            text_114.setAutoDraw(True)
        if text_114.status == STARTED:  # only update if drawing
            text_114.setOpacity(Tr[88], log=False)
        
        # *text_115* updates
        if t >= 0.0 and text_115.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_115.tStart = t
            text_115.frameNStart = frameN  # exact frame index
            text_115.setAutoDraw(True)
        if text_115.status == STARTED:  # only update if drawing
            text_115.setOpacity(Tr[89], log=False)
        
        # *text_116* updates
        if t >= 0.0 and text_116.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_116.tStart = t
            text_116.frameNStart = frameN  # exact frame index
            text_116.setAutoDraw(True)
        if text_116.status == STARTED:  # only update if drawing
            text_116.setOpacity(Tr[90], log=False)
        
        # *polygon_117* updates
        if t >= 0.0 and polygon_117.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_117.tStart = t
            polygon_117.frameNStart = frameN  # exact frame index
            polygon_117.setAutoDraw(True)
        if polygon_117.status == STARTED:  # only update if drawing
            polygon_117.setOpacity(Tr[91], log=False)
        
        # *polygon_118* updates
        if t >= 0.0 and polygon_118.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_118.tStart = t
            polygon_118.frameNStart = frameN  # exact frame index
            polygon_118.setAutoDraw(True)
        if polygon_118.status == STARTED:  # only update if drawing
            polygon_118.setOpacity(Tr[92], log=False)
        
        # *polygon_119* updates
        if t >= 0.0 and polygon_119.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_119.tStart = t
            polygon_119.frameNStart = frameN  # exact frame index
            polygon_119.setAutoDraw(True)
        if polygon_119.status == STARTED:  # only update if drawing
            polygon_119.setOpacity(Tr[93], log=False)
        
        # *polygon_120* updates
        if t >= 0.0 and polygon_120.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_120.tStart = t
            polygon_120.frameNStart = frameN  # exact frame index
            polygon_120.setAutoDraw(True)
        if polygon_120.status == STARTED:  # only update if drawing
            polygon_120.setOpacity(Tr[94], log=False)
        
        # *polygon_121* updates
        if t >= 0.0 and polygon_121.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_121.tStart = t
            polygon_121.frameNStart = frameN  # exact frame index
            polygon_121.setAutoDraw(True)
        if polygon_121.status == STARTED:  # only update if drawing
            polygon_121.setOpacity(Tr[95], log=False)
        
        # *polygon_122* updates
        if t >= 0.0 and polygon_122.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_122.tStart = t
            polygon_122.frameNStart = frameN  # exact frame index
            polygon_122.setAutoDraw(True)
        if polygon_122.status == STARTED:  # only update if drawing
            polygon_122.setOpacity(Tr[96], log=False)
        
        # *polygon_123* updates
        if t >= 0.0 and polygon_123.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_123.tStart = t
            polygon_123.frameNStart = frameN  # exact frame index
            polygon_123.setAutoDraw(True)
        if polygon_123.status == STARTED:  # only update if drawing
            polygon_123.setOpacity(Tr[97], log=False)
        
        # *polygon_124* updates
        if t >= 0.0 and polygon_124.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_124.tStart = t
            polygon_124.frameNStart = frameN  # exact frame index
            polygon_124.setAutoDraw(True)
        if polygon_124.status == STARTED:  # only update if drawing
            polygon_124.setOpacity(Tr[98], log=False)
        
        # *polygon_125* updates
        if t >= 0.0 and polygon_125.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_125.tStart = t
            polygon_125.frameNStart = frameN  # exact frame index
            polygon_125.setAutoDraw(True)
        if polygon_125.status == STARTED:  # only update if drawing
            polygon_125.setOpacity(Tr[99], log=False)
        
        # *polygon_126* updates
        if t >= 0.0 and polygon_126.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_126.tStart = t
            polygon_126.frameNStart = frameN  # exact frame index
            polygon_126.setAutoDraw(True)
        if polygon_126.status == STARTED:  # only update if drawing
            polygon_126.setOpacity(Tr[100], log=False)
        
        # *polygon_127* updates
        if t >= 0.0 and polygon_127.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_127.tStart = t
            polygon_127.frameNStart = frameN  # exact frame index
            polygon_127.setAutoDraw(True)
        if polygon_127.status == STARTED:  # only update if drawing
            polygon_127.setOpacity(Tr[101], log=False)
        
        # *polygon_128* updates
        if t >= 0.0 and polygon_128.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_128.tStart = t
            polygon_128.frameNStart = frameN  # exact frame index
            polygon_128.setAutoDraw(True)
        if polygon_128.status == STARTED:  # only update if drawing
            polygon_128.setOpacity(Tr[102], log=False)
        
        # *polygon_129* updates
        if t >= 0.0 and polygon_129.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_129.tStart = t
            polygon_129.frameNStart = frameN  # exact frame index
            polygon_129.setAutoDraw(True)
        if polygon_129.status == STARTED:  # only update if drawing
            polygon_129.setOpacity(Tr[103], log=False)
        
        # *polygon_130* updates
        if t >= 0.0 and polygon_130.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_130.tStart = t
            polygon_130.frameNStart = frameN  # exact frame index
            polygon_130.setAutoDraw(True)
        if polygon_130.status == STARTED:  # only update if drawing
            polygon_130.setOpacity(Tr[104], log=False)
        
        # *polygon_131* updates
        if t >= 0.0 and polygon_131.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_131.tStart = t
            polygon_131.frameNStart = frameN  # exact frame index
            polygon_131.setAutoDraw(True)
        if polygon_131.status == STARTED:  # only update if drawing
            polygon_131.setOpacity(Tr[105], log=False)
        
        # *polygon_132* updates
        if t >= 0.0 and polygon_132.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_132.tStart = t
            polygon_132.frameNStart = frameN  # exact frame index
            polygon_132.setAutoDraw(True)
        if polygon_132.status == STARTED:  # only update if drawing
            polygon_132.setOpacity(Tr[106], log=False)
        
        # *polygon_133* updates
        if t >= 0.0 and polygon_133.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_133.tStart = t
            polygon_133.frameNStart = frameN  # exact frame index
            polygon_133.setAutoDraw(True)
        if polygon_133.status == STARTED:  # only update if drawing
            polygon_133.setOpacity(Tr[107], log=False)
        
        # *polygon_134* updates
        if t >= 0.0 and polygon_134.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_134.tStart = t
            polygon_134.frameNStart = frameN  # exact frame index
            polygon_134.setAutoDraw(True)
        if polygon_134.status == STARTED:  # only update if drawing
            polygon_134.setOpacity(Tr[108], log=False)
        
        # *polygon_135* updates
        if t >= 0.0 and polygon_135.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_135.tStart = t
            polygon_135.frameNStart = frameN  # exact frame index
            polygon_135.setAutoDraw(True)
        if polygon_135.status == STARTED:  # only update if drawing
            polygon_135.setOpacity(Tr[109], log=False)
        
        # *polygon_136* updates
        if t >= 0.0 and polygon_136.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_136.tStart = t
            polygon_136.frameNStart = frameN  # exact frame index
            polygon_136.setAutoDraw(True)
        if polygon_136.status == STARTED:  # only update if drawing
            polygon_136.setOpacity(Tr[110], log=False)
        
        # *polygon_137* updates
        if t >= 0.0 and polygon_137.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_137.tStart = t
            polygon_137.frameNStart = frameN  # exact frame index
            polygon_137.setAutoDraw(True)
        if polygon_137.status == STARTED:  # only update if drawing
            polygon_137.setOpacity(Tr[111], log=False)
        
        # *polygon_138* updates
        if t >= 0.0 and polygon_138.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_138.tStart = t
            polygon_138.frameNStart = frameN  # exact frame index
            polygon_138.setAutoDraw(True)
        if polygon_138.status == STARTED:  # only update if drawing
            polygon_138.setOpacity(Tr[112], log=False)
        
        # *polygon_139* updates
        if t >= 0.0 and polygon_139.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_139.tStart = t
            polygon_139.frameNStart = frameN  # exact frame index
            polygon_139.setAutoDraw(True)
        if polygon_139.status == STARTED:  # only update if drawing
            polygon_139.setOpacity(Tr[113], log=False)
        
        # *polygon_140* updates
        if t >= 0.0 and polygon_140.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_140.tStart = t
            polygon_140.frameNStart = frameN  # exact frame index
            polygon_140.setAutoDraw(True)
        if polygon_140.status == STARTED:  # only update if drawing
            polygon_140.setOpacity(Tr[114], log=False)
        
        # *polygon_141* updates
        if t >= 0.0 and polygon_141.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_141.tStart = t
            polygon_141.frameNStart = frameN  # exact frame index
            polygon_141.setAutoDraw(True)
        if polygon_141.status == STARTED:  # only update if drawing
            polygon_141.setOpacity(Tr[115], log=False)
        
        # *polygon_142* updates
        if t >= 0.0 and polygon_142.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_142.tStart = t
            polygon_142.frameNStart = frameN  # exact frame index
            polygon_142.setAutoDraw(True)
        if polygon_142.status == STARTED:  # only update if drawing
            polygon_142.setOpacity(Tr[116], log=False)
        
        # *text_117* updates
        if t >= 0.0 and text_117.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_117.tStart = t
            text_117.frameNStart = frameN  # exact frame index
            text_117.setAutoDraw(True)
        if text_117.status == STARTED:  # only update if drawing
            text_117.setOpacity(Tr[91], log=False)
        
        # *text_118* updates
        if t >= 0.0 and text_118.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_118.tStart = t
            text_118.frameNStart = frameN  # exact frame index
            text_118.setAutoDraw(True)
        if text_118.status == STARTED:  # only update if drawing
            text_118.setOpacity(Tr[92], log=False)
        
        # *text_119* updates
        if t >= 0.0 and text_119.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_119.tStart = t
            text_119.frameNStart = frameN  # exact frame index
            text_119.setAutoDraw(True)
        if text_119.status == STARTED:  # only update if drawing
            text_119.setOpacity(Tr[93], log=False)
        
        # *text_120* updates
        if t >= 0.0 and text_120.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_120.tStart = t
            text_120.frameNStart = frameN  # exact frame index
            text_120.setAutoDraw(True)
        if text_120.status == STARTED:  # only update if drawing
            text_120.setOpacity(Tr[94], log=False)
        
        # *text_121* updates
        if t >= 0.0 and text_121.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_121.tStart = t
            text_121.frameNStart = frameN  # exact frame index
            text_121.setAutoDraw(True)
        if text_121.status == STARTED:  # only update if drawing
            text_121.setOpacity(Tr[95], log=False)
        
        # *text_122* updates
        if t >= 0.0 and text_122.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_122.tStart = t
            text_122.frameNStart = frameN  # exact frame index
            text_122.setAutoDraw(True)
        if text_122.status == STARTED:  # only update if drawing
            text_122.setOpacity(Tr[96], log=False)
        
        # *text_123* updates
        if t >= 0.0 and text_123.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_123.tStart = t
            text_123.frameNStart = frameN  # exact frame index
            text_123.setAutoDraw(True)
        if text_123.status == STARTED:  # only update if drawing
            text_123.setOpacity(Tr[97], log=False)
        
        # *text_124* updates
        if t >= 0.0 and text_124.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_124.tStart = t
            text_124.frameNStart = frameN  # exact frame index
            text_124.setAutoDraw(True)
        if text_124.status == STARTED:  # only update if drawing
            text_124.setOpacity(Tr[98], log=False)
        
        # *text_125* updates
        if t >= 0.0 and text_125.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_125.tStart = t
            text_125.frameNStart = frameN  # exact frame index
            text_125.setAutoDraw(True)
        if text_125.status == STARTED:  # only update if drawing
            text_125.setOpacity(Tr[99], log=False)
        
        # *text_126* updates
        if t >= 0.0 and text_126.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_126.tStart = t
            text_126.frameNStart = frameN  # exact frame index
            text_126.setAutoDraw(True)
        if text_126.status == STARTED:  # only update if drawing
            text_126.setOpacity(Tr[100], log=False)
        
        # *text_127* updates
        if t >= 0.0 and text_127.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_127.tStart = t
            text_127.frameNStart = frameN  # exact frame index
            text_127.setAutoDraw(True)
        if text_127.status == STARTED:  # only update if drawing
            text_127.setOpacity(Tr[101], log=False)
        
        # *text_128* updates
        if t >= 0.0 and text_128.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_128.tStart = t
            text_128.frameNStart = frameN  # exact frame index
            text_128.setAutoDraw(True)
        if text_128.status == STARTED:  # only update if drawing
            text_128.setOpacity(Tr[102], log=False)
        
        # *text_129* updates
        if t >= 0.0 and text_129.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_129.tStart = t
            text_129.frameNStart = frameN  # exact frame index
            text_129.setAutoDraw(True)
        if text_129.status == STARTED:  # only update if drawing
            text_129.setOpacity(Tr[103], log=False)
        
        # *text_130* updates
        if t >= 0.0 and text_130.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_130.tStart = t
            text_130.frameNStart = frameN  # exact frame index
            text_130.setAutoDraw(True)
        if text_130.status == STARTED:  # only update if drawing
            text_130.setOpacity(Tr[104], log=False)
        
        # *text_131* updates
        if t >= 0.0 and text_131.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_131.tStart = t
            text_131.frameNStart = frameN  # exact frame index
            text_131.setAutoDraw(True)
        if text_131.status == STARTED:  # only update if drawing
            text_131.setOpacity(Tr[105], log=False)
        
        # *text_132* updates
        if t >= 0.0 and text_132.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_132.tStart = t
            text_132.frameNStart = frameN  # exact frame index
            text_132.setAutoDraw(True)
        if text_132.status == STARTED:  # only update if drawing
            text_132.setOpacity(Tr[106], log=False)
        
        # *text_133* updates
        if t >= 0.0 and text_133.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_133.tStart = t
            text_133.frameNStart = frameN  # exact frame index
            text_133.setAutoDraw(True)
        if text_133.status == STARTED:  # only update if drawing
            text_133.setOpacity(Tr[107], log=False)
        
        # *text_134* updates
        if t >= 0.0 and text_134.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_134.tStart = t
            text_134.frameNStart = frameN  # exact frame index
            text_134.setAutoDraw(True)
        if text_134.status == STARTED:  # only update if drawing
            text_134.setOpacity(Tr[108], log=False)
        
        # *text_135* updates
        if t >= 0.0 and text_135.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_135.tStart = t
            text_135.frameNStart = frameN  # exact frame index
            text_135.setAutoDraw(True)
        if text_135.status == STARTED:  # only update if drawing
            text_135.setOpacity(Tr[109], log=False)
        
        # *text_136* updates
        if t >= 0.0 and text_136.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_136.tStart = t
            text_136.frameNStart = frameN  # exact frame index
            text_136.setAutoDraw(True)
        if text_136.status == STARTED:  # only update if drawing
            text_136.setOpacity(Tr[110], log=False)
        
        # *text_137* updates
        if t >= 0.0 and text_137.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_137.tStart = t
            text_137.frameNStart = frameN  # exact frame index
            text_137.setAutoDraw(True)
        if text_137.status == STARTED:  # only update if drawing
            text_137.setOpacity(Tr[111], log=False)
        
        # *text_138* updates
        if t >= 0.0 and text_138.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_138.tStart = t
            text_138.frameNStart = frameN  # exact frame index
            text_138.setAutoDraw(True)
        if text_138.status == STARTED:  # only update if drawing
            text_138.setOpacity(Tr[112], log=False)
        
        # *text_139* updates
        if t >= 0.0 and text_139.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_139.tStart = t
            text_139.frameNStart = frameN  # exact frame index
            text_139.setAutoDraw(True)
        if text_139.status == STARTED:  # only update if drawing
            text_139.setOpacity(Tr[113], log=False)
        
        # *text_140* updates
        if t >= 0.0 and text_140.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_140.tStart = t
            text_140.frameNStart = frameN  # exact frame index
            text_140.setAutoDraw(True)
        if text_140.status == STARTED:  # only update if drawing
            text_140.setOpacity(Tr[114], log=False)
        
        # *text_141* updates
        if t >= 0.0 and text_141.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_141.tStart = t
            text_141.frameNStart = frameN  # exact frame index
            text_141.setAutoDraw(True)
        if text_141.status == STARTED:  # only update if drawing
            text_141.setOpacity(Tr[115], log=False)
        
        # *text_142* updates
        if t >= 0.0 and text_142.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_142.tStart = t
            text_142.frameNStart = frameN  # exact frame index
            text_142.setAutoDraw(True)
        if text_142.status == STARTED:  # only update if drawing
            text_142.setOpacity(Tr[116], log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_9_13Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_9_13"-------
    for thisComponent in routine_9_13Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('target', target)
    
    trials.addData('number', number_touch)
    trials.addData('time', number_time)
    trials.addData('click_miss', click_miss_list)
    
    # the Routine "routine_9_13" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
