import numpy as np 
import time
from numpy.fft import fft, fftshift, fftfreq
import scipy.io.wavfile as wav
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.animation as animation

def read_song(fname):
	(rate, song) = wav.read(fname)
	fps = 30
	song_data = np.zeros( (len(song)/rate * fps, rate/fps, 2) )
	for n in xrange(len(song)/rate * fps):
		song_data[n,:,:] = (song[n*rate/fps:(n+1)*rate/fps,:])/2**15.
	return song_data, rate

def process_song(song_data,  sample_rate, time_step, leftright):
	#fft is real data only	
	song_data[time_step,:,leftright] = song_data[time_step,:,leftright] - \
			np.mean(song_data[time_step,:,leftright])
	fft_data = fft(song_data[time_step,:,leftright])
	fft_length = len(fft_data)/2;
	if (fft_length % 2 != 0):
		fft_length += 1
	spectrum = abs(fft_data[:fft_length-1])
	N = fft_length
	freq = sample_rate/fft_length * np.arange(1,fft_length)
	return freq, spectrum

def integrate_power(freq, spectrum, width):
	#chops off the decimal of len(freq)/width but that's at like 40 kHz anyways. Doesn't matter.
	freq = freq[:len(freq/width)]
	spectrum = spectrum[:len(freq/width)]
	power = [0 for n in xrange(len(freq)/width - 1)]
	sampled_freq = [0 for n in xrange(len(freq)/width - 1)]
	maximum_scale = 0
	for n in xrange(len(freq)/width - 1):
		power[n] = integrate(freq[n*width:(n+1)*width], spectrum[n*width:(n+1)*width])
		highestVal  = max(power) 
		if highestVal > maximum_scale:
			maximum_scale = highestVal
		sampled_freq[n] = (freq[n*width] + freq[(n+1)*width])*0.5
	return  sampled_freq, power, width, maximum_scale

def integrate(freq, spectrum):
	dx = freq[1] - freq[0]
	power = 0
	for n in xrange(len(freq)-1):
		power += dx * (spectrum[n] + spectrum[n+1])*0.5
	return abs(power)

def ani_frame(freq, pow_series, maximum_scale, width):
	fig = plt.figure()
	frame = plt.gca()
	l, = plt.plot( [], [], 'b-')
	plt.xlim(0,8000)
	plt.ylim(0, maximum_scale)
	plt.xlabel('Frequency (Hz)')
	plt.title('Call Me Pathetic - Stoker')
	plt.ylabel('Power')
	plt.setp(l, linewidth=2.0)
	frame.axes.get_yaxis().set_ticks([])
	def update_img(num, freq, data, line, frame):
		line.set_ydata(data[num, :])
		line.set_xdata(freq[num, :])
		return line,

	ani = animation.FuncAnimation(fig, update_img, pow_series.shape[0], fargs=(freq,r_pow_series,  l, frame),interval=50)
	writer = animation.writers['ffmpeg'](fps=30)

	ani.save('stoker.mp4', writer = writer, dpi=100)
	return ani

if __name__ == '__main__':
	song, rate = read_song('stoker.wav')
	width = 3
	dummy_freq, dummy_spec = process_song(song, rate, 10*60, 0)
	dummy_freq, dummy_pow, width, maximum_scale = integrate_power(dummy_freq, dummy_spec, width)
	r_pow_series = np.zeros( (len(song), len(dummy_pow))) 
	l_pow_series = np.zeros( (len(song), len(dummy_pow)) )
	freq = np.zeros( (len(song), len(dummy_freq)) )
	max_val = 0
	for n in xrange(len(song)):
		lfreq, lspectrum = process_song(song, rate, n, 0)
		rfreq, rspectrum = process_song(song, rate, n, 1)
		freqs, lpower, width, maximum_scale = integrate_power(lfreq, lspectrum, width)
		freqs, rpower, width, maximum_scale = integrate_power(rfreq, rspectrum, width)
		r_pow_series[n,:] = rpower
		l_pow_series[n,:] = lpower
		freq[n,:] = freqs
		if maximum_scale > max_val:
			max_val = maximum_scale
	ani_frame(freq, r_pow_series, max_val, width)
