# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from tensorboard.compat import tf
import numpy as np
from keras.utils.np_utils import to_categorical

class HerKY:
    def __init__(self):
        self.model = tf.keras.models.load_model('mnist_holl.h5')

    def guess(self,train_images):
        train_images_a = train_images
        
        train_images = np.array(train_images_a)
        
        model = tf.keras.models.load_model("mnist_holl.h5")
        
        predict_result = model.predict(train_images)
        
        ai_answer = np.argmax(predict_result[0])
        
        return ai_answer
