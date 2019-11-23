# Given two ordered pairs calculate the distance between them. Round to two decimal places.
# This should be easy to do in 0(1) timing.
import math
def distance(x1, y1, x2, y2):
    # dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) #calculate the distance between two ordered pairs

    # Round to two decimal places.
    dist = round((math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)),2)

    return (dist)

print(distance(1,2,3,4))

