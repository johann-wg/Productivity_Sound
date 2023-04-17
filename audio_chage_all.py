# 폴더 안의 모든 오디오 파일을 다른 확장자로 변경
from pydub import AudioSegment
import os

# 원본 파일이 있는 폴더
a_folder = '/Users/jjong/desktop/test/'
# 저장할 폴더
b_folder = '/Users/jjong/desktop/'

for file in os.listdir(a_folder):
    if file.endswith('.wav'):
        wav_file = os.path.join(a_folder, file)
        mp3_file = os.path.join(b_folder, file.replace('.wav', '.mp3'))
        sound = AudioSegment.from_wav(wav_file)
        sound.export(mp3_file, format='mp3')