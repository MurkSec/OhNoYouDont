#import pygame
#import os;

class ImageLibrary:
    def __init__(self):
        self.m_image = []
        self.m_filename = []

    def LoadImage(self, p_filename):
        self.m_filename.append(p_filename)
        
