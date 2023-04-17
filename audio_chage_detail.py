# 오디오 비트, 채널 변경
from pydub import AudioSegment

input_file = "/users/jjong/desktop/test/tiny riot.wav"
output_file = "/users/jjong/desktop/test/tiny riot2.wav"

# 오디오 파일 불러오기
audio = AudioSegment.from_file(input_file, format="wav")

# 채널 수, 샘플링 레이트, 샘플 너비 설정
audio = audio.set_channels(1)
audio = audio.set_frame_rate(44100)
audio = audio.set_sample_width(2)

# WAV 파일로 내보내기
audio.export(output_file, format="wav")
