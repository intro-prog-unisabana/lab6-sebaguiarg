# Write your code here!

def temp_and_color(dict):
    temp = dict.get("temp")
    color = dict.get("color")
    return temp, color
print(temp_and_color)

dict = {}
result = temp_and_color(dict)
print(result)