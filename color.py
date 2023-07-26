from enum import IntEnum
import numpy as np

color_values = [
    [[219, 196, 171, 255],  ["Empty"]],   # EMPTY
    [[255, 255, 255, 255],  ["White"]],  # WHITE
    [[230, 206, 156, 255],  ["Brick Yellow"]],   # BRICK YELLOW
    [[205, 24, 8, 255],     ["Red"]],      # RED
    [[0, 85, 189, 255],     ["Blue"]],      # BLUE
    [[246, 206, 49, 255],   ["Yellow"]],    # YELLOW
    [[0, 16, 24, 255],      ["Black"]],      # BLACK
    [[32, 121, 64, 255],    ["Dark Green"]],     # DARK GREEN
    [[49, 149, 106, 255],   ["Green"]],    # GREEN
    [[164, 85, 0, 255],     ["Dark Orange"]],      # DARK ORANGE
    [[90, 145, 222, 255],   ["Medium Blue"]],    # MEDIUM BLUE
    [[255, 137, 24, 255],   ["Bright Orange"]],    # BRIGHT ORANGE
    [[189, 234, 8, 255],    ["Yellowish Green"]],     # YELLOWISH GREEN
    [[148, 56, 115, 255],   ["Reddish Violet"]],  # REDDISH VIOLET
    [[115, 129, 156, 255],  ["Sand Blue"]],   # SAND BLUE
    [[148, 137, 115, 255],  ["Sand Yellow"]],  # SAND YELLOW
    [[8, 52, 98, 255],      ["Earth Blue"]],      # EARTH BLUE
    [[49, 60, 57, 255],     ["Earth Green"]],      # EARTH GREEN
    [[106, 141, 124, 255],  ["Sand Green"]],   # SAND GREEN
    [[115, 12, 16, 255],    ["Dark Red"]],     # DARK RED
    [[255, 186, 57, 255],   ["Yellowish Orange"]],    # YELLOWISH ORANGE
    [[90, 40, 16, 255],     ["Reddish Brown"]],      # REDDISH BROWN
    [[164, 165, 172, 255],  ["Grey"]],   # GREY
    [[106, 109, 106, 255],  ["Dark Grey"]],   # DARK GREY
    [[106, 194, 230, 255],  ["Light Blue"]],   # LIGHT BLUE
    [[205, 113, 164, 255],  ["Bright Purple"]],   # BRIGHT PURPLE
    [[230, 174, 205, 255],  ["Light Purple"]],   # LIGHT PURPLE
    [[255, 238, 106, 255],  ["Cool Yellow"]],   # COOL YELLOW
    [[65, 24, 148, 255],    ["Lilac"]],     # LILAC
    [[246, 214, 180, 255],  ["Light Nougat"]],   # LIGHT NOUGAT
    [[57, 32, 0, 255],      ["Dark Brown"]],       # DARK BROWN
    [[172, 125, 82, 255],   ["Med. Nougat"]],    # MEDIUM NOUGAT
    [[0, 137, 205, 255],    ["Dark Azure"]],     # DARK AZURE
    [[106, 194, 230, 255],  ["Medium Azure"]],   # MEDIUM AZURE
    [[213, 242, 238, 255],  ["Aqua"]],   # AQUA
    [[172, 117, 189, 255],  ["Med. Lavender"]],   # MEDIUM LAVENDER
    [[230, 214, 238, 255],  ["Lavender"]],   # LAVENDER
    [[222, 238, 164, 255],  ["Spring Green"]],   # SPRING GREEN
    [[156, 153, 90, 255],   ["Olive Green"]],    # OLIVE GREEN
    [[0, 141, 156, 255],    ["Dark Turquoise"]],     # DARK TURQUOISE
    [[255, 109, 90, 255],   ["Coral"]]    # CORAL
]


def get_color_rgba(name):
    for i in range(len(Color)):
        if Color(i).name == name:
            return color_values[i][0]
    print("Invalid argument when calling get_color_rgba: " + str(name))
    return [0, 0, 0, 0]


def get_color_name(name):
    for i in range(len(Color)):
        if Color(i).name == name:
            color_to_return = str(color_values[i][1])
            color_to_return = color_to_return.replace("['", "")
            color_to_return = color_to_return.replace("']", "")
            return color_to_return
    print("Invalid argument when calling get_color_rgba: " + str(name))
    return "!! ERROR !!"


def find_color(pixel):
    p = np.array(pixel)

    for i in range(len(color_values)):
        if np.array_equal(p, color_values[i][0]):
            return Color(i)

    return Color.NO_MATCH


def find_color_old(pixel):
    p = np.array(pixel)

    if np.array_equal(p, [219, 196, 171, 255]):
        return Color.EMPTY
    elif np.array_equal(p, [255, 255, 255, 255]):
        return Color.WHITE
    elif np.array_equal(p, [230, 206, 156, 255]):
        return Color.BRICK_YELLOW
    elif np.array_equal(p, [205, 24, 8, 255]):
        return Color.RED
    elif np.array_equal(p, [0, 85, 189, 255]):
        return Color.BLUE
    elif np.array_equal(p, [246, 206, 49, 255]):
        return Color.YELLOW
    elif np.array_equal(p, [0, 16, 24, 255]):
        return Color.BLACK
    elif np.array_equal(p, [32, 121, 64, 255]):
        return Color.DARK_GREEN
    elif np.array_equal(p, [49, 149, 106, 255]):
        return Color.GREEN
    elif np.array_equal(p, [164, 85, 0, 255]):
        return Color.DARK_ORANGE
    elif np.array_equal(p, [90, 145, 222, 255]):
        return Color.MEDIUM_BLUE
    elif np.array_equal(p, [255, 137, 24, 255]):
        return Color.BRIGHT_ORANGE
    elif np.array_equal(p, [189, 234, 8, 255]):
        return Color.YELLOWISH_GREEN
    elif np.array_equal(p, [148, 56, 115, 255]):
        return Color.REDDISH_VIOLET
    elif np.array_equal(p, [115, 129, 156, 255]):
        return Color.SAND_BLUE
    elif np.array_equal(p, [148, 137, 115, 255]):
        return Color.SAND_YELLOW
    elif np.array_equal(p, [8, 52, 98, 255]):
        return Color.EARTH_BLUE
    elif np.array_equal(p, [49, 60, 57, 255]):
        return Color.EARTH_GREEN
    elif np.array_equal(p, [106, 141, 124, 255]):
        return Color.SAND_GREEN
    elif np.array_equal(p, [115, 12, 16, 255]):
        return Color.DARK_RED
    elif np.array_equal(p, [255, 186, 57, 255]):
        return Color.YELLOWISH_ORANGE
    elif np.array_equal(p, [90, 40, 16, 255]):
        return Color.REDDISH_BROWN
    elif np.array_equal(p, [164, 165, 172, 255]):
        return Color.GREY
    elif np.array_equal(p, [106, 109, 106, 255]):
        return Color.DARK_GREY
    # elif np.array_equal(p, [106, 194, 230, 255]):
    #     return Color.LIGHT_BLUE
    elif np.array_equal(p, [205, 113, 164, 255]):
        return Color.BRIGHT_PURPLE
    elif np.array_equal(p, [230, 174, 205, 255]):
        return Color.LIGHT_PURPLE
    elif np.array_equal(p, [255, 238, 106, 255]):
        return Color.COOL_YELLOW
    elif np.array_equal(p, [65, 24, 148, 255]):
        return Color.LILAC
    elif np.array_equal(p, [246, 214, 180, 255]):
        return Color.LIGHT_NOUGAT
    elif np.array_equal(p, [57, 32, 0, 255]):
        return Color.DARK_BROWN
    elif np.array_equal(p, [172, 125, 82, 255]):
        return Color.MEDIUM_NOUGAT
    elif np.array_equal(p, [0, 137, 205, 255]):
        return Color.DARK_AZURE
    elif np.array_equal(p, [106, 194, 230, 255]):
        return Color.MEDIUM_AZURE
    elif np.array_equal(p, [213, 242, 238, 255]):
        return Color.AQUA
    elif np.array_equal(p, [172, 117, 189, 255]):
        return Color.MEDIUM_LAVENDER
    elif np.array_equal(p, [230, 214, 238, 255]):
        return Color.LAVENDER
    elif np.array_equal(p, [222, 238, 164, 255]):
        return Color.SPRING_GREEN
    elif np.array_equal(p, [156, 153, 90, 255]):
        return Color.OLIVE_GREEN
    elif np.array_equal(p, [0, 141, 156, 255]):
        return Color.DARK_TURQUOISE
    elif np.array_equal(p, [255, 109, 90, 255]):
        return Color.CORAL
    else:
        return Color.NO_MATCH


class Color(IntEnum):
    EMPTY = 0
    WHITE = 1
    BRICK_YELLOW = 2
    RED = 3
    BLUE = 4
    YELLOW = 5
    BLACK = 6
    DARK_GREEN = 7
    GREEN = 8
    DARK_ORANGE = 9
    MEDIUM_BLUE = 10
    BRIGHT_ORANGE = 11
    YELLOWISH_GREEN = 12
    REDDISH_VIOLET = 13
    SAND_BLUE = 14
    SAND_YELLOW = 15
    EARTH_BLUE = 16
    EARTH_GREEN = 17
    SAND_GREEN = 18
    DARK_RED = 19
    YELLOWISH_ORANGE = 20
    REDDISH_BROWN = 21
    GREY = 22
    DARK_GREY = 23
    LIGHT_BLUE = 24
    BRIGHT_PURPLE = 25
    LIGHT_PURPLE = 26
    COOL_YELLOW = 27
    LILAC = 28
    LIGHT_NOUGAT = 29
    DARK_BROWN = 30
    MEDIUM_NOUGAT = 31
    DARK_AZURE = 32
    MEDIUM_AZURE = 33
    AQUA = 34
    MEDIUM_LAVENDER = 35
    LAVENDER = 36
    SPRING_GREEN = 37
    OLIVE_GREEN = 38
    PEARL_GOLD = 39
    SILVER_METALLIC = 40
    PEARL_DARK_GREY = 41
    DARK_TURQUOISE = 42
    CORAL = 43
    NO_MATCH = 44
