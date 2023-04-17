# 원하는 특정 파일 하나만 확장자 변경
from pydub import AudioSegment
import os

a_folder = '/Users/jjong/desktop/test'
b_folder = '/Users/jjong/desktop'
file_name = 'tiny riot.wav'

wav_file = os.path.join(a_folder, file_name)
mp3_file = os.path.join(b_folder, file_name.replace('.wav', '.mp3'))
sound = AudioSegment.from_wav(wav_file)
sound.export(mp3_file, format='mp3')