import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<0.003:
            pass
        else:
            break
        idx_f+=1
        
    idx_f-=10
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<0.003:
            pass
        else:
            break
        idx_l-=1
        
    idx_l+=10
    
    return arr_n[idx_f:idx_l]


y, sr = librosa.load("김유미가3.mp3")

y_trim = cutMute(y)

t = np.arange(0, len(y_trim))
print(sr)
print(y_trim)


plt.plot(t,y_trim)
plt.savefig("kim.png")
plt.grid()
plt.show()




