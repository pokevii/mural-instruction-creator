import imageio.v3 as iio
import importlib
import color
util = importlib.import_module("mural-util")

img = iio.imread("Mural 1x (320x320).png")
max_x = img.shape[0]
max_y = img.shape[1]

grid_x = 32
grid_y = 32
grid_pos = [0, 0]

rows = int(max_x / grid_x)
cols = int(max_y / grid_y)

currentColorCount = [0] * 45
finalColorCount = [0] * 45


for i in range(rows):
    for j in range(cols):
        for x in range(grid_x):
            for y in range(grid_y):
                # Get the current pixel and match the RGB values to ones known in the Color enumeration
                # Store colors in the currentColorCount array
                pix = img[x+(i*32), y+(j*32)]
                value = color.find_color(pix)
                if value == color.Color.NO_MATCH:
                    print("No match found at (" + str(y+(j*32)) + ", " + str(x+(i*32)) + ") | " + str(pix))
                currentColorCount[value] += 1

        # Save image
        filename = chr(65 + grid_pos[1]) + str(grid_pos[0])
        util.create_image(filename, currentColorCount)
        print(filename + " completed.")

        # Add colors to Final Color Count, reset the current count.
        index = 0
        for value in finalColorCount:
            finalColorCount[index] += currentColorCount[index]
            index += 1
        currentColorCount = [0] * 45

        # Move the grid position
        grid_pos[0] += 1

    grid_pos[0] = 0
    grid_pos[1] += 1

index = 0
for i in finalColorCount:
    # print(color.Color(index).name + ": " + str(finalColorCount[index]))
    index += 1
