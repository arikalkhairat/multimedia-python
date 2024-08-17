from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx

video = VideoFileClip('./Movie/Video.mp4') 
video.write_videofile('./Movie/Video.mp4')

short_video = video.subclip(0, 2)  # Mendapatkan 10 detik pertama
short_video.write_videofile('./Movie/hasilcrop.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('./Movie/Gabungan.mp4')

reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('./Movie/reversed_result.mp4')

sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('./Movie/percepat.mp4')