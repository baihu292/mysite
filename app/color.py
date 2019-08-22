import os
from PIL import Image


def img_deal(file, path, color_data): # 转换底色
    try:
        # 颜色转换
        im = Image.open(os.path.join(path, file.name + '_no_bg.png')) 
        # im = Image.open(os.path.join(path, file.name)) 
        x, y = im.size
        try:
            p = Image.new('RGBA', im.size, color=color_data)
            p.paste(im, (0, 0, x, y), im)
            p.save(os.path.join(path, file.name + '_bh.png'))

        except:
            pass
    except:
        return '底色转换失败了！！！'

    return 'http://39.107.247.16/media/' + file.name + '_bh.png' # 返回下载处理后的图片地址





# 添加水印处理
 # img_url = 'http://127.0.0.1:8000/download/' + file.name + '_bh.png'
            # 添加水印
            # img = Image.open(os.path.join(path, file.name + '_bh.png'))
            # text = "简单方便"
            # font = ImageFont.FreeTypeFont('C:\\Windows\\Fonts\\simhei.ttf', 40)
            # lave = img.convert('RGBA')
            # text_img = Image.new('RGBA', lave.size, (255, 255, 255, 0))
            # img_draw = ImageDraw.Draw(text_img)
            # text_size_x, text_size_y = img_draw.textsize(text, font=font)
            # text_xy = (lave.size[0] - text_size_x, lave.size[1] - text_size_y)
            # img_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 50))
            # after = Image.alpha_composite(lave, text_img)
            # after.save(os.path.join(path, file.name + 'sy.png'))