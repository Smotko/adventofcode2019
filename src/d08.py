from collections import Counter


def get_layers(image, width, height):
    layers = []
    image = image[0]
    i = 0

    while i < len(image):
        layer = []
        for k in range(height):
            for j in range(width):
                layer.append(int(image[i]))
                i += 1

        layers.append(layer)
    return layers


def solve(image, width=25, height=6):
    layers = get_layers(image, width, height)
    min_zeros = (9999, [])
    for layer in layers:
        current_zeros = sum([1 for i in layer if i == 0])
        if current_zeros < min_zeros[0]:
            min_zeros = (current_zeros, layer)
    zero_layer = min_zeros[1]
    one_digits = sum([1 for i in zero_layer if i == 2])
    two_digits = sum([1 for i in zero_layer if i == 1])
    return one_digits * two_digits


def solve2(image, width=25, height=6):
    layers = get_layers(image, width, height)
    final_layer = layers[0]

    i = 0
    for _ in range(height):
        for _ in range(width):
            l = 0
            while layers[l][i] == 2:
                l += 1
            print(l, layers[l][i])
            final_layer[i] = layers[l][i]
            print(final_layer)
            i += 1
    i = 0
    prntrs = {0: " ", 1: "*", 2: "X"}
    for _ in range(height):
        for _ in range(width):
            prnt = prntrs[final_layer[i]]
            print(prnt, end="")
            i += 1
        print("")
    return "AHFCB"
