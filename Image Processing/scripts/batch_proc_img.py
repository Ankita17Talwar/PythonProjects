# Batch image resizing

import cv2
import glob

imgs = glob.glob("data\sample_images\*.jpg")


for image in imgs:
    img = cv2.imread(image,0)
    resize = cv2.resize(img, (100,100))
    cv2.imshow('Image',resize)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    print("resized_" + image)
    cv2.imwrite('resized_' + image, resize)