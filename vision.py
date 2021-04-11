'''
this has been developed to read text from image using google API capabilities
this takes path to image as an input and produces the regognized text as output
-SL
'''
import os, io
from google.cloud import vision
#import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"
client = vision.ImageAnnotatorClient()

def vision_ocr(path):
#file_name = str(input('Enter image name - '))
#image_path = f'.\VisionAPI\Images\{file_name}'

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    # construct an image instance
    image = vision.types.Image(content=content)

    # annotate Image Response
    response = client.text_detection(image=image)  # returns TextAnnotation
    #df = pd.DataFrame(columns=['locale', 'description'])
    texts = response.text_annotations
    #print(texts)
    for text in texts:
        # df = df.append(
        #     dict(
        #         locale=text.locale,
        #         description=text.description
        #     ),
        #     ignore_index=True
        # )

        return(texts)

path2='/home/steven/Projects/invoice_cap/invoice.jpg'

#testing
print(vision_ocr(path2))
