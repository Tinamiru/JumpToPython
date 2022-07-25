import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import numpy as np
import cv2

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

for idx, data in enumerate(train_images):
    cv2.imwrite(f"./train/{train_labels[idx][0]}/{idx}.png", train_images[idx])