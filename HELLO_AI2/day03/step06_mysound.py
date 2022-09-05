import librosa

import librosa.display
import matplotlib
import numpy as np

y, sr = librosa.load("output.wav")

t= np.array(0,len(y))

sr = np.ones((200))

