
from PIL import Image
from PIL import ImageDraw
from math import log, log2

# define parameters: max iterations, x-range = real axis, y-range = imaginary axis
max_iter = 100
re_start, re_end, im_start, im_end = -1.5, 0.5, -1, 1

def mandelbrot(c):
    ''' This function is used for the mandelbrot series formula'''
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1

    if n == max_iter:
        return max_iter
    
    return n + 1 - log(log2(abs(z)))

def draw_mandel(width):
    ''' This function draws the mandelbrot series and requires a pixel count as input.
    It outputs the drawn graph as a .png image.
    '''
    height = width    
    # plot an image
    im = Image.new('HSV', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, width):
        for y in range(0, height):
            # Converts pixel coordinate to complex number
            c = complex(re_start + (x / width) * (re_end - re_start),
                        im_start + (y / height) * (im_end - im_start))
            # Number of iterations is calculated
            m = mandelbrot(c)
            # Color is done based on the number of iterations
            hue = int(255 * m / max_iter)
            saturation = 255
            value = 255 if m < max_iter else 0
            # Used to plot each point
            draw.point([x, y], (hue, saturation, value))
    # Image output
    im.convert('RGB').save('output.png', 'PNG')