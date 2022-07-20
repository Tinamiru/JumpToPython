import cv2

cascade_filename = 'face.xml'
cascade = cv2.CascadeClassifier(cascade_filename)

def imgDetector(img, cascade):

    # 영상 압축
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # cascade 얼굴 탐지 알고리즘 
    results = cascade.detectMultiScale(gray,  # 입력 이미지
                                       scaleFactor=1.2,  # 이미지 피라미드 스케일 factor
                                       minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                       minSize=(3, 3)  # 탐지 객체 최소 크기
                                       )        

    for box in results:

        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=1)

    # 사진 출력        
    cv2.imshow('facenet', img)  
    cv2.waitKey(10000)

img = cv2.imread('startup.png')
print("img", type(img))

imgDetector(img,cascade)

cv2.waitKey(0)
cv2.destroyAllWindows()