from pydub import AudioSegment

audio = AudioSegment.from_file('/workspaces/multimedia-python/audio.mp3')
audio.export('hasil.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('hasilcrop.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('hasilgabung.mp3', format='mp3')

audio.export('result.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('hasilvol.mp3', format='mp3')