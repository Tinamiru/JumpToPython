import cv2

cascade_filename = 'face.xml'



cascade = cv2.CascadeClassifier(cascade_filename)


def imgDetector(cascade):
    img = cv2.imread('startup.png')
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # cascade 얼굴 탐지 알고리즘 
    results = cascade.detectMultiScale(gray,  # 입력 이미지
                                       scaleFactor=1.2,  # 이미지 피라미드 스케일 factor
                                       minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                       minSize=(3, 3)  # 탐지 객체 최소 크기
                                       )
    
        
    for box in results:
        pengsu = cv2.imread('pengsu.png')

        x, y, w, h = box
        mosaic_loc = img[y:y + h, x:x + w]
        img_w_mosaic = img
        img_w_mosaic[y:y + h, x:x + w] = mosaic_loc
        
        
        presize = cv2.resize(pengsu, (mosaic_loc.shape[0], mosaic_loc.shape[1]))
        
        h, w, c = presize.shape
        roi = img[y:y + h, x:x + w]  # 배경이미지의 변경할(다음 로고 넣을) 영역
        mask = cv2.cvtColor(presize, cv2.COLOR_BGR2GRAY)  # 로고를 흑백처리
        # 이미지 이진화 => 배경은 검정. 글자는 흰색
        mask[mask[:] == 255] = 0
        mask[mask[:] > 0] = 255
        mask_inv = cv2.bitwise_not(mask)  # mask반전.  => 배경은 흰색. 글자는 검정
        daum = cv2.bitwise_and(presize, presize, mask=mask)  # 마스크와 로고 칼라이미지 and하면 글자만 추출됨
        back = cv2.bitwise_and(roi, roi, mask=mask_inv)  # roi와 mask_inv와 and하면 roi에 글자모양만 검정색으로 됨
        pengsu = cv2.add(daum, back)  # 로고 글자와 글자모양이 뚤린 배경을 합침
        img[y:y + h, x:x + w] = pengsu
        
        
        cv2.destroyAllWindows()
        cv2.imshow("Mosaic", img)
    print("peng",pengsu.shape)
    # 사진 출력        


cv2.waitKey(0)
cv2.destroyAllWindows()
    
img = cv2.imread('startup.png')

print("img", type(img))

imgDetector(cascade)

cv2.waitKey(0)
cv2.destroyAllWindows()
