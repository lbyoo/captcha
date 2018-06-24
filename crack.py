#!/usr/bin/env python
import os
from PIL import Image,ImageDraw
import difflib
import json

nums = json.loads(open("data.txt").read())
def identifyNum(s):
    r = []
    for a,b in nums:
        seq = difflib.SequenceMatcher(None, s, b)  
        r.append((seq.ratio(),a))
    # print max(r)
    return max(r)[1]
  


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
    
def train():
    data = []
    for f in os.listdir("img"):
        numbs = os.path.splitext(f)[0]
        n = 0
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
                    # print "%s,%s" %(numbs[n],code)
                    data.append((numbs[n],code))
                    n += 1
                    code = ""
                    start = False

    with open("data.txt","w") as f:
        f.write(json.dumps(data))


# 识别过程
for f in os.listdir("img"):
    print dealImg(f)    

# 将需要训练的图片按照内容命名，然后执行train函数
# train()

 