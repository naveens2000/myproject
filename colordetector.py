# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:20:15 2020

@author: Naveen
"""

import cv2
import webbrowser
import webcolors
import text_to_speech as speech
from googletrans import Translator
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = webcolors.rgb_to_name((requested_colour))
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name
lang=input("CHOOSE LANGUAGE 1).'en' FOR ENGLISH    2).'ta' FOR TAMIL")
if(lang=="en"):
    name=input("enter your sweet name:")
    speech.speak("welcome to color identifier device,{}".format(name),"en")
    inputimg=input("please input the image")
if(lang=="ta"):
     name=input("உங்கள் பெயரை உள்ளிடவும்")
     speech.speak("வண்ண அடையாளங்காட்டி சாதனத்திற்கு நாங்கள் வரவேற்கிறோம் ., {}".format(name),"ta")
     inputimg=input("தயவுசெய்து படத்தை உள்ளிடவும்:")
img = cv2.imread(inputimg)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
moment = cv2.moments(gray_img)
X = int(moment ["m10"] / moment["m00"])
Y = int(moment ["m01"] / moment["m00"])
pixel_b, pixel_g, pixel_r = img[X][Y]
print(pixel_r,pixel_b,pixel_g)
requested_colour = (pixel_r,pixel_g,pixel_b)
#closest_name=webcolors.rgb_to_name((pixel_r,pixel_g,pixel_b))
closest_name = get_colour_name(requested_colour)
print (closest_name)
translator = Translator()
t=translator.translate(closest_name,dest='ta')
english="THE COLOR IDENTIFIED BY OUR DEVICE IS "+closest_name
tamil="எங்கள் சாதனத்தால் அடையாளம் காணப்பட்ட வண்ணம்"+t.text
if(lang=="en"):
    speech.speak(english,"en")
else:
    speech.speak(tamil,"ta")
f = open('naveen.html','w+')
wrapper = """<html >
<head>
<title>
color identifier device
</title></head>
<body><h1 style="font-size:70px">THE LIQUID COLOR IS <span style="color:%s;text-transform:uppercase">%s</span></h1></body>
<footer style="text-align:center;color:%s;position: fixed;right: 0;bottom: 0;font-size:50px">done by naveen and ramanathan</footer>
</html>"""
whole = wrapper % (closest_name,closest_name,closest_name)
f.write(whole)
f.close()
webbrowser.open_new_tab('naveen.html')
if(lang=="en"):
    speech.speak("thank you {} for using our device".format(name),"en")
else:
    speech.speak("எங்கள் சாதனத்தைப் பயன்படுத்தியதற்கு நன்றி,{}".format(name),"ta")
