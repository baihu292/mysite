import os
from PIL import Image


def img_deal(file, path, color_data): # 图片底色转换
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
        
    return 'http://39.107.247.16/media/' + file.name + '_bh.png'  # 返回下载处理过后的图片地址
