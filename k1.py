import tensorflow as tf

model_path = "model.h5"
loaded_model = tf.keras.models.load_model(model_path)
import cv2
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("archive/Test/00014.png")
print(image)
image_fromarray = Image.fromarray(image, 'RGB')
resize_image = image_fromarray.resize((30, 30))
expand_input = np.expand_dims(resize_image,axis=0)
input_data = np.array(expand_input)
input_data = input_data/255

pred = loaded_model.predict(input_data)
result = pred.argmax()
print(result)