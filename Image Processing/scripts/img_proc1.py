# Load, display , Resize and create image
import cv2

# read image ; flag =1 to read as coloured , 0 for Black-white
img = cv2.imread('Data\galaxy.jpg', 0)

print(img)
print(img.shape)

# resize image
resized_img = cv2.resize(img,(1000,500))
# resize in same ratio
resz_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2 ) ))

# show image
cv2.imshow('Galaxy',resz_img)
cv2.imwrite('Output\Galaxy_Resized.jpg', resz_img)
cv2.waitKey(2000) # 2000 ms ; if set to 0 image will stay until closed
cv2.destroyAllWindows()