from moviepy.editor import VideoFileClip

video = VideoFileClip('video.mp4') 
video.write_videofile('video.mp4')

short_video = video.subclip(0, 20)  # Mendapatkan 10 detik pertama
short_video.write_videofile('hasilcrop.mp4')