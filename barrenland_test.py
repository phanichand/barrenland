import unittest
from barrenland import Land

class Testland(unittest.TestCase):
    
    def testLandinit(self):
        length = 400
        breadth = 600
        land_obj = Land(length,breadth)
        land_length = len(land_obj.land)
        land_breadth = len(land_obj.land[0])
        self.assertEqual(land_length,length)
        self.assertEqual(land_breadth,breadth)
        

    def test_create_barren_land(self):
        length = 4
        breadth = 6
        left_bot_corner = (0,0)
        right_top_corner = (3,2)
        land_obj = Land(length,breadth)
        land_obj.create_barren_land(left_bot_corner,right_top_corner)
        self.assertEqual(land_obj.land[left_bot_corner[0]][left_bot_corner[1]],0)
        self.assertEqual(land_obj.land[right_top_corner[0]][right_top_corner[1]],0)
        self.assertEqual(land_obj.land[right_top_corner[0]][left_bot_corner[1]],0)
        self.assertEqual(land_obj.land[left_bot_corner[0]][right_top_corner[1]],0)

    def test_fill_barren_land(self):
        length = 4
        breadth = 6
        coordinates = [((0,0),(3,2))]
        land_obj = Land(length,breadth)
        land_obj.fill_barren_land(coordinates)
        coordinates = coordinates[0]
        self.assertEqual(land_obj.land[coordinates[0][0]][coordinates[0][1]],0)
        self.assertEqual(land_obj.land[coordinates[1][0]][coordinates[1][1]],0)
        self.assertEqual(land_obj.land[coordinates[1][0]][coordinates[0][1]],0)
        self.assertEqual(land_obj.land[coordinates[0][0]][coordinates[1][1]],0)

    def test_zero_fertile_land(self):
        length = 4
        breadth = 6
        left_bot_corner = (0,0)
        right_top_corner = (3,5)
        land_obj = Land(length,breadth)
        land_obj.create_barren_land(left_bot_corner,right_top_corner)
        result = land_obj.fertile_area()
        self.assertEqual(land_obj.fertile_area(),[])

    
    def test_complete_fertile_land(self):
        length = 4 
        breadth = 6
        land_obj = Land(length,breadth) 
        result = land_obj.fertile_area() 
        self.assertEqual(land_obj.fertile_area(),[24])  
