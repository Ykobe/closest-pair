""" Reads closest pairs input and prints the closest pair as determined by
    the point_set module.
"""

import point_set
import point_pair
import time

def main():
    num_points = int(input())
    points = []
    txt = open ("points.txt")
    
    
    for i in range(num_points):
        # read one line of input, split into x and y, convert to numbers,
        # and add to list
        line = txt.readline()
        
        coords = line.split(" ")
        x = float(coords[0])
        y = float(coords[1])
        points.append((x, y))
    
    t = time.time()
    point_pair.print_pair(point_set.closest_pair(points))
    tt = time.time() - t
    print("time taken =  "+str(tt)+ " seconds")
if __name__ == '__main__':
    main()

