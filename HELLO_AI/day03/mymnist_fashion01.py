import tensorflow as tf
import numpy as np
import cv2

# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

test_image = test_images
labels_correct = test_labels

# 2. 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 훈련
model.fit(train_images, train_labels, epochs=5)

# 6. 정확도 평가하기
loss, accuracy = model.evaluate(test_images, test_labels)
predict_result = model.predict(test_images)

print("loss: ", loss)
print("accuracy: ", accuracy)

cnt = [0,0,0,0,0,0,0,0,0,0]

for idx, data in enumerate(predict_result):
    ai_result = np.argmax(predict_result[idx])
    cnt[ai_result] += 1
    cv2.imwrite(f"./{ai_result}/{idx}.png", test_image[idx])
    print(ai_result,"-",idx)
    # print(idx, cnt)
