from PIL import Image
from PIL import ImageFilter, ImageEnhance, ImageFont, ImageDraw

def sketch(inp, out):

    img = Image.open(inp)
    img_obj = img.filter(ImageFilter.CONTOUR)
    img_obj.save(out)
    enhance_sharpness(out,2)


def enhance_sharpness(inp_img, factor):
    img = Image.open(inp_img)
    img_enh_obj = ImageEnhance.Sharpness(img)

    new_img = img_enh_obj.enhance(factor)
    new_img.save('Output\ImageEnhance\enhaanced_sketch.jpg')


if __name__ == '__main__':
    sketch('data\images\PXL_20220402_073007401.jpg','Output\ImageEnhance\img_sketch.jpg')
