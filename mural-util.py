from PIL import Image, ImageFont, ImageDraw
import color


debug = True
save = True


def create_color_icon(c, qty, small):
    # Set variables and get info
    rgb = color.get_color_rgba(c)
    rgb = tuple(rgb)
    color_name = color.get_color_name(c)
    color_name = str(color_name)
    color_box_outline = Image.open("images/box outline.png")

    # Prepare images and their coordinates
    # If there are a lot of instructions, we'll need to shrink them down:
    if small:
        qty_pos = (8, 9)
        text_pos = (55, 9)
        if qty <= 9:
            qty_pos = (15, 9)
        elif qty >= 100:
            qty_pos = (1, 9)
        image = Image.new(mode="RGBA", size=(400, 45), color="white")
        color_box = Image.new(mode="RGBA", size=(45, 45), color=rgb)
        color_box_outline = color_box_outline.resize((45, 45))
        font = ImageFont.truetype("System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf", 38)

    # Otherwise, we keep them large.
    else:
        qty_pos = (14, 16)
        text_pos = (70, 16)
        if qty <= 9:
            qty_pos = (22, 16)
        elif qty >= 100:
            qty_pos = (5, 16)
        image = Image.new(mode="RGBA", size=(400, 65), color="white")
        color_box = Image.new(mode="RGBA", size=(65, 65), color=rgb)
        color_box_outline = color_box_outline.resize((65, 65))
        font = ImageFont.truetype("System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf", 46)

    # Begin drawing
    draw = ImageDraw.Draw(image)
    # Special exception for white (can't draw white-on-white)
    if c == "WHITE":
        image.paste(color_box_outline, (0, 0))
        draw.text(qty_pos, str(qty), fill="black", font=font, align="center")
        draw.text(text_pos, color_name, fill="black", font=font, align="left")
        return image
    else:
        image.paste(color_box, (0, 0))
        draw.text(qty_pos, str(qty), fill="white", font=font, align="center")
        draw.text(text_pos, color_name, fill=rgb, font=font, align="left")
        return image


def create_instructions(image, cc):
    return image


def create_image(fn, cc):

    # Prepare images to be composited
    grid = Image.open("images/grid/" + fn + ".png")
    grid = grid.resize((967, 967))
    line = Image.open("images/black.png")
    line = line.resize((2000, 6))

    # Composite image by pasting images over white bg
    image = Image.new(mode="RGB", size=(993, 1404), color=(255, 255, 255))
    image.paste(grid, (11, 14))
    image.paste(line, (-10, 1040))

    # Put grid name on it
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("System/Library/Fonts/Supplemental/Charter.ttc", 62)
    text = fn + " - "
    draw.text((22, 970), text, fill="black", font=font, align="left")

    # Prepare the instruction loop
    index = 0
    color_count = 0
    total_colors = 0
    inst_index = [0, 0]

    # Get color count first
    for c in cc:
        color_name = color.Color(index).name
        if cc[index] > 0:
            if color_name != "EMPTY":
                color_count += 1
        index += 1

    index = 0
    # Now create instructions
    for c in cc:
        color_name = color.Color(index).name
        if cc[index] > 0:
            if color_name != "EMPTY":
                total_colors += c
                if color_count > 15:
                    instruction = create_color_icon(color_name, c, True)
                    image.paste(instruction, (5 + (275 * inst_index[1]), 1050 + (50 * inst_index[0])))
                    inst_index[0] += 1
                    if inst_index[0] > 6:
                        inst_index[0] = 0
                        inst_index[1] += 1
                else:
                    instruction = create_color_icon(color_name, c, False)
                    image.paste(instruction, (5 + (350 * inst_index[1]), 1050 + (70 * inst_index[0])))
                    inst_index[0] += 1
                    if inst_index[0] > 4:
                        inst_index[0] = 0
                        inst_index[1] += 1
        index += 1

    # Debug stuff (shows more info on image)
    if debug:
        debug_font = ImageFont.truetype("System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf", 30)
        draw.text(
            (720, 1000),
            "TOTAL: " + str(total_colors) + "  |  " + str(color_count) + " COLORS",
            fill="black",
            font=debug_font,
            align="left"
        )
        image.show()
        if save:
            image.save("out/" + fn + ".png")
        return

    image.show()
    if save:
        image.save("out/" + fn + ".png")

