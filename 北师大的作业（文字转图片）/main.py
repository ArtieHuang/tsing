from _csv import reader

import numpy as np
from PIL import Image, ImageFont, ImageDraw
import os

def CreateImg(text, max_len,i):
    fontSize = 30
    liens = text.split('\n')
  #  lines = text.count('\n')
    # 画布颜色
    im = Image.new("RGB", ((fontSize * max_len), len(liens) * (fontSize + 5)), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    # 字体样式
    fontPath = os.path.join("/System/Library/Fonts", "Hiragino Sans GB.ttc")

    font = ImageFont.truetype(fontPath, fontSize)
    # 文字颜色
    dr.text((0, 0), text, font=font, fill="#000000")
    im.save(str(i)+'.png')


LINE_CHAR_COUNT = 30*2  # 每行字符数：30个中文字符(=60英文字符)
CHAR_SIZE = 30
TABLE_WIDTH = 4
def line_break(line):
    ret = ''
    width = 0
    count =1

    for c in line:
        if c=='\'':
            c=''
        if c== '[' and count<2:
            c='(1) '
            count+=1
        if c==' ' and count<5:
            width=0
            c='\n('+str(count)+') '
            count+=1
        if  c==']':
            c=''
        if len(c.encode('utf8')) == 3:  # 中文
            if LINE_CHAR_COUNT == width + 1:  # 剩余位置不够一个汉字
                width = 2
                ret += '\n' + c
            else: # 中文宽度加2，注意换行边界
                width += 2
                ret += c
        else:
            if c == '\t':
                space_c = TABLE_WIDTH - width % TABLE_WIDTH  # 已有长度对TABLE_WIDTH取余
                ret += ' ' * space_c
                width += space_c
            elif c == '\n':
                width = 0
                ret += c
            else:
                width += 1
                ret += c
        if width >= LINE_CHAR_COUNT:
            ret += '\n'
            width = 0
    if ret.endswith('\n'):
        return ret
    return ret + '\n'


# with open('word.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
# with open('word.txt', 'r', encoding='utf-8') as f:
#     text_temp = f.readlines()

filename="副本A.csv"

with open(filename, 'rt', encoding='UTF-8') as raw_data:
    readers = reader(raw_data, delimiter=',')
    x = list(readers)
    data = np.array(x)
    # print(data)
    # print(data.shape)
    # print(data[:,2])
    # print(data[:,3])
    timu1=data[:,6][:,np.newaxis]
    timu2=data[:,7][:,np.newaxis]
    timu3=data[:,8][:,np.newaxis]
    timu4=data[:,9][:,np.newaxis]
    # print(timu3)

    timu= np.hstack((timu1, timu2,timu3,timu4))

    #print(timu)
    # timu=[]
    # for k in range(5193):
    #     timu[k]="".join(timu1(k))+"        ".join(timu2(k))+"\n".join(timu3(k))+"\n".join(timu4(k))


#text_temp="1.61该同学立定跳远的成绩该同学表现最好项目的成绩7.82该同学实心球的成绩该同学表现最好项目的成绩1.47该同学立定跳远的成绩该同学表现最差项目的成绩6.32该同学实心球的成绩该同学表现最差项目的成绩10.1该同学50米跑的成绩该同学表现最差项目的成绩8.5该同学50米跑的成绩该同学表现最好项目的成绩"
max_len =33
# for i, s in enumerate(timu1):
#     if len(s) > max_len:
#         max_len = len(s)
print(max_len)
i=0
for text in timu:
    i=i+1
    #print(text)
    output_str = line_break(str(text))
    CreateImg(output_str, max_len,i)
    print(i)
    print(output_str)