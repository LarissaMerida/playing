import numpy as np
from scipy.stats import mode
import cv2
import os
import csv
import time


path = 'C:/Users/larissa.santos/Desktop/dev/opencv/faces'
os.chdir(path)

# salva o arquivo com o título atualizado por data e hora
titulo = time.strftime("%Y-%m-%d") + '_' +time.strftime("%H-%M-%S")
saida  = open('face_recon_'+titulo+'.csv', 'w')
export = csv.writer(saida, quoting=csv.QUOTE_NONNUMERIC)


file_list = []

for file in os.listdir(path):
    if file.endswith(".jpg"):
        file_list.append(file)

print(file_list)