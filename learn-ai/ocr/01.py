# -*- coding: utf-8 -*-
# import pytesserocr
from PIL import Image
import pytesseract

def handle_text(img_path, lang='eng'):
    img = Image.open(img_path)
    # img = _fix_img(img)
    text = pytesseract.image_to_string(img,lang=lang)  # 设置为中文文字的识别
    print(text)

def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img

def _fix_img(img):
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            data = (img.getpixel((i,j)))
            if (data[0]>=10 and data[1]>=10 and data[2]>=10):  # 黑色rgb为（0，0，0）
                img.putpixel((i,j),(255,255,255,255))
    return img

def handle_image(img_path):
    # image = Image.open('./assets/02.png')
    image = Image.open(img_path)
    img = image.convert('L')
    # 把图片变成二值图像。
    img1=binarizing(img,190)
    # img2=depoint(img1)
    img1.show()
    code = pytesseract.image_to_string(img1, lang='eng')
    print("识别该验证码是:" + str(code))

# handle_image('./assets/04.png')
handle_text('./assets/01.png', 'chi_sim')
