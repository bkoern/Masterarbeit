import cv2
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw

def main():
    
    width = 1368
    #x_max = width - 68 #1300
    #x_min = 100
    
    height = 912
    #y_max = height - 112 #800
    #y_min = 200
    
    df = pd.read_csv('Dateien.txt')
    for index, row in df.iterrows():
    
        im = Image.new('RGB', (width, height), (255, 255, 255));
        draw = ImageDraw.Draw(im)
        #draw.rectangle((x_min, y_min, x_max, y_max), fill=(240, 240, 240), outline=(10, 10, 10))


        name = row['files']
        df = pd.read_csv(name + '.csv')
        for index, row in df.iterrows():
            match row['type']:
                case 'l':
                    draw.line((row['x1'], row['y1'], row['x2'], row['y2']), fill=(0, 0, 0), width=25)
                case 'c':
                    draw.ellipse((row['x1'], row['y1'], row['x2'], row['y2']), fill=(240, 240, 240), outline=(0, 0, 0), width=25)
                
        im.save(name + '.png')

main()
print("Generierung fertig.")