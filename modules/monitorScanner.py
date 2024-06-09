from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from modules.makeBarcodes import getFullName

def monitorScanner(scanner):
    try:
        while True:
            reading = scanner.read(13).decode('utf-8')
            print(reading)
            scanner.reset_input_buffer()
            with open('queue.txt', 'a') as queue:
                queue.write(reading)
    except KeyboardInterrupt:
        pass



# def monitorScanner(scanner):
#     try:
#         while True:
#             reading = scanner.read(13).decode('utf-8')
#             scanner.reset_input_buffer()
#             if reading[-1] == '>':
#                 with open('queue.txt', 'a') as queue:
#                     queue.write(reading)
#     except KeyboardInterrupt:
#         pass


def watchForCodes(personDict, key):
    font = ImageFont.truetype("/Users/zrj/repos/lowerthird-barcode/fonts/Roboto-Black.ttf", 80)
    img = Image.open('lowerthird.tiff')
    I1 = ImageDraw.Draw(img)
    I1.text((100, 850), getFullName(personDict[key]), font=font, fill=(255, 255, 255))
    I1.text((100, 950), personDict[key]['superlative'], font=font, fill=(255, 255, 255))
    img.save("lowerthirdNamed.tiff")




# import cv2 as cv

# img=cv.imread('lowerthirdNamed.tiff')
# while True:
#     img=cv.imread('lowerthirdNamed.tiff')
#     cv.imshow("image",img)
#     k=cv.waitKey(10) & 0XFF
#     if k== 27 :
#         break

# cv.destroyAllWindows()