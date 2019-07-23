import pygame
import os;


class ImageLibrary:
    def __init__(self):
        self.m_imagedb = []

    # Load an image, expects a file name. Returns a pygame.image
    def LoadImage(self, p_filename):
        # first we check to see if the filename has already been loaded into memory.
        # this way we do not load the same image data more than once.
        for imagerec in self.m_imagedb:
            if p_filename == imagerec[0]:
                # found the image name, so return the image file.
                return imagerec[1]
        # We did not find it already loaded, so we will load it and store it into the database.
        image = pygame.image.load(p_filename)
        self.m_imagedb.append((p_filename, image))
        # return the generated pygame.image
        return self.m_imagedb[-1][1]


class SoundLibrary:
    def __init__(self):
        self.m_sounddb = []

    # Load an image, expects a file name. Returns a pygame.image
    def LoadSound(self, p_filename):
        # first we check to see if the filename has already been loaded into memory.
        # this way we do not load the same image data more than once.
        for soundrec in self.m_sounddb:
            if p_filename == soundrec[0]:
                # found the image name, so return the image file.
                return soundrec[1]
        # We did not find it already loaded, so we will load it and store it into the database.
        sound = pygame.mixer.Sound(p_filename)
        self.m_sounddb.append((p_filename, sound))
        # return the generated pygame.image
        return self.m_sounddb[-1][1]

    def PlayEffect(self, soundnumber):
        self.m_sounddb[soundnumber][1].play()

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
imglibrary = ImageLibrary()
spriteone = pygame.transform.scale((imglibrary.LoadImage("smile.png")), (200, 200))
sndlibrary = SoundLibrary()
sndlibrary.LoadSound('ohnorobot16b.wav')
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play(-1)
sndlibrary.PlayEffect(0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(spriteone, (20, 20))
    pygame.display.flip()
    clock.tick(60)
