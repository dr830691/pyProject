from pptx import Presentation
from imageCompositor import combining 
from pptGenerator  import pptSlideAdder
number_of_slides=6 #taken the input number of slides to be added
for i in range(1,number_of_slides):
    mainImage="./data/image"+str(i)+".jpg" 
    logoImage="./data/nike_black.png" 
    # print(mainImage,logoImage)
    #function to composite main image with Logo image the 
    combining(mainImage,logoImage,i)
    prs = Presentation() #create a presentation object
    prs.save('output.pptx') # create a test.pptx file
pptSlideAdder("output.pptx",number_of_slides) #function to generate ppt
