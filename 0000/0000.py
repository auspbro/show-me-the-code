#!/usr/local/bin/python
#coding=utf-8

"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

from PIL import Image, ImageDraw, ImageFont

number = str(99)     
color = (255, 0, 0)   # 红色
# windows_font = 'Arial.ttf'  # 自己添加字体
windows_font = 'c:/windows/fonts/Arial.ttf'  # 调用 Windows 系统字体

def draw_text(text, fill_color, windows_font):
    im = Image.open('zen.jpg')
    x, y = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(windows_font, 200)
    draw.text((x-250, 10), text, fill_color, font)

    im.save('zen-demo.jpg')
    # im.show('zen-demo.jpg')     # 显示图片
    return 0

if __name__ == '__main__':
    draw_text(number, color, windows_font)
