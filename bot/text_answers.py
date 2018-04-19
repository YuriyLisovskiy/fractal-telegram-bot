HELP = """
___Available commands___:
/help - read current message
/bug 'description' - report a bug
/juliaset - generate Gaston Julia fractal
/lorenzattractor - generate Edvard Lorenz mathematical model of atmospheric convection
/mandelbrotset - generate Benoit Mandelbrot fractal
/quasicrystal - generate quasiperiodic crystal
"""

START = 'Welcome, {}\n. I can generate an amazing fractals.\n' + HELP + "\nIf you need help, enter /help"

INVALID_COMMAND = 'Invalid command. /help'

INVALID_INPUT = 'Invalid input. /help'

WAIT_FOR_FRACTAL = 'Generating, please wait...'

CRASHED = 'Error occurred. Repeat your command, please. /help'

THANKS_FOR_REPORT = 'Thank you for your report. /help'
