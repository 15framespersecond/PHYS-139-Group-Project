import json

def import_files(file_path):
    try:
        with open(file_path, 'r') as file:
            d = json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {file_path}.")
    return d

#Python Script to make dataset
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime
import os
import ipywidgets as widgets
from ipywidgets import  interactive
# Jupyter/ IPython formatting
from IPython.display import Math, Latex, display

# Default values for plots
plt.rcParams["figure.figsize"] = [14, 9] # figure width and height
plt.rcParams["font.size"] = 20


            

def get_signal_data(path):
    path = path + '/data/raw/dataSD1500/'
    files = os.listdir(path)
    binsize = 0.025
    y = []
    t=[]
    for f in files:
        data = import_files(path+f)

#stations contain the signal of the 3 pmts of the wcds and some related parameters
        stations = pd.DataFrame(data['stations'])
        stations.set_index('id', inplace=True)

        
    
        wcd = stations.iloc[0] #select the first station 

        # Assuming y is a list initialized earlier in your code
        y.append(wcd.pmt1)
        time = [np.arange(len(wcd[f'pmt{i + 1}'])) * binsize for i in range(3)]
        t.append(time[0])
    return y, t, data