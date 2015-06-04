__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window()
window.set_caption('stipple-polygon')
fireArray = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0xc0, 0x00, 0x00, 0x01, 0xf0,
             0x00, 0x00, 0x07, 0xf0, 0x0f, 0x00, 0x1f, 0xe0,
             0x1f, 0x80, 0x1f, 0xc0, 0x0f, 0xc0, 0x3f, 0x80,
             0x07, 0xe0, 0x7e, 0x00, 0x03, 0xf0, 0xff, 0x80,
             0x03, 0xf5, 0xff, 0xe0, 0x07, 0xfd, 0xff, 0xf8,
             0x1f, 0xfc, 0xff, 0xe8, 0xff, 0xe3, 0xbf, 0x70,
             0xde, 0x80, 0xb7, 0x00, 0x71, 0x10, 0x4a, 0x80,
             0x03, 0x10, 0x4e, 0x40, 0x02, 0x88, 0x8c, 0x20,
             0x05, 0x05, 0x04, 0x40, 0x02, 0x82, 0x14, 0x40,
             0x02, 0x40, 0x10, 0x80, 0x02, 0x64, 0x1a, 0x80,
             0x00, 0x92, 0x29, 0x00, 0x00, 0xb0, 0x48, 0x00,
             0x00, 0xc8, 0x90, 0x00, 0x00, 0x85, 0x10, 0x00,
             0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00]
fire = (GLubyte * 128)(*fireArray)


@window.event
def on_draw():
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100.0, 100.0, -100.0, 100.0, -1.0, 1.0)
    glColor3f(1.0, 1.0, 0.0)
    glEnable(GL_POLYGON_STIPPLE)
    glPolygonStipple(fire)
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 0.0)
    glVertex2f(50.0, 0.0)
    glVertex2f(50.0, 50.0)
    glVertex2f(0.0, 50.0)
    glEnd()
    glFlush()

pg.app.run()
