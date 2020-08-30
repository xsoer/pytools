import requests
from PIL import Image
import pytesseract
# from io import BytesIO
import time

#headers = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#captcha_url = 'http://www.moguproxy.com/proxy/validateCode/createCode?time={} '.format(int(time.time() * 1000))
#r = requests.get(captcha_url, headers=headers) #请求验证码图片链接
#im = Image.open(BytesIO(r.content))   #直接读取bytes数据，生成图片对象
im = Image.open('./assets/04.png')
width, height = im.size
#获取图片中的颜色，返回列表[(counts, color)...]
color_info = im.getcolors(width*height)
sort_color = sorted(color_info, key=lambda x: x[0], reverse=True)
#将背景全部改为白色, 提取出字，每张图片一个字
char_dict = {}
for i in range(1, 6):
    start_x = 0
    im2 = Image.new('RGB', im.size, (255, 255, 255))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if im.getpixel((x, y)) == sort_color[i][1]:
                im2.putpixel((x, y), (0, 0, 0))
                if not start_x:
                    start_x = x  #标记每个字符的起始位置，用于最后字符串的排序
            else:
                im2.putpixel((x, y), (255, 255, 255))
    char = pytesseract.image_to_string(im2, lang='normal',config='--psm 10')
    char_dict[start_x] = char
code = ''.join([item[1] for item in sorted(char_dict.items(), key=lambda i:i[0])])
print(code)