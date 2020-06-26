#Problem Statement

You have a farm of 400m by 600m where coordinates of the field are from (0, 0) to (399,599). A portion of the farm is barren, and all the barren land is in the form of rectangles.
Due to these rectangles of barren land, the remaining area of fertile land is in noparticular shape. An area of fertile land is defined as the largest area of land that is not covered by any of the rectangles of barren land.

Read input from STDIN. Print output to STDOUT

##Input
You are given a set of rectangles that contain the barren land. These rectangles are 
defined in a string, which consists of four integers separated by single spaces, with no
additional spaces in the string. The first two integers are the coordinates of the bottom
left corner in the given rectangle, and the last two integers are the coordinates of the 
top right corner.
##Output

Output all the fertile land area in square meters, sorted from smallest area to greatest,
separated by a space.

#Requirements
python3.7


##Unitests:

python -m unittest barrenland_test


##To Test the problem

Type 

python barrenland.py

{"48 192 351 207", "48 392 351 407","120 52 135 547", "260 52 275 547"}