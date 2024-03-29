
import tensorflow as tf
from tensorflow import keras
import numpy as np


train_images_a = [
    [0,0,0,0],
    [0,1,0,0],
    [1,0,0,0],
    [1,1,0,0],
    
    [0,0,0,1],
    [0,1,0,1],
    [1,0,0,1],
    [1,1,0,1],
    
    [0,0,1,0],
    [0,1,1,0],
    [1,0,1,0],
    [1,1,1,0],

    [0,0,1,1],
    [0,1,1,1],
    [1,0,1,1],
    [1,1,1,1]
]
train_labels_a = [
    2,1,1,0,
    1,2,0,1,
    1,0,2,1,
    0,1,1,2
]


train_images = np.array(train_images_a,dtype=np.float16)
train_images = np.reshape(train_images,(16,4))

train_labels = np.array(train_labels_a) 



model = keras.Sequential([
    keras.layers.Flatten(input_shape=(4,1)),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(3)
])



model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=50)


predictions = model.predict(train_images)


converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

f = open('mnist_cnn_strike.tflite', "wb")
f.write(tflite_model)
f.close()





