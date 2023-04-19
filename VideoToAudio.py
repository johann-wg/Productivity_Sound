# extract audio file from video file

import moviepy.editor as mp

video = mp.VideoFileClip("/users/desktop/test.mp4")

audio = video.audio

audio.write_audiofile("/users/desktop/audio.mp3")
