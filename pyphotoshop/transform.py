from image import Image
import numpy as np

def adjust_brightness(image, factor):
    # when we adjust the brightness, we just want to scale each value by some amount
    # factor is a value > 0, how much you want to brighten the image by
    # factor < 1 -> darkening
    # factor > 1 -> brightening
    x_pixels, y_pixels, num_channels = image.array.shape # get x, y pixels of image, chaneels
    # make an empty image so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # the non-vectorized way of doing it, intuitive!
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor
    # vectorized version
    new_im.array = image.array * factor

    return new_im

def adjust_contrast(image, factor, mid=0.5):
    x_pixels, y_pixels, num_channels = image.array.shape # get x, y pixels of image, chaneels
    # make an empty image so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # the non-vectorized way of doing it, intuitive!
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid
    
    # vectorized
    # new_im.array = (image.array - mid) * factor + mid

    return new_im

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 -> the neighbors left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape # get x, y pixels of image, chaneels
    # make an empty image so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(x_pixels-1, x+neighbor_range) + 1):
                    for y_i in range(max(0,y-neighbor_range), min(y_pixels-1, y+neighbor_range) + 1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size ** 2)

    return new_im

def apply_kernel(image, kernel):
    # the kernel should be a numpy 2D array that represents the kernel we'll use!
    # for the sake of simplicity of this implementation let's assume that the kernel is SQUARE
    # for example the soble x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size // 2

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(x_pixels-1, x+neighbor_range) + 1):
                    for y_i in range(max(0,y-neighbor_range), min(y_pixels-1, y+neighbor_range) + 1):
                        # we need to find which value of the kernel this corresponds to
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x, y, c] = total

    return new_im

def combine_images(image1, image2):
    x_pixels, y_pixels, num_channels = image1.array.shape # get x, y pixels of image, chaneels
    # make an empty image so we don't actually modify the original one
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image1.array[x, y, c]**2 + image2.array[x, y, c]**2)**0.5
    return new_im
        
if __name__ == "__main__":
    lake = Image(filename="lake.png")
    city = Image(filename="city.png")

    # incr_contrast = adjust_contrast(lake, 2, 0.5)
    # incr_contrast.write_image("increased_contrast_lake.png")

    # decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    # decr_contrast.write_image("decreased_contrast_lake.png")

    # blur_3 = blur(city, 3)
    # blur_3.write_image("blur_k3.png")

    # blur_15 = blur(city, 15)
    # blur_15.write_image("blur_k15.png")

    # let's apply a sobel edge detection kernel on the x and y axis
    sobel_x_kernel = np.array([
        [1, 2, 1], 
        [0, 0, 0], 
        [-1, -2, -1]
    ])
    sobel_y_kernel = np.array([
        [1, 0, -1], 
        [2, 0, -2], 
        [1, 0, -1]
    ])

    sobel_x = apply_kernel(city, sobel_x_kernel)
    # sobel_x.write_image("edge_x.png")
    sobel_y = apply_kernel(city, sobel_y_kernel)
    # sobel_y.write_image("edge_y.png")

    sobel_xy = combine_images(sobel_x, sobel_y)
    sobel_xy.write_image("sobel_xy.png")