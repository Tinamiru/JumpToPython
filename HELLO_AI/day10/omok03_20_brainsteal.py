from tensorflow.python.keras.models import load_model
import numpy as np

model = load_model('models/20201213_202430.h5')

input_arr = [
    [1,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],

    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],

    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
    [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
]

input_n = np.array(input_arr)
input = np.reshape(input_n(1,20,20,1))


output = model.predict(input).squeeze()
output = output.reshape((20, 20))
output_y, output_x = np.unravel_index(np.argmax(output), output.shape)
