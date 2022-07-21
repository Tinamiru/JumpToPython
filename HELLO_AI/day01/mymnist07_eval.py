import numpy as np
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

test_image = test_images
labels_correct = test_labels

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)
test_loss, test_acc = model.evaluate(test_images, test_labels)



predict_result = model.predict(test_images)
cnt_o = 0
cnt_x = 0
for idx, data in enumerate(predict_result):
    go_label = labels_correct[idx]
    ai_label = np.argmax(predict_result[idx])
    print(idx)
    go_index = str(go_label)
    ai_index = str(ai_label)
    i = str(idx)
    if go_label == ai_label:
            cv2.imwrite("./test/o/" + go_index + "_" + ai_index + "_" + i + ".png", test_image[idx])
            cnt_o += 1
    else:
            cv2.imwrite("./test/x/" + go_index + "_" + ai_index + "_" + i + ".png", test_image[idx])
            cnt_x += 1
print("cnt_o", cnt_o)
print("cnt_x", cnt_x)
print("Done")
