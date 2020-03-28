import glob
c = glob.glob(r"""D:\temp\*.*""")    # a list of files' path


from PIL import Image
import os

def make_thumb(path, sizes=(1024,)):
    base, ext = os.path.splitext(path)
    try:
        im = Image.open(path)
    except IOError:
        return
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255-x)
            im = im.convert('RGB')
            im.paste((255,255,255), None, bgmask)
        else:
            im = im.convert('RGB')
            
    width, height = im.size
            
    for size in sizes:
        filename = base + "_width==1024" + ".jpg"
        thumb = im.resize((size,size*height//width), Image.ANTIALIAS)
        thumb.save(filename, quality=100)    # default quality=75

if __name__ == '__main__':    
    for i in c:
        make_thumb(r''+i)
