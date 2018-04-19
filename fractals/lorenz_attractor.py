import random
from PIL import Image


class LorenzAttractor:

	def __init__(self, x=1024, y=1024, max_iterations=100000):
		self.x = x
		self.y = y
		self.max_iterations = max_iterations
		self.name = 'LorenzAttractorFractal.png'

	@staticmethod
	def lorenz(x, y, z):
		delta = float(10)
		r = float(28)
		b = float(8) / 3
		h = 1e-3
		dx_dt = delta * (y - x)
		dy_dt = r * x - y - x * z
		dz_dt = x * y - b * z
		x += dx_dt * h
		y += dy_dt * h
		z += dz_dt * h
		return x, y, z

	def generate(self):
		print('Generating {}, please wait...'.format(self.name))
		image = Image.new('RGB', (self.x, self.y))
		size = 30
		xa = -size
		xb = size
		ya = -size
		yb = size
		x = random.random() * size * 2 - 1
		y = random.random() * size * 2 - 1
		z = random.random() * size * 2 - 1
		# dx/dt = delta * (y - x)
		# dy/dt = r * x - y - x * z
		# dz/dt = x * y - b * z
		for i in range(self.max_iterations):
			(x, y, z) = self.lorenz(x, y, z)
			xi = int((self.x - 1) * (x - xa) / (xb - xa))
			yi = int((self.y - 1) * (y - ya) / (yb - ya))
			if 0 <= xi < self.x and 0 <= yi < self.y:
				image.putpixel((xi, yi), (255, 255, 255))
		image.save(self.name, 'PNG')
		return self.name
