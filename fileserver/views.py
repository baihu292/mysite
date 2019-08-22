import os
from PIL import ImageColor
from . import color
from . import settings
from django.http import HttpResponse
from removebg import RemoveBg
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


api_data = None
no_bg_path_img = None
file = None
path = None


# 首页
def index(request):
    return render(request, 'index.html')


# 接收上传的图片
@ csrf_exempt
def uploadfile01(request):
    global file
    global path
    global api_data

    if request.method == "POST":
        try:
            file = request.FILES.get("file", None)  # 接收上传的文件

            path = settings.MEDIA_ROOT  # 文件存储路径
            if not file:
                return HttpResponse("no files for upload!")
            
            destination = open(os.path.join(path, file.name), 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
                
        except:
            return HttpResponse('上传失败！！！')
        try:
            rmbg = RemoveBg(api_data, "error.log")
            rmbg.remove_background_from_img_file(os.path.join(path, file.name))
        except:
            return HttpResponse('抠图失败')
        return HttpResponse('上传成功！！！')



# 获取上传的API
def bg_api(request):
    global api_data
    api = request.GET['api_data']
    api_data = api
    return HttpResponse('')


# 获取上传的颜色信息
def wx_data01(request):
    # global color_data
    global path
    global file
    formula = request.GET['formula']
    try:
        result = eval(formula, {})
        if result == 2:
            color_data = ImageColor.getrgb('White') # ['255, 255, 255']
            a = color.img_deal(file, path, color_data)
            return HttpResponse(a)
        elif result == 4:
            color_data = ImageColor.getrgb("DodgerBlue")# ['30, 144, 255']
            a = color.img_deal(file, path, color_data)
            return HttpResponse(a)
        elif result == 6:
            color_data = ImageColor.getrgb("Red")# [255,0, 0']
            a = color.img_deal(file, path, color_data)
            return HttpResponse(a)
        else:
            pass
    except:
        return HttpResponse('底色信息获取失败！！！')
    





