"""
This program gives you back your picture applied with your chosen filter. You'll need to choose the picture you want
to recolour, it will show you some 25 recoloured versions of your selected picture in one run. You can choose the filter
you liked,If you don not like the filters you can rerun the program to get fresh set of recoloured picture
"""
import random
from simpleimage import SimpleImage
# the user can increase the number of recoloured files in the given set by changing N_ROWS and N_COLS values
N_ROWS = 5
N_COLS = 5
PATCH_NAME = 'images/simba-sq.jpg'
MAX = 3
MIN = 0


def main():
    list_colour = []
    image = SimpleImage(get_file())
    final_image = SimpleImage.blank(N_COLS * image.width, N_ROWS * image.height)
    # creates the patch in the two rows
    for rows in range(N_ROWS):
        # create three patches in the columns of the given row
        for cols in range(N_COLS):
            # randomly generate a real number to be used as the value of mentioned variable
            red_scale = random.uniform(MIN, MAX)
            green_scale = random.uniform(MIN, MAX)
            blue_scale = random.uniform(MIN, MAX)
            first_filter = [red_scale, green_scale, blue_scale]
            list_colour.append(first_filter)
            # create a patch in the given row and column
            patch = make_patch(final_image, cols, rows, image)
            # adds filters to the patch created
            recolored_patch = make_recolored_patch(red_scale, green_scale, blue_scale, cols, rows, patch,image)

    # shows the set of 9 different recoloured image
    recolored_patch.show()

    # ask if the user want to continue with the shown set of pictures or want to rerun the program
    ask_continue = input("Do you want to apply any of the shown filters then type 'y': ")
    if ask_continue == "y":
        # the chosen filter is applied and image is shown
        filtered_photo = user_input(image, list_colour)
        filtered_photo.show()
    else:
        print("Why don't you re-run the program and get different set of filters")





def user_input(image, list_colour):
    filename = image
    # user is asked to put the row and column number of the chosen filter
    which_filter = input("Which filter do you want to use, type in form of (row,column): ")
    for i in range(N_ROWS):
        for x in range(N_COLS):
            value = str(x+1) + "," + str(i+1)
            if which_filter == value:
                new_list = list_colour[x + (N_COLS * i)]
                red = new_list[0]
                green = new_list[1]
                blue = new_list[2]

    # the filter is applied to chosen image
    filename = recolour(red, green, blue, filename)
    # gives you a bigger picture
    resize_image = SimpleImage.blank(3 * image.width, 3 * image.height)
    filename.make_as_big_as(resize_image)
    """
    for i in range(image.width):
    resize_image.set_pixel(x, 2y, filename.get_pixel(x,y))
    resize_image.set_pixel(x, 2y+1, filename.get_pixel(x,y))
    resize_image.set_pixel(x, 2y+2, filename.get_pixel(x,y))
    """
    return filename


def get_file():
    filename = input("Please give us the file path that you want to apply the filters to: ")
    if filename == "":
        return PATCH_NAME

    return filename


def recolour(red, green, blue, filename):
    # given rgb value is applied to the image
    for pixel in filename:
        pixel.red = red * pixel.red
        pixel.green = green * pixel.green
        pixel.blue = blue * pixel.blue
    return filename


def make_patch(final_image, cols, rows, image):
    # a patch is created
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            # if write x = x + cols * patchsize, it does work but if write y = y + rows, it does not work
            # so put the values directly in the get pixel ()
            final_image.set_pixel((cols * image.width) + x, (rows * image.height) + y,  pixel)
    return final_image


def make_recolored_patch(red_scale, green_scale, blue_scale, cols, rows, patch, image):
    """
     It loads the patch image and recolors it.
     red_scale: A random number generated that multiplies to  each pixels' red component
    :param green_scale: A random number generated that multiplies to  each pixels' green component by
    :param blue_scale: A random number generated that multiplies to  each pixels' blue component
    :return: the newly generated patch
    """
    for y in range(image.height):
        for x in range(image.width):
            pixel = patch.get_pixel((cols * image.width) + x, (rows * image.height) + y)
            pixel.red = red_scale * pixel.red
            pixel.green = green_scale * pixel.green
            pixel.blue = blue_scale * pixel.blue
    return patch




if __name__ == '__main__':
    main()