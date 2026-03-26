# Write your code here!

dict = {}
def temp_and_color(dict):
    if "temp" not in dict:
        print("None")
    else:
        print(dict["temp"])

    if "color" not in dict:
        print("None")
    else:
        print(dict["color"])
    return temp_and_color

print(tuple(temp_and_color))
