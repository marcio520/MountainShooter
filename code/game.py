#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 400))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            #Check for all events
            #for event in pygame.event.get():
             #if event.type ==  pygame.QUIT:
              #  print('Quitting...')
               # pygame.quit()  #Close window
                #quit() #end pygame