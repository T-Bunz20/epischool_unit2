def to_hex(dec_num):
    final_num = ""
    while True:
        hex_num = dec_num % 16
        if hex_num > 9:
            final_num = chr(hex_num + 87) + final_num
        else:
            final_num = str(hex_num) + final_num
        if (dec_num // 16) <= 0:
            return final_num
        dec_num = dec_num // 16

def hex_code(red, green, blue):
    red = to_hex(red)
    if (len(red) == 1):
        red = "0" + red
    green = to_hex(green)
    if (len(green) == 1):
        green = "0" + green
    blue = to_hex(blue)
    if (len(blue) == 1):
        blue = "0" + blue
    return "#" + red + green + blue