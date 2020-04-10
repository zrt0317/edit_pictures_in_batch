import glob
c = glob.glob(r"""D:\temp\*_width==1024.jpg""")


import cv2
from PIL import Image

for i in range(len(c)):
    # load picture
    img = cv2.imread(c[i])
    
    # add rectangle and word
    width, height, _ = img.shape
    
    cv2.rectangle(img,
                  (height-100, width-50),
                  (height, width),
                  (0, 0, 0),
                  -1)
    
    cv2.putText(img,
                (str(i).rjust(3,'0')),
                (height-70, width-20),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                1,
                (255,255,255),
                1,
                cv2.LINE_AA)
    
    cv2.imwrite((str(i).rjust(3,'0'))+".jpg",
                img)
