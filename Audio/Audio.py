from pydub import AudioSegment


audio = AudioSegment.from_file('audio.mp3')

audio.export('./Audio/hasil.mp3', format='mp3')