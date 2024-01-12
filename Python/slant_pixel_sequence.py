colors = ["R", "G", "B", "Y"]


def mean(*colors):
    st = ""
    for c in colors:
        if c:
            st += c + "|"
    return st[:-1]


# Originally made by Ansh Dadwal
# 12 Jan 2024, 1:22PM
# Visual representation: https://imgur.com/5Nah3ze


def get_slant_pixel_map(colors):
    len_colors = len(colors)
    color_map = [None] * (len_colors**2)
    current_pixel = 0
    for color in range(len_colors):
        color_map[current_pixel] = colors[color]
        current_pixel += len_colors + 1
    slant_pixel_sequence = [
        [i, i + ((len_colors - 1) * k)]
        for k in range(1, len_colors + 1)
        for i in range(k, len_colors**2 - (len_colors * k), len_colors + 1)
    ]
    for pixel in slant_pixel_sequence:
        color_map[pixel[0]] = mean(
            color_map[pixel[0] - 1], color_map[pixel[0] + len_colors]
        )
        color_map[pixel[1]] = mean(
            color_map[pixel[1] + 1], color_map[pixel[1] - len_colors]
        )
    return color_map


result = get_slant_pixel_map(colors)
for i in range(0, len(result), len(colors)):
    print(result[i : i + len(colors)])
