from PIL import Image
import numpy as np
import cv2
import time
import os

HEIGHT = 39 # HEIGHT % 3 must be equal 0 
WIDTH = int(HEIGHT * (4/3))

clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def transform(img_arr):
  image = ''
  for i in range(len(img_arr)):
    for j in range(len(img_arr[i])):
      num = int(img_arr[i][j][0])
      if 0 <= num <= 99: image += '..'
      if 100 <= num <= 149: image +=  '**'
      if 150 <= num <= 255: image +=  '##'
    image += '\n'
  print(image)

vidcap = cv2.VideoCapture('bad_apple.mp4')
success, image = vidcap.read()

while success:
  start_time = time.time()
  clear_console()
  success, image = vidcap.read()
  img = Image.fromarray(image).convert('LA').resize((WIDTH, HEIGHT))
  img_arr = np.array(img)
  transform(img_arr)
  time.sleep(1/30 - (time.time() - start_time))