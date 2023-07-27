import os
import numpy as np
from tensorflow import keras
import tensorflow as tf
import librosa
from matplotlib import pyplot
from tqdm import tqdm
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
import sys

def get_metadata(file_name):
    if file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '01':
        emo = 'neutral'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '02':
        emo = 'calm'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '03':
        emo = 'happy'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '04':
        emo = 'sad'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '05':
        emo = 'angry'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '06':
        emo = 'fearful'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '07':
        emo = 'disgust'
    elif file_name[-len('03-01-06-02-02-01-07.wav'):][6:8] == '08':
        emo = 'surprised'
        
    if int(file_name[-len('03-01-06-02-02-01-07.wav'):][18:20]) % 2 == 0:  # Gender
        gen = 'female'
    else:
        gen = 'male'
        # 01 = neutral, 02 = calm, 03 = happy, 04 = sad, 
        # 05 = angry, 06 = fearful, 07 = disgust, 
        # 08 = surprised
    return emo, gen


fn = []
for dirname, _, filenames in os.walk('/mount/Project/Project Files/Data/Audio/Audio Speech Sentiment/'):
    for filename in filenames:
        fn.append(os.path.join(dirname, filename))