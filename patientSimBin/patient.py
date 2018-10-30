from __future__ import print_function
import random

import sys
import os
import signal
from flask import Flask, url_for, render_template

from flask import jsonify
import requests
import simplejson
import json

#import pylab
import scipy.signal as signal
import numpy
import random

def ecg(beatsPerMinute = 60):
    # The "Daubechies" wavelet is a rough approximation to a real,
    # single, heart beat ("pqrst") signal
    pqrst = signal.wavelets.daub(10)

    # Add the gap after the pqrst when the heart is resting.
    samples_rest = 10
    zero_array = numpy.zeros(samples_rest, dtype=float)
    pqrst_full = numpy.concatenate([pqrst,zero_array])

    # Simulated Beats per minute rate
    # For a health, athletic, person, 60 is resting, 180 is intensive exercising
    bpm = beatsPerMinute
    bps = bpm / 60

    # Simumated period of time in seconds that the ecg is captured in
    capture_length = 10

    # Caculate the number of beats in capture time period
    # Round the number to simplify things
    num_heart_beats = int(capture_length * bps)

    # Concatonate together the number of heart beats needed
    ecg_template = numpy.tile(pqrst_full , num_heart_beats)

    # Add random (gaussian distributed) noise
    noise = numpy.random.normal(0, 0.01, len(ecg_template))
    ecg_template_noisy = noise + ecg_template

    # Simulate an ADC by sampling the noisy ecg template to produce the values
    # Might be worth checking nyquist here
    # e.g. sampling rate >= (2 * template sampling rate)
    sampling_rate = 50.0
    num_samples = sampling_rate * capture_length
    ecg_sampled = signal.resample(ecg_template_noisy, int(num_samples))

    # Scale the normalised amplitude of the sampled ecg to whatever the ADC
    # bit resolution is
    # note: check if this is correct: not sure if there should be negative bit values.
    adc_bit_resolution = 1024
    ecg =  adc_bit_resolution * ecg_sampled

    return ecg

if __name__ == "__main__":
#    print(generate_buzz())
    print ("Entering Main Function")
    #print (sys.argv[1])
    print ("Exiting Main Function")
