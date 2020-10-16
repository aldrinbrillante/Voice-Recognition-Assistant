# pip3 install moviepy
from moviepy.editor import VideoFileClip
import pygame

pygame.display.set_caption('My video!')

clip = VideoFileClip('vreea.mov')
clip.preview()
pygame.quit()