from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watchForCodes(personDict):
    font = ImageFont.truetype("/Users/zrj/repos/lowerthird-barcode/fonts/Roboto-Black.ttf", 80)
    while True:
        code = input("Scan new barcode.")
        code = code[0:11]
        personDict[code].printInfo()
        img = Image.open('lowerthird.tiff')
        I1 = ImageDraw.Draw(img)
        I1.text((100, 850), personDict[code].fullName(), font=font, fill=(255, 255, 255))
        I1.text((100, 950), personDict[code].superlative, font=font, fill=(255, 255, 255))
        img.save("lowerthirdNamed.tiff")




import cv2 as cv

img=cv.imread('lowerthirdNamed.tiff')
while True:
    img=cv.imread('lowerthirdNamed.tiff')
    cv.imshow("image",img)
    k=cv.waitKey(10) & 0XFF
    if k== 27 :
        break

cv.destroyAllWindows()