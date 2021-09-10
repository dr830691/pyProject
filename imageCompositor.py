from ctypes import resize
from wand.image import Image
from wand.drawing import Drawing
from wand.display import display
from wand.color import Color
def combining(mainImage,logoImage,i):
    with Image(filename=mainImage)  as img1:     
        img1.resize(400,500) #resize the image
        # display(img1)
        with Image(filename=logoImage) as img2:
            img2.resize(172,63)
            with Image(width=img1.width ,height=img1.height) as img:
                img.composite(image=img1,left=0,top=0)
                img.composite(image=img2,left=5,top=5)
                
                path="./compositeImages/new"+str(i)+".png"
                img.save(filename=path)  #composite images are saving in composite image folder
                print(str(i)+" Image is combined successfully")
                # print(img) 
                # print("running succesfully")   
#Testing the Function
# mainImage="./data/image1.jpg" 
# logoImage="./data/nike_black.png" 
# combining(mainImage,logoImage)      