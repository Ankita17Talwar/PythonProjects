from PIL import ImageEnhance
from PIL import Image

def enhance_brightness(inp_img, factor):
    img = Image.open(inp_img)
    img_enh_obj = ImageEnhance.Brightness(img)

    new_img = img_enh_obj.enhance(factor)
    # low factor -> less color(brightness, contrast etc), 1= retunrs same quality image

    new_img.save('Output\ImageEnhance\enhanced_img.jpg')



if __name__ == '__main__':
    enhance_brightness('data\images\low_bright.jpg', 2.5)
