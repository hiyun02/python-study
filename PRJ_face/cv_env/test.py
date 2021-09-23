#   opencv python 코딩
#   얼굴을 인식한 상태에만 자동으로 촬영
#

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# haar cascade 검출기 객체 선언
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

font = ImageFont.truetype('fonts/SCDream6.otf', 20)

# 무한루프
while True:    

    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M')
    nowDatetime_path = now.strftime('%Y-%m-%d %H_%M')

    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    # 글자가 잘보이도록 배경을 넣어줌
    # img는 사각형을 넣을 이미지, pt1, pt2는 사각형의 시작점과 끝점, color는 색상(파랑,초록,빨강), tickness는 선굵기(-1은 내부를 채우는 것)
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)     
    
    # 아래의 4줄은 글자를 영상에 더해주는 역할을 함    
    frame = Image.fromarray(frame)    
    draw = ImageDraw.Draw(frame)    
    # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
    draw.text(xy=(10, 15),  text="얼굴인식 중.. \n현재시간 "+nowDatetime, font=font, fill=(255, 255, 255))
    frame = np.array(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 영상을 흑백으로 바꿔줌

    # scaleFactor를 1에 가깝게 해주면 정확도가 상승하나 시간이 오래걸림
    # minNeighbors를 높여주면 검출률이 상승하나 오탐지율도 상승
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.5, minNeighbors=3, minSize=(20,20))
    #print(faces)
    
    key = cv2.waitKey(30)   # 30ms 동안 키입력 대기
    if key == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
        break
    # 찾은 얼굴이 있으면
    # 얼굴 영역을 영상에 사각형으로 표시
    if len(faces) :
        for  x, y, w, h in faces :
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,255,255), 2, cv2.LINE_4)
        if key == ord('c'):       # c 키를 누르면
            # (파일이름(한글불가, 영어만), 이미지)로 영상을 캡쳐하여 그림파일로 저장
            cv2.imwrite("capture " + nowDatetime_path + ".png", frame)  # 파일이름(한글안됨), 이미지 
    cv2.imshow("original", frame)   # frame(카메라 영상)을 original 이라는 창에 띄워줌

capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌