import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker #for what???
import math

# create dictionary(this step might be ommited if we will use
# only one type of audiofile)

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

# definig functions to format graph

def format_time(x, pos=None):
    global duration, nframes, k
    progress = int(x / float(nframes) * duration * k)
    mins, secs = divmod(progress, 60)
    hours, mins = divmod(mins, 60)
    out = "%d:%02d" % (mins, secs)
    if hours > 0:
        out = "%d:" % hours
    return out

def format_db(x, pos=None):
    if pos == 0:
        return ""
    global peak
    if x == 0:
        return "-inf"
    db = 20 * math.log10(abs(x) / float(peak))
    return int(db)

# open file(it may be better to combine two programs into one)
wav = wave.open("output.wav", mode="r")
#(number of channels, byte per sample, frame per second, number of frames, compression type, compression name)
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

duration = nframes / framerate
# paremeters of graph
w, h = 800, 300
k = nframes/w/32
DPI = 72
peak = 256 ** sampwidth / 2

content = wav.readframes(nframes)
samples = np.fromstring(content, dtype=types[sampwidth])

f=open("test.txt", 'wb')
np.savetxt(f, samples, '%10.1f', newline="")

plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)
plt.subplots_adjust(wspace=0, hspace=0)

# now we are making graph

for n in range(nchannels):
    channel = samples[n::nchannels]
    
    channel = channel[0::k]
    if nchannels == 1:
        channel = channel - peak
    
    axes = plt.subplot(2, 1, n+1, axisbg="k")
    axes.plot(channel, "g")
    axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
    plt.grid(True, color="w")
    axes.xaxis.set_major_formatter(ticker.NullFormatter())

axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
plt.savefig("wave", dpi=DPI)
plt.show()