import numpy
from numpy import sin, linspace, pi
#from pylab import plot, show, title, xlabel, ylabel, subplot, figure, savefig, hist
from numpy import fft, arange
#from scipy import fft, arange, ifft
import aifc, os, subprocess, csv
#import scipy
#import scipy.fftpack
import math

def read_in_solution():
    """
        Read in training data solution
    """
    solution = []
    reader = csv.reader(open('./data/train.csv'))
    reader.next()
    for row in reader:
        solution.append(row)
    return solution

def simplify(y, rms):
    """
        Defauts to 0 everything below rms
    """
    for i in range(len(y)):
        y[i]=y[i]-(1.*rms)
        if y[i] < 0: y[i]=0
    norm_factor = max(y)
    #frequency=[0]*500
    #for i in range(len(y)):
    #y[i]=y[i]/norm_factor

def dominant_frequencies(file, filename, type):
    #print "Matching data in ", path+filename, " with solution in ", solution[counter][0]
    signal, RMS_s, frq, abs_Y, RMS_f = process_image(file)
    # cut below RMS and normalise to 1
    simplify(abs_Y, RMS_f)
    #print signal, RMS_s
    simplify(signal, RMS_s)
    #abs_Y has 2000 points. Divide in 10 intervals
    feature=[]
    for i in range(len(abs_Y)):
        if abs_Y[i]!=0:
            feature.append(i/1000.)
            break

    for i in range(10): feature.append(sum(abs_Y[200*(i):200*(i+1)]))
    feature_norm = max(feature[1:])
    for i in range(1,len(feature)):feature[i]=feature[i]/feature_norm

    #for i in range(40): feature.append(sum(signal[100*(i):100*(i+1)]))
    #feature_norm2 = max(feature[11:])
    #for i in range(11,len(feature)):feature[i]=feature[i]/float(feature_norm2)
    #plot(feature)
    #plot_and_save(signal, frq, abs_Y, type, filename)
    #print type
    #show()
    return feature

def process_image(file):
    # Get frame specifics.
    Fs            = file.getframerate()
    number_frames = file.getnframes()
    raw           = file.readframes(number_frames)
    # Frame data into list.
    signal = numpy.fromstring(raw, numpy.short).byteswap()
    # Length of the signal.
    k = arange(number_frames)
    Total_time = number_frames/Fs
    # dt = float(Total_time)/float(number_frames)
    # Two sides frequency range.
    frq = k/Total_time
    # One side frequency range.
    frq = frq[range(number_frames/2)]
    # FFT computing and normalization
    normalization = sum(abs(signal))
    Y = fft.rfft(signal)/normalization
    Y = Y[range(number_frames/2)]
    abs_Y = abs(Y)
    rms_f = numpy.sqrt(numpy.mean(abs_Y**2))
    #RMS_f = [rms_f for i in xrange(len(frq))]
    #t=range(len(signal))
    signal = abs(signal)
    rms_signal = numpy.sqrt(numpy.mean(signal**2.))
    #RMS_signal = [rms_signal for i in xrange(len(signal))]
    if math.isnan(rms_signal): rms_signal = 0
    if math.isnan(rms_f): rms_f = 0
    return signal, rms_signal, frq, abs_Y, rms_f

def plot_and_save(Y, frq, abs_Y, type, filename):
    fig = figure()
    t=range(len(Y))
    subplot(2,1,1)
    plot(t,Y)
    xlabel('Time')
    ylabel('Amplitude')
    subplot(2,1,2)
    plot(frq,abs_Y,'r') # plotting the spectrum
    #plot(frq,RMS_f)
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')
    #ax.set_yscale('log')
    #plot(frq,abs_Y,'r') # plotting the spectrum
    #plot(frq,RMS)
    #xlabel('Freq (Hz)')
    #ylabel('|Y(freq)|')
    print type
    print filename
    show()
    name = filename
    dir = './data/'+str(type)+'/'
    name=name.strip(".aiff")
    complete_name = dir+name
    fig.savefig(complete_name)
    del fig


