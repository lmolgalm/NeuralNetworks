import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import cmath

# this step is for case if we decide to choose amount of channels

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

# open file, that we have got from audio we need to do that
# cause pyaudio doesn't work with python3.4
wav = wave.open("output.wav", mode="r")
#(number of channels, byte per sample, frame per second, number of frames,
#compression type, compression name)
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

# defining parameters of record
duration = nframes / framerate
w, h = 800, 150 #width and height of plot
k = nframes/w/32 #step of plot (save time)
DPI = 72 # resolution
peak = 256 ** sampwidth / 2

#reading data
content = wav.readframes(nframes)
# creating numpy array
samples = np.fromstring(content, dtype=types[sampwidth])
print(len(samples))

#saving array in TXT
f=open("test.txt", 'wb')
np.savetxt(f, samples, '%10.1f', newline="")


# defining size of graph
plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)

#making grapk for each channel
for n in range(nchannels):
    channel = samples[n::nchannels]
    channel = channel[0::k]
    # create plot
    axes = plt.subplot(1, 1, n+1, axisbg="k")
    axes.plot(channel, 'g')
    #we are not marking axes, because we do not need it (y)
    axes.yaxis.set_major_formatter(ticker.NullFormatter())
    #create scale
    plt.grid(True, color="w")
#axes.xaxis.set_major_formatter(ticker.NullFormatter())
#(x)
axes.xaxis.set_major_formatter(ticker.NullFormatter())
plt.savefig("wave", dpi=DPI)
#now we are trying to do FFT

new_test=np.fft.rfft(samples)
new_test=new_test[1:3000]
new_test=np.abs(new_test)
f=open("test1.txt", 'wb')
np.savetxt(f, new_test, '%10.1f', newline="")
print(len(new_test))
plt.figure(2, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)

axes = plt.subplot(1, 1, n+1, axisbg="k")
axes.plot(new_test, 'g')
axes.xaxis.set_major_formatter(ticker.NullFormatter())
axes.yaxis.set_major_formatter(ticker.NullFormatter())

plt.savefig("wave1", dpi=DPI)
plt.show()



