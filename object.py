import numpy as np
import pygame as pg
from methods import *


class Object():
    ins = []

    def __init__(self, vertex, faces, screen, color=(80, 150, 50)):
        self.__class__.ins.append(self)
        self.vertex = vertex
        self.faces = faces
        self.color = color
        self.screen = screen

        self.basis = np.array([(1, 0, 0),
                               (0, 1, 0),
                               (0, 0, 1)])
        self.b = np.array([(1, 0, 0),
                           (0, 1, 0)])

        self.cam = np.array([(0, 0, -1)])

        self.x, self.y, self.z = 0, 0, 0

        # импорт объекта из obj файла
        # коментов побольше чем обычно потому что код функции не совсем мой и таким обычно не пользуюсь

    def move(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def scale(self, width, height, depth):
        self.basis = self.basis @ s(width, height, depth)
        self.b = self.b @ s(width, height, depth)

    def rot_xy(self, angle):
        self.basis = self.basis @ rot_xy(angle)
        self.b = self.b @ rot_xy(angle)

    def rot_xz(self, angle):
        self.basis = self.basis @ rot_xz(angle)
        self.b = self.b @ rot_xz(angle)

    def rot_yz(self, angle):
        self.basis = self.basis @ rot_yz(angle)
        self.b = self.b @ rot_yz(angle)

    def render(self):
        for faces in self.faces:
            poly = []
            p = []
            for index in faces:
                coords = self.b @ self.vertex[index].T
                p.append(self.vertex[index])
                poly.append((coords[0] + self.x, coords[1] + self.y))

            norm = calc_norm(p, self.basis)
            ang = np.dot(self.cam, norm)

            if ang >= 0:
                # pg.draw.polygon(self.screen, (150 + 100 * ang, 150 + 100 * ang, 150 + 100 * ang), poly, False)
                pg.draw.polygon(self.screen, (130, 120, 70), poly, True)
