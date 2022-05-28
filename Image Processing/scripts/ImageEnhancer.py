from PIL import ImageEnhance
from PIL import Image

def enhance_brightness(inp_img, factor):
    img = Image.open(inp_img)
    img_enh_obj = ImageEnhance.Brightness(img)

    new_img = img_enh_obj.enhance(factor)
    # low factor -> less color(brightness, contrast etc), 1= retunrs same quality image

    new_img.save('Output\ImageEnhance\enhanced_brigh_img.jpg')

def enhance_contrast(inp_img,factor):
    img = Image.open(inp_img)
    img_enh_obj = ImageEnhance.Contrast(img)

    new_img = img_enh_obj.enhance(factor)
    new_img.save('Output\ImageEnhance\enhanced_Bri_contrast_img.jpg')

def enhance_sharpness(inp_img, factor):
    img = Image.open(inp_img)
    img_enh_obj = ImageEnhance.Sharpness(img)

    new_img = img_enh_obj.enhance(factor)
    new_img.save('Output\ImageEnhance\enhanced_sharp_img.png')


if __name__ == '__main__':
    enhance_brightness('data\images\sample_img1.jpg', 2.5)
    enhance_contrast(r'Output\ImageEnhance\enhanced_brigh_img.jpg', 1.5)
    enhance_sharpness(r'data\images\blurr_img1.png',2)
