# Imports
import torch
from PIL import Image
import numpy as np
from PIL import ImageGrab
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import pygame
import pygame.camera 

model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)
imagename = "Camerafeed.png"
def takePicture():
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist: 
        cam = pygame.camera.Camera(camlist[0], (640, 480))
        cam.start()
        image = cam.get_image()
        pygame.image.save(image, imagename)
def analysePicture():
    img = np.array(Image.open(imagename).resize((3840,2160)).convert("RGB"))
    plt.imshow(img)
    results = model([img])
    results.print()
    results.xyxy[0]
    result = results.pandas().xyxy[0]
    prices = {
        40: 1.49,
        43: 0.15,
        44: 0.15,
        45: 0.15,
        50: 0.50,
        54: 1.25,
        68: 399.99,
        74: 24.99,
        77: 4.99,
        78: 14.99,
        80: 1.25
    }
    img = np.array(Image.open(imagename).resize((3840,2160)).convert("RGB"))
    fig, ax = plt.subplots()
    ax.imshow(img)

    for x in range(len(result["xmin"])):
        if result["class"][x].item() in prices.keys():
            rect = patches.Rectangle((result["xmin"][x], result["ymin"][x]), result["xmax"][x] - result["xmin"][x], result["ymax"][x] - result["ymin"][x], linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            #ax.text(result["xmax"][x], result["ymin"][x], result["name"][x],bbox={'facecolor': 'grey', 'alpha': 0.5, 'pad': 10})

    plt.savefig("annotatedoutput.png")
    with open("itemsrecognized.txt", "w") as out1, open("prices.txt", "w") as out2:
        out1.truncate(0)
        out2.truncate(0)
        for x in range(len(result["xmin"])):
            if result["class"][x].item() in prices.keys():
                out1.write(str(result["name"][x]) + "\n")
                out2.write(str(prices[result["class"][x].item()]) + "\n")

#Master Loop
while True:
    takePicture()
    analysePicture()