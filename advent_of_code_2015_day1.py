# Initialise starting floor as 0
ground_floor = 0

directions = input("What are Santa's directions?")


# Loop through the characters of the directions
def floor_num(directions):
    for char in directions:
        directions.replace("(", '1') and directions.replace(")", '-1')


print(floor_num(directions))
