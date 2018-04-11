import math
import random
from PIL import Image


class ApollonianGasket:

	def __init__(self, x=512, y=512, max_iterations=256, name='CircleInversionFractal.png'):
		self.name = name
		self.img_x = x
		self.img_y = y
		self.max_iterations = max_iterations

	def generate(self):
		image = Image.new("RGB", (self.img_x, self.img_y))
		pixels = image.load()
		n = random.randint(3, 6)  # of main circles
		a = math.pi * 2.0 / n
		r = math.sin(a) / math.sin((math.pi - a) / 2.0) / 2.0  # r of main circles
		h = math.sqrt(1.0 - r * r)
		xa = -h
		xb = h
		ya = -h
		yb = h  # viewing area
		cx = [0.0]
		cy = [0.0]
		cr = [1.0 - r]  # center circle
		for i in range(n):  # add main circles
			cx.append(math.cos(a * i))
			cy.append(math.sin(a * i))
			cr.append(r)
		x = -2.0
		y = -2.0  # initial point (outside of the circles)
		for i in range(self.max_iterations):
			k = random.randint(0, n)  # selected circle for inversion
			dx = x - cx[k]
			dy = y - cy[k]
			d = math.hypot(dx, dy)
			dx = dx / d
			dy = dy / d
			d_new = cr[k] ** 2.0 / d
			x = d_new * dx + cx[k]
			y = d_new * dy + cy[k]
			kx = int((self.img_x - 1) * (x - xa) / (xb - xa))
			ky = int((self.img_y - 1) * (y - ya) / (yb - ya))
			try:
				pixels[kx, ky] = (255, 255, 255)
			except Exception as exc:
				print(exc)
		image.save(self.name, "PNG")
