import math
from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageChops
import textwrap
from typing import Tuple

def random_text_color()->Tuple[float,float,float,float]:
    import random
    return (random.choice(range(0,250)),random.choice(range(0,250)),random.choice(range(0,250)),random.choice(range(0,250)))

def random_ttf(folder:str)->str:
    import os,random
    ttf_files=[]
    for root, dirs, files in os.walk(folder, topdown=True):
        for name in files:
            if name.endswith(".otf") or name.endswith(".ttf"):
                ttf_file=os.path.join(root, name)
                ttf_files.append(ttf_file)
    return random.choice(ttf_files)

def text2image(text:str,font_path:str,text_color:Tuple[float,float,float,float],img_size:Tuple[float,float]=(800,300))->Image:

    para = textwrap.wrap(text, width=30)

    MAX_W, MAX_H = img_size
    im = Image.new('RGB', (MAX_W, MAX_H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, 20)

    current_h, pad = 50, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line,fill=text_color, font=font)
        current_h += h + pad
    return im

def set_opacity(im:Image, opacity:float)->Image:
    '''
    设置水印透明度
    '''
    assert opacity >= 0 and opacity <= 1

    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def crop_image(im:Image)->Image:
    '''裁剪图片边缘空白'''
    bg = Image.new(mode='RGBA', size=im.size)
    diff = ImageChops.difference(im, bg)
    del bg
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im
def add_water_mark(im:Image,text:str,mark_font:str,color="#8B8B1B",space=75,angle=30,_size=20,opacity=0.15,quality=100)->Image:
    """_summary_

    Args:
        im (Image): Image object
        text (str): mark text
        mark_font (str): font path
        color (str, optional): text color like '#000000'. Defaults to "#8B8B1B".
        space (int, optional): space between watermarks. Defaults to 75.
        angle (int, optional): rotate angle of watermarks. Defaults to 30.
        _size (int, optional): font size of text. Defaults to 20.
        opacity (float, optional): opacity of watermarks. Defaults to 0.15.
        quality (int, optional): quality of output images. Defaults to 100.

    Returns:
        Image: Image object
    """
    # 字体宽度
    width = len(text) * _size

    # 创建水印图片(宽度、高度)
    mark = Image.new(mode='RGBA', size=(width,_size))

    # 生成文字
    draw_table = ImageDraw.Draw(im=mark)
    draw_table.text(xy=(0, 0),
                    text=text,
                    fill=color,
                    font=ImageFont.truetype(mark_font,
                                            size=_size))
    del draw_table

    # 裁剪空白
    mark = crop_image(mark)

    # 透明度
    set_opacity(mark, opacity)

    def mark_im(im):
        ''' 在im图片上添加水印 im为打开的原图'''

        # 计算斜边长度
        c = int(math.sqrt(im.size[0]*im.size[0] + im.size[1]*im.size[1]))

        # 以斜边长度为宽高创建大图（旋转后大图才足以覆盖原图）
        mark2 = Image.new(mode='RGBA', size=(c, c))

        # 在大图上生成水印文字，此处mark为上面生成的水印图片
        y, idx = 0, 0
        while y < c:
            # 制造x坐标错位
            x = -int((mark.size[0] + space)*0.5*idx)
            idx = (idx + 1) % 2

            while x < c:
                # 在该位置粘贴mark水印图片
                mark2.paste(mark, (x, y))
                x = x + mark.size[0] + space
            y = y + mark.size[1] + space

        # 将大图旋转一定角度
        mark2 = mark2.rotate(angle)

        # 在原图上添加大图水印
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        im.paste(mark2,  # 大图
                 (int((im.size[0]-c)/2), int((im.size[1]-c)/2)),  # 坐标
                 mask=mark2.split()[3])
        del mark2
        return im

    return mark_im(im)