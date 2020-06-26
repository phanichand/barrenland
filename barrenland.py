import ast

def pairwise(t):
    it = iter(t)
    return zip(it,it)

class Land(object):
    def __init__(self,length,breadth):
        """
        Create the matrix with a complete fertile land of x*y
        x is length
        y is breadth
        Matrix will be filled with 1s
        """
        self.length = length
        self.breadth = breadth
        self.land = self._creatematrix(length,breadth)

    def _creatematrix(self,length,breadth,value=1):
        land = [[value for x in range(breadth)] for y in range(length)]
        return land

    def create_barren_land(self,left_bottom_corner,right_top_corner):
        """
        Fill the barren land with 0
        We can calculate the coordinates with the corners that were given 

        """
        for x in range(left_bottom_corner[0],right_top_corner[0]+1):
            for y in range(left_bottom_corner[1],right_top_corner[1]+1):
                self.land[x][y] = 0

    def fill_barren_land(self,coordinates):
        for coord in coordinates:
            self.create_barren_land(coord[0],coord[1])

    def fertile_area(self):
        """
        DFS 
        Returns the area of all islands with 1s

        """
        visited = set()
        result = []
        for r0, row in enumerate(self.land):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in visited:
                    stack = [(r0, c0)]
                    visited.add((r0, c0))
                    area = 0
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < self.length and 0 <= nc < self.breadth
                                    and self.land[nr][nc] and (nr, nc) not in visited):
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                    result.append(area)
        result.sort()
        return result

def format_input(input_str):
    """
    Format the inpurt strings into a valid list 
    
    Input
    {"48 192 351 207", "48 392 351 407","120 52 135 547", "260 52 275 547"}

    Output 
    [[(48, 392), (351, 407)], [(48, 192), (351, 207)], [(120, 52), (135, 547)], [(260, 52), (275, 547)]]

    """
    input_str = ast.literal_eval(input_str)
    landcorners = []
    for point_str in input_str:
        points = []
        for x,y in pairwise(point_str.split()):
            points.append((int(x),int(y)))        
        landcorners.append(points)
    print(landcorners)
    return landcorners



if __name__ == '__main__':
    barrenland_str = input("Do input the string of coordinates \n")
    land_obj = Land(400,600)
    barrenland_coord = format_input(barrenland_str)
    
    land_obj.fill_barren_land(barrenland_coord)
    result = land_obj.fertile_area()
    print(" ".join(str(area) for area in result))       
