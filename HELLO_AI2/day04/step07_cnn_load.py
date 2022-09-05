
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2

labels = [
    "곽금규",
    "곽동석",
    "김민수",
    "심재린",
    "조정현",
  ]


img1 = cv2.imread('output.png')
print("img1",img1.shape)
train_images = img1.reshape((1,480,640,3))
train_images = train_images/255.0




model = tf.keras.models.load_model('myvoice.h5')

predictions = model.predict(train_images)

print(labels[np.argmax(predictions[0])])
    
