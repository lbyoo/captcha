#!/usr/bin/env python
import os
from PIL import Image,ImageDraw
import difflib

nums = ['1111100000000010000010000000100000001000000100000001000000010000010000000001111100000000000000000000', #0,
        '10000001000000100000001000000111111111000000000000001000000000000001000000000000000000000000000000000',   #1
        '100000011000000100000101000000100001001000000100010001000000011100001000000000000000000000000000000000',  #2
        '100000000100000100010001000000100010001000000100101001000000011000110000000000000000000000000000000000',  #3
        '11000000000000101000000000001001000000000010001000000000111111111000000000001000000000000000000000', #4
        '111100001000000100100001000000100100001000000100010010000000100001100000000000000000000000000000000000', #5
        '1111100000000010010010000000100100001000000100100001000100100010010000000100001100000000000000000000', #6
        '100000000000000100000011000000100001100000000100110000000000101000000000000110000000000000000000000000', #7
        '11001110000000100110001000000100010001000000100010001000000100110001000000011001110000000000000000000',   #8
        '1100001000000010010001000000100001001000000100001001000000010010010000000001111100000000000000000000',#9
        ]

def identifyNum(s):
    r = []
    for i in range(len(nums)):
        seq = difflib.SequenceMatcher(None, s, nums[i])  
        r.append(seq.ratio())
    # print r
    return str(r.index(max(r)))
  


def dealImg(f):
    im = Image.open("img/%s"%f)
    w,h = im.size

    start = False
    code = ""
    startx = 0
    icode = ""
    for i in range(0,w):
        for j in range(0,h):
            r,g,b = im.getpixel((i,j))
            # print (r,g,b),
            m = lambda x: 0 if x[0] >= 100 and x[1] >= 100 and x[2] >= 100 else 1
            # m = lambda x: (255,255,255) if x[0] >= 100 and x[1] >= 100 and x[2] >= 100 else (0,0,0)
            # draw.point((i,j),fill = (m((r,g,b))))
            if m((r,g,b)) and not start:
                start = True
                startx = i
            
            if start and i < startx + 7:
                code += str(m((r,g,b)))

            if i >= startx + 7:
                startx = 9999
                icode += identifyNum(code)
                code = ""
                start = False

    return icode
    


    # im.resize((500,150)).show()
    # om.resize((500,150)).show()
    # for i in range(0,w):
    #     for j in (range(0,h)):
    #         if lambda x:1 x[0] > 0 (om.getpixel((i,j))) > 0
for f in os.listdir("img"):
    print f,
    print dealImg(f),
    print 

# dealImg("0094.png")
