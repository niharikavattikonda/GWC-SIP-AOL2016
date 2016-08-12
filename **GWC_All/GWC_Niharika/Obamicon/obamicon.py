'''
Additional documentation can be found here: http://effbot.org/imagingbook/image.htm
'''
from PIL import Image

##path = r"C:\Users\GWC\Desktop\niharika.jpg"

im = Image.open("niharika.jpg")

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

def obamicize(image_data):
    newpic = []
    for item in image_data:
        r = item[0]
        g = item[1]
        b = item[2]
        sum_pic = r + g + b
        if sum_pic < 182:
            newpic.append(darkBlue)
        elif 182 <= sum_pic <= 364:
            newpic.append(red)
        elif 364 <= sum_pic <= 546:
            newpic.append(lightBlue)
        elif sum_pic > 546:
            newpic.append(yellow)
    return newpic

imDataList = list(im.getdata())
obamicized_data = obamicize(imDataList)
obamicized_image = Image.new(im.mode, im.size)
obamicized_image.putdata(obamicized_data)
obamicized_image.save("output.jpg", "jpeg")


'''
    Returns: a new list of image data.
    
    This function creates a new list of pixels that converts an image's pixels into an Obama campaign-style photo.
    
    If the pixel has low intensity (<182) the new pixel will be dark blue.
    If the pixel is medium/low intensity (between 182 and 364) the new pixel will be red.
    If the pixel is medium/high intensity (between 364 and 546) the new pixel will be light blue.
    If the pixel is high intensity (>546) the new pixel will be yellow.
    
    Parameter image_data: a list of pixels 
    '''
    
