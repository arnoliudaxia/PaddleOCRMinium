# # GPU
# pip install paddlepaddle-gpu

# CPU
# pip install paddlepaddle
# pip install paddleocr

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

# OCR
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = "image.png"
result = ocr.ocr(img_path, cls=True)

# Print Text
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# Show the image with bounding boxes
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save("ocr_result.jpg")