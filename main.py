import pygame as pg
import numpy as np
from object import Object


class App():
    def __init__(self, WIDTH=1300, HEIGHT=700, FPS=60):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        self.FPS = FPS

        # np.array([(0, 1, 2, 3),
        #           (4, 5, 6, 7),
        #           (1, 2, 6, 5),
        #           (2, 3, 7, 6),
        #           (0, 3, 7, 4),
        #           (0, 1, 5, 4)])
        # self.test = Object(
        #     np.array([(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        #               (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]),
        #     np.array([(0, 2, 1), (0, 3, 2),
        #               (4, 5, 6), (4, 6, 7),
        #               (0, 1, 4), (1, 5, 4),
        #               (1, 2, 5), (2, 6, 5),
        #               (2, 3, 7), (2, 7, 6),
        #               (0, 4, 7), (0, 7, 3)]),
        #     self.screen)  # faces
        self.test = self.get_object_from_file('monkey.obj', (100, 100, 100))

        self.test.move(500, 300, 10)
        self.test.scale(180, 180, 100)
        self.test.rot_xy(3.1)
        self.test.rot_xz(3.1)
        self.angle = 0

    def get_object_from_file(self, filename, color):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):  # если линия начинается с символа v
                    # print()
                    vertex.append([float(i) for i in line.split()[1:]])  # добавление вершин
                elif line.startswith('f'):  # если линия начинается с символа f
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])  # добавление граней
        return Object(np.asarray(vertex), np.asarray(faces), self.screen, color)  # возврат объекта с вершинами и гранями из файла

    @staticmethod
    def events():
        [exit() for i in pg.event.get() if i.type == pg.QUIT]

    def update(self):
        pg.display.flip()
        self.clock.tick(self.FPS)

    def draw(self):
        self.screen.fill((50, 50, 50))
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        for o in Object.ins:
            o.render()

    def run(self):
        while True:
            self.events()
            self.draw()

            self.angle += 0.00001
            self.test.rot_xz(self.angle)
            self.test.rot_yz(-self.angle)
            self.test.rot_xy(self.angle)

            self.update()


if __name__ == '__main__':
    app = App()
    app.run()
