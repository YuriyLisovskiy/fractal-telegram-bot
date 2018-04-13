from PIL import Image
import random


class JuliaSet:

	def __init__(self, x=1024, y=1024):
		self.x = x
		self.y = y
		self.name = 'JuliaSetFractal.png'

	def generate(self):
		image = Image.new('RGB', (self.x, self.y))
		xa = -2.0
		xb = 2.0
		ya = -1.5
		yb = 1.5
		max_iterations = 255

		# find a good Julia set point using the Mandelbrot set
		while True:
			cx = random.random() * (xb - xa) + xa
			cy = random.random() * (yb - ya) + ya
			c = cx + cy * 1j
			z = c
			for i in range(max_iterations):
				if abs(z) > 2.0:
					break
				z = z * z + c
			if i > 10 and i < 100:
				break

		# draw the Julia set
		for y in range(self.y):
			zy = y * (yb - ya) / (self.y - 1) + ya
			for x in range(self.x):
				zx = x * (xb - xa) / (self.x - 1) + xa
				z = zx + zy * 1j
				for i in range(max_iterations):
					if abs(z) > 2.0:
						break
					z = z * z + c
				image.putpixel((x, y), (i % 8 * 32, i % 16 * 16, i % 32 * 8))
		image.save(self.name, 'PNG')
