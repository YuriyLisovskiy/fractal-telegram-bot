import math
from PIL import Image


class MandelbrotSet:

	def __init__(self, x=1024, y=1024, max_iterations=256):
		if max_iterations > 256:
			raise ValueError('invalid max iterations value')
		self.__xb = 1.0
		self.__yb = 1.5
		self.__ya = -1.5
		self.__xa = -2.0
		self.__img_x = x
		self.__img_y = y
		self.__max_abs_x = 0.0
		self.__max_abs_y = 0.0
		self.__max_abs_z = 0.0
		self.__name = 'MandelbrotFractal.png'
		self.__max_iterations = max_iterations

	def __find_max_values(self):
		for ky in range(self.__img_y):
			b = ky * (self.__yb - self.__ya) / (self.__img_y - 1) + self.__ya
			for kx in range(self.__img_x):
				a = kx * (self.__xb - self.__xa) / (self.__img_x - 1) + self.__xa
				c = complex(a, b)
				z = c
				for i in range(self.__max_iterations):
					z = z * z + c
					if abs(z) > 2.0:
						break
				if abs(z.real) > self.__max_abs_x:
					self.__max_abs_x = abs(z.real)
				if abs(z.imag) > self.__max_abs_y:
					self.__max_abs_y = abs(z.imag)
				if abs(z) > self.__max_abs_z:
					self.__max_abs_z = abs(z)

	def generate(self):
		print('Generating {}, please wait...'.format(self.__name))
		image = Image.new('RGB', (self.__img_x, self.__img_y))
		pixels = image.load()
		self.__find_max_values()
		for ky in range(self.__img_y):
			b = ky * (self.__yb - self.__ya) / (self.__img_y - 1) + self.__ya
			for kx in range(self.__img_x):
				a = kx * (self.__xb - self.__xa) / (self.__img_x - 1) + self.__xa
				c = complex(a, b)
				z = c
				for i in range(self.__max_iterations):
					z = z * z + c
					if abs(z) > 2.0:
						break
				v0 = int(255 * abs(z.real) / self.__max_abs_x)
				v1 = int(255 * abs(z.imag) / self.__max_abs_y)
				v2 = int(255 * abs(z) / self.__max_abs_z)
				v3 = int(255 * abs(math.atan2(z.imag, z.real)) / math.pi)
				v = v3 * 256 ** 3 + v2 * 256 ** 2 + v1 * 256 + v0
				color__r_g_b = int(16777215 * v / 256 ** 4)
				red = int(color__r_g_b / 65536)
				green = int(color__r_g_b / 256) % 256
				blue = color__r_g_b % 256
				# red = (color__r_g_b % 8) * 32
				# green = (16 - color__r_g_b % 16) * 16
				# blue = (color__r_g_b % 16) * 16
				pixels[kx, ky] = (red, green, blue)
		image.save(self.__name, 'PNG')
		return self.__name
