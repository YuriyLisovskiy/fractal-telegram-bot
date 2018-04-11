import math
import random
from PIL import Image


class QuasiCrystal:

	def __init__(self, x=512, y=512, name='quasi_crystal.png'):
		self.img_x = x
		self.img_y = y
		self.name = name

	def generate(self):
		image = Image.new("RGB", (self.img_x, self.img_y))
		pixels = image.load()
		f = random.random() * 40 + 10  # frequency
		p = random.random() * math.pi  # phase
		n = random.randint(10, 20)     # rotations
		for ky in range(self.img_y):
			y = float(ky) / (self.img_y - 1) * 4 * math.pi - 2 * math.pi
			for kx in range(self.img_x):
				x = float(kx) / (self.img_x - 1) * 4 * math.pi - 2 * math.pi
				z = 0.0
				for i in range(n):
					r = math.hypot(x, y)
					a = math.atan2(y, x) + i * math.pi * 2.0 / n
					z += math.cos(r * math.sin(a) * f + p)
				c = int(round(255 * z / n))
				pixels[kx, ky] = (c, c, c)  # gray scale
		image.save(self.name, 'PNG')
