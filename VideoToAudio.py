# extract audio file from video file

import moviepy.editor as mp

video = mp.VideoFileClip("/users/jjong/desktop/test.mp4")

audio = video.audio

audio.write_audiofile("/users/jjong/desktop/audio.mp3")
