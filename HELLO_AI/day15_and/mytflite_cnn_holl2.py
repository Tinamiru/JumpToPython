
import tensorflow as tf
from tensorflow import keras
import numpy as np

print(tf.__version__)

train_images_a = [
    [1, 0],
    [0, 1],
]

train_labels_a = [0, 1]


train_images = np.array(train_images_a,dtype=np.float16)
train_images = np.reshape(train_images,(2,2))

train_labels = np.array(train_labels_a) 



model = keras.Sequential([
    keras.layers.Flatten(input_shape=(2,1)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(2)
])



model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)


predictions = model.predict(train_images)


converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

f = open('mnist_cnn_holl2.tflite', "wb")
f.write(tflite_model)
f.close()


