# Mandelbrot set
from PIL import Image
from random import random
from mandelbrot import mandelbrot_set

maxIterations = 100

image = mandelbrot_set((-2,0.47),(-1.12,1.12),(1235,1120),100)
image.show()