# Mandelbrot set
from PIL import Image

def mandelbrot_set(x_bounds:tuple, y_bounds:tuple, image_size:tuple, max_iterations:int):
    """Returns an image of the Mandelbrot Set based on the given parameters
    Args:
        x_bounds (tuple (float,float)) : min and max for x (inclusive)
        y_bounds (tuple (float,float)) : min and max for y (inclusive)
        image_size (tuple (int,int)) : x and y size of returned image in pixels
        max_iterations (int) : Max iterations of the mandelbrot function.
    Returns:
        image (PIL image) : Image of the Mandelbrot Set
    """
    def mandelbrot_function(c): #Returns status of an imaginary points based on the mandelbrot function.
        z = c
        iteration = 0
        while (abs(z) <= 2 and iteration < max_iterations):
            z = z**2+c
            iteration+=1
        return(iteration==max_iterations)

    image = Image.new(mode='RGB', size=image_size)
    total_pixels = image_size[0]*image_size[1]
    current_pixel = 0
    for pixel_x in range(image_size[0]):
        for pixel_y in range(image_size[1]):
            current_pixel+=1
            percent_done = current_pixel/total_pixels
            if current_pixel%(total_pixels//1000) == 0:
               print(percent_done)
                        
            cx = ((x_bounds[1]-x_bounds[0])/(image_size[0] - 1)) * (pixel_x) + x_bounds[0]
            cy = ((y_bounds[1]-y_bounds[0])/(image_size[1] - 1)) * (pixel_y) + y_bounds[0]
            c = cx + cy*1j # turn it into an imaginary number
            pixel_color = (0,0,0)
            if mandelbrot_function(c): # If c remains bounded
                pixel_color = (128,128,255)
            image.putpixel((pixel_x,pixel_y),pixel_color)

    return(image)