# 음성 파일을 텍스트 파일로 변환하는 함수 정의
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
    with open("output.txt", "w") as f:
      f.write(text)
    print("텍스트 파일로 변환 완료")
  except sr.UnknownValueError:
    print("음성 인식에 실패했습니다.")
  except sr.RequestError as e:
    print("구글 서비스에 접속할 수 없습니다. {0}".format(e))

# 예시: test.wav 라는 음성 파일을 output.txt 라는 텍스트 파일로 변환하기
speech_to_text("Ai2_2.wav")