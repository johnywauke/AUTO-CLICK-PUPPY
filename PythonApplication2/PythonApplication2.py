import numpy as np
from PIL import ImageGrab
from click import click, queryMousePosition, PressKey, ReleaseKey, SPACE
import time

tamanhotelajogo = [559,44,562,48]
tamanhotela = [973,102,979,109] #fecha o X
tamanhotela2 = [580,287,966,649] #clica no tesouro
tamanhotela3 = [982,335,988,338] #clica cetro
tamanhotela4 = [889,640,930,650] #compra cachorro
tamanhotela5 = [674,529,888,575] #clica comercial merge
tamanhotela6 = [1478,74,1484,80] #fecha comercial
tamanhotela7 = [1482,62,1490,70] #fecha comercial2
tamanhotela71 = [1361,240,1380,250] #fecha comercial2
tamanhotela8 = [982,59,991,64] #fecha comercial3
tamanhotela9 = [993,44,995,56] #fecha comercial3
tamanhotela10 = [874,40,1007,65] #fecha comercial4
start_time_of_level = 0

def clicanatela(reds):
 global no_of_clicks_this_level,tamanhotela
 reds = [i[0] for i in reds]
 x = int(reds[1] + tamanhotela[0] + 5)
 y = int(reds[0] + tamanhotela[1] + 5)
 print(x,y,'  reds')
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela2(reds2):
 global no_of_clicks_this_level,tamanhotela2
 reds2 = [i[0] for i in reds2]
 x = int(reds2[1] + tamanhotela2[0] + 5)
 y = int(reds2[0] + tamanhotela2[1] + 5)
 print(x,y,'   reds2')
 time.sleep(1)
 click(x,y)
 start_time = 0
def clicanatela3(reds3):
 global no_of_clicks_this_level,tamanhotela3
 reds3 = [i[0] for i in reds3]
 x = int(reds3[1] + tamanhotela3[0] + 5)
 y = int(reds3[0] + tamanhotela3[1] + 5)
 print(x,y,'   reds3')
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela4(reds4):
 global no_of_clicks_this_level,tamanhotela4
 reds4 = [i[0] for i in reds4]
 x = int(reds4[1] + tamanhotela4[0] + 5)
 y = int(reds4[0] + tamanhotela4[1] + 5)
 print(x,y,'   reds4')
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 click(777,812)
 time.sleep(0.1)
 start_time = 0
def clicanatela5(reds5):
 global no_of_clicks_this_level,tamanhotela5
 reds5 = [i[0] for i in reds5]
 x = int(reds5[1] + tamanhotela5[0] + 5)
 y = int(reds5[0] + tamanhotela5[1] + 5)
 print(x,y,'   reds5')
 time.sleep(1)
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela6(reds6):
 global no_of_clicks_this_level,tamanhotela6
 reds6 = [i[0] for i in reds6]
 x = int(reds6[1] + tamanhotela6[0] + 5)
 y = int(reds6[0] + tamanhotela6[1] + 5)
 print(x,y,'   reds6')
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela7(reds7):
 global no_of_clicks_this_level,tamanhotela7
 reds7 = [i[0] for i in reds7]
 x = int(reds7[1] + tamanhotela7[0] + 5)
 y = int(reds7[0] + tamanhotela7[1] + 5)
 print(x,y,'   reds7')
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela8(reds8):
 global no_of_clicks_this_level,tamanhotela8
 reds8 = [i[0] for i in reds8]
 x = int(reds8[1] + tamanhotela8[0] + 5)
 y = int(reds8[0] + tamanhotela8[1] + 5)
 print(x,y,'   reds8')
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela9(reds9):
 global no_of_clicks_this_level,tamanhotela9
 reds9 = [i[0] for i in reds9]
 x = int(reds9[1] + tamanhotela9[0] + 5)
 y = int(reds9[0] + tamanhotela9[1] + 5)
 print(x,y,'   reds9')
 click(x,y)
 time.sleep(0.1)
 start_time = 0
def clicanatela10(reds10):
 global no_of_clicks_this_level,tamanhotela10
 reds10 = [i[0] for i in reds10]
 x = int(reds10[1] + tamanhotela10[0] + 5)
 y = int(reds10[0] + tamanhotela10[1] + 5)
 print(x,y,'   reds10')
 click(x,y)
 time.sleep(0.1)
 start_time = 0

while True:
   screen5 = np.array(ImageGrab.grab(bbox=tamanhotelajogo))
   color=np.array([152,190,71],dtype=np.uint8)
   color2=np.array([46,57,21],dtype=np.uint8)
   reds5=np.where(np.all((screen5==color),axis=-1))
   reds6=np.where(np.all((screen5==color2),axis=-1))
   if len(reds5[0]) + len(reds6[0])> 0:
    start_time = time.time()
    time.sleep(0.1)
    screen = np.array(ImageGrab.grab(bbox=tamanhotela))
    color=np.array([255,255,255],dtype=np.uint8)
    reds=np.where(np.all((screen==color),axis=-1))
    if len(reds[0]) > 0:
      clicanatela(reds)
      clicks_per_second =  (time.time() - start_time)
      print("Clicks per second {}".format(clicks_per_second))
    else:
     #clica no tesouro
     start_time = time.time()
     time.sleep(0.1)
     screen2 = np.array(ImageGrab.grab(bbox=tamanhotela2))
     color2= np.array([186,109,247],dtype=np.uint8)
     reds2= np.where(np.all((screen2==color2),axis=-1))
     if len(reds2[0]) > 0:   
      clicanatela2(reds2)
      clicks_per_second =  (time.time() - start_time)
      print("Clicks per second {}".format(clicks_per_second))
     else:
      #clica cetro
      start_time = time.time()
      time.sleep(0.1)
      screen3 = np.array(ImageGrab.grab(bbox=tamanhotela3))
      color3= np.array([252,172,33],dtype=np.uint8)
      reds3= np.where(np.all((screen3==color3),axis=-1))
      if len(reds3[0]) > 0:   
       clicanatela3(reds3)
       clicks_per_second =  (time.time() - start_time)
       print("Clicks per second {}".format(clicks_per_second))
      else:
      #compracachorro
       start_time = time.time()
       time.sleep(0.1)
       screen4 = np.array(ImageGrab.grab(bbox=tamanhotela4))
       color4= np.array([195,143,73],dtype=np.uint8)
       reds4= np.where(np.all((screen4==color4),axis=-1))
       if len(reds4[0]) > 0:   
        clicanatela4(reds4)
        clicks_per_second =  (time.time() - start_time)
        print("Clicks per second {}".format(clicks_per_second))
       else:
      #compraclicar comercial merge
        start_time = time.time()
        time.sleep(0.1)
        screen5 = np.array(ImageGrab.grab(bbox=tamanhotela5))
        color5= np.array([255,183,0],dtype=np.uint8)
        reds5= np.where(np.all((screen5==color5),axis=-1))
        if len(reds5[0]) > 0:   
         clicanatela5(reds5)
         clicks_per_second =  (time.time() - start_time)
         print("Clicks per second {}".format(clicks_per_second))
   else:
    #aclicar comercial merge
    screen5 = np.array(ImageGrab.grab(bbox=tamanhotela5))
    color5= np.array([255,255,255],dtype=np.uint8)
    reds5= np.where(np.all((screen5==color5),axis=-1))
    if len(reds5[0]) > 0:   
     click(1577,767)
     time.sleep(2)
     print("esperando")
    else:
     #aclicar comercial merge
     screen5 = np.array(ImageGrab.grab(bbox=tamanhotela5))
     color5= np.array([0,0,0],dtype=np.uint8)
     reds5= np.where(np.all((screen5==color5),axis=-1))
     if len(reds5[0]) > 0:   
      click(1577,767)
      time.sleep(2)
      print("esperando")


