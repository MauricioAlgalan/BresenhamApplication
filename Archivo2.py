# uncompyle6 version 3.6.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
# [GCC 8.3.0]
# Embedded file name: /home/black/Source/Simulador/Archivo2.py
# Compiled at: 2014-04-23 19:03:37
import pygame
from pygame import gfxdraw
from pygame import *
red = (222, 0, 0)
black = (0, 0, 0)

class Muestra:

    def __init__(self, geometry=(640, 480), Delta_t=30, r=15):
        self.geometry = geometry
        self.Delta_t = Delta_t
        self.radio = r
        self.coordenada = (0, 0)
        self.puntos = []
        pygame.init()
        self.Pantalla = display.set_mode(self.geometry)
        self.Pantalla.fill(black)
        pygame.display.set_caption('CNC', 'cnc')
        gfxdraw.circle(self.Pantalla, self.coordenada[0], self.coordenada[1], self.radio, red)
        pygame.display.flip()

    def marcar(self):
        gfxdraw.pixel(self.Pantalla, self.coordenada[0], self.coordenada[1], red)
        self.puntos.append(self.coordenada)
        self.dibujar()
        pygame.display.flip()

    def dibujar(self):
        for p in self.puntos:
            gfxdraw.pixel(self.Pantalla, p[0], p[1], red)

        pygame.display.flip()

    def mueve(self, posicion=(0, 0), marcar=False):
        if posicion[0] < 0 | posicion[1] < 0 | posicion[0] > self.geometry[0] - 1 | posicion[1] > self.geometry[1] - 1:
            return
        else:
            if posicion[0] < self.coordenada[0]:
                Delta_X = -1
            else:
                Delta_X = 1
            if posicion[1] < self.coordenada[1]:
                Delta_Y = -1
            else:
                Delta_Y = 1
            for x in range(self.coordenada[0], posicion[0] + Delta_X, Delta_X):
                gfxdraw.circle(self.Pantalla, self.coordenada[0], self.coordenada[1], self.radio, black)
                self.dibujar()
                pygame.time.delay(self.Delta_t)
                print (x, self.coordenada[1])
                self.coordenada = (x, self.coordenada[1])
                gfxdraw.circle(self.Pantalla, self.coordenada[0], self.coordenada[1], self.radio, red)
                self.dibujar()
                pygame.time.delay(self.Delta_t)

            for y in range(self.coordenada[1], posicion[1] + Delta_Y, Delta_Y):
                gfxdraw.circle(self.Pantalla, self.coordenada[0], self.coordenada[1], self.radio, black)
                self.dibujar()
                pygame.time.delay(self.Delta_t)
                print (self.coordenada[0], y)
                self.coordenada = (self.coordenada[0], y)
                gfxdraw.circle(self.Pantalla, self.coordenada[0], self.coordenada[1], self.radio, red)
                self.dibujar()
                pygame.time.delay(self.Delta_t)

            if marcar:
                self.marcar()
            gfxdraw.circle(self.Pantalla, self.coordenada[0], self.coordenada[1], self.radio, red)
            pygame.display.flip()
            return
# okay decompiling Archivo2.pyc
