# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from tensorboard.compat import tf
import numpy as np
from keras.utils.np_utils import to_categorical

train_images_a = [[0,1]]

train_images = np.array(train_images_a)

model = tf.keras.models.load_model("mnist_hit.h5")

predict_result = model.predict(train_images)

ai_answer = np.argmax(predict_result[0])

print("ai_answer", ai_answer)
