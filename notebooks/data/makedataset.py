#Python Script to make dataset
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os, sys, json, datetime, random
from scipy.signal import butter, filtfilt

def import_file(file_path):
    '''imports one file
    '''
    try:
        with open(file_path, 'r') as file:
            d = json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {file_path}.")
    return d            

def get_signal_data(path):
    '''Taking in the path of the project ex /home/tuckyg/Documents/PHYS-139-GROUP-PROJECT and returns signal data similar to previous hw
    '''
    path = path + '/data/raw/dataSD1500/'
    files = os.listdir(path)
    binsize = 0.025
    y = []
    data_to_save=[]
    for f in files:
        data = import_file(path+f)

#stations contain the signal of the 3 pmts of the wcds and some related parameters
        stations = pd.DataFrame(data['stations'])
        stations.set_index('id', inplace=True)

        
    
        wcd = stations.iloc[0] #select the first station 

        # Assuming y is a list initialized earlier in your code
        y.append(wcd.pmt1)
        time = [np.arange(len(wcd[f'pmt{i + 1}'])) * binsize for i in range(3)]
        data_to_save.append([wcd.pmt1])
    return y, data_to_save

def VEM_to_eV(VEM):
    VEM = np.array(VEM)
    '''slope and intercept are claculated using the energy-calibration.ipynb
    '''
    slope = 45.14153715340955
    intercept = 2.3400270892667407
    return ((VEM - intercept) / slope)/10


def generate_noise(length, alpha):
    white_noise = np.random.normal(0, 1, length)
    freq = np.fft.fftfreq(length)
    colored_noise = white_noise / (np.sign(freq)*np.abs(freq)**(alpha / 2) + 1)
    
    return white_noise + colored_noise

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y / 10


