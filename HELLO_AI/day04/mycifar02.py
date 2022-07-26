import numpy as np
from tensorflow import keras
from keras import datasets, layers, models

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()

test_image = test_images
labels_correct = test_labels
g_test_images = test_images
print("Train samples:", train_images.shape, train_labels.shape)
print("Test samples:", test_images.shape, test_labels.shape)
 
test_images = test_images.reshape((10000, 32, 32, 3))
test_images = test_images / 255.0
print("test models Sequential")
 
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
print("test compile")
 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

 
print("test with tf.device")
model.fit(train_images, train_labels, epochs=10)
 
print("test evaluate")
test_loss, test_acc = model.evaluate(test_images, test_labels)
 
print('Test accuracy:', test_acc)
 
print("test predictions")
predictions = model.predict(test_images)

cnt_o = 0
cnt_x = 0
for idx, data in enumerate(g_test_images):
    go_label = test_labels[idx]
    ai_label = np.argmax(predictions[idx])
    if go_label == ai_label:
        # cv2.imwrite(f"./test/o/{idx}.png", test_image[idx])
        cnt_o += 1
    else:
        # cv2.imwrite(f"./test/x/{idx}.png", test_image[idx])
        cnt_x += 1
    print("cnt_o: ", cnt_o)
    print("cnt_x: ", cnt_x)
