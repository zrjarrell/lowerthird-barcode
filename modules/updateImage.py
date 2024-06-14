import cv2 as cv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from modules.makeBarcodes import getFullName

# def watchForCodes(personDict):
#     img = cv.imread('lowerthirdNamed.tiff')
#     cv.imshow("image", img)
#     cv.waitKey(1)
#     try:
#         while True:
#             key = input("Input key")
#             updateImage(personDict, key)
#             cv.imshow("image", img)
#             cv.waitKey(1)
#     except KeyboardInterrupt:
#         cv.destroyAllWindows()

def updateImage(personDict, key):
    font = ImageFont.truetype("/Users/zrj/repos/lowerthird-barcode/fonts/Roboto-Black.ttf", 80)
    img = Image.open('lowerthird.tiff')
    I1 = ImageDraw.Draw(img)
    I1.text((100, 850), getFullName(personDict[key]), font=font, fill=(255, 255, 255))
    I1.text((100, 950), personDict[key]['superlative'], font=font, fill=(255, 255, 255))
    img.save("lowerthirdNamed.tiff")


# import json

# f = open('personDict.json',)
# personDict = json.load(f)

# img = cv.imread("lowerthird.tiff")
# cv.imshow("image",img)
# cv.waitKey(10)
# try:
#     while True:
#         key = input("input key")
#         updateImage(personDict, key)
#         img=cv.imread("lowerthirdNamed.tiff")
#         cv.imshow("image",img)
#         cv.waitKey(10)
# except KeyboardInterrupt:
#     pass

# cv.destroyAllWindows()
