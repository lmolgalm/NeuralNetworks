import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

# this step is for case if we decide to choose amunt of channels

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
w, h = 800, 300 #width and height of plot
k = nframes/w/32 #step of plot (save time)
DPI = 72 # resolution
peak = 256 ** sampwidth / 2

#reading data
content = wav.readframes(nframes)
# creating numpy array
samples = np.fromstring(content, dtype=types[sampwidth])

#saving array in TXT
f=open("test.txt", 'wb')
np.savetxt(f, samples, '%10.1f', newline="")


# defining size of graph
plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)

#making grapk for each channel
for n in range(nchannels):
    channel = samples[n::nchannels]
    
    channel = channel[0::k]
    # in case if we use sound wasn't normalized
    if nchannels == 1:
        channel = channel - peak

    axes = plt.subplot(2, 1, n+1, axisbg="k")
    axes.plot(channel, "g")
    #we are not marking axes, because we do not need it (y)
    axes.yaxis.set_major_formatter(ticker.NullFormatter())
    #create scale
    plt.grid(True, color="w")
    axes.xaxis.set_major_formatter(ticker.NullFormatter())
#(x)
axes.xaxis.set_major_formatter(ticker.NullFormatter())
plt.savefig("wave", dpi=DPI)
