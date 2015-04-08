
import pyaudio
import wave

# here we declare parameters of recording

CHUNK = 1024 
FORMAT = pyaudio.paInt16   #16bit
CHANNELS = 1               #mono sound
RATE = 44100               #sample rate
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

#use class for audio

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

#start recording

print("* recording")

# the empty frame(list) is generated where recorded info will be stored

frames = []

#here we read CHUNK of data as many times as we need and
#store it into our frame(list)

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) # 2 bytes(16 bits) per channel

print("* done recording")

#stop recording

stream.stop_stream()
stream.close()
p.terminate()

# write sound into new file(possibly, this step might be ommited)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
