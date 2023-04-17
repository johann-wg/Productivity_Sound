# 폴더 안의 모든 음성 파일을 텍스트로. 두 줄씩 띄워서
import os
import speech_recognition as sr

def speech_to_text(audio_file):
    # 음성 인식 객체 생성
    r = sr.Recognizer()
    # 음성 파일 열기
    with sr.AudioFile(audio_file) as source:
        # 음성 데이터 로드
        audio = r.record(source)
    try:
        # 구글 음성 인식 API를 사용하여 음성 데이터를 텍스트로 변환
        text = r.recognize_google(audio, language="ko-KR")
        # 텍스트 파일로 저장
        with open(os.path.splitext(audio_file)[0] + ".txt", "a") as f:
            f.write(text + "\n\n")  # 수정된 부분
        print(audio_file + "를 텍스트 파일로 변환 완료")
    except sr.UnknownValueError:
        print(audio_file + "의 음성 인식에 실패했습니다.")
    except sr.RequestError as e:
        print("구글 서비스에 접속할 수 없습니다. {0}".format(e))

# 예시: 폴더 안에 있는 모든 음성 파일을 텍스트 파일로 변환하기
folder_path = "/Users/jjong/desktop/test2"
for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        audio_file = os.path.join(folder_path, filename)
        speech_to_text(audio_file)
