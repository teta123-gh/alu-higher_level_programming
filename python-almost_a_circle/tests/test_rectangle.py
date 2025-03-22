#!/usr/bin/python3
"""
Test Rectangle class
"""
import os
import sys
import unittest
from io import StringIO

from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_rect_with_2(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rect_with_3(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_rect_with_4(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)


# @unittest.skip
class RectangleTestErrors(unittest.TestCase):

    def test_rect_type_errors_1(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rect_type_errors_2(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_rect_type_errors_3(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_rect_type_errors_4(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    # def test_rect_with_5_args(self):
    #     with self.assertRaises(TypeError):
    #         r = Rectangle(1, 2, 3, 4, 5)

    def test_rect_value_errors_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_rect_value_errors_2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_rect_value_errors_3(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_rect_value_errors_4(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_rect_value_errors_5(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_rect_value_errors_6(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rectangle_str_representation(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display(self):
        r1 = Rectangle(2, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__

        expected_output = "##\n##\n##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_display_with_x(self):
        r2 = Rectangle(3, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__

        expected_output = " ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_display_with_x_and_y(self):
        r3 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r3.display()
        sys.stdout = sys.__stdout__

        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


class TestRectangleAdditional(unittest.TestCase):
    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 89)
        expected = {'id': 89, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] ({}) 10/10 - 10/10".format(r.id))

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")

    def test_update_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")

    def test_update_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwargs_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3)
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 1/2")

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            from json import loads
            loaded = loads(f.read())
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0]['width'], 1)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])

    def test_load_from_file_exists(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(str(list_rectangles_output[0]), str(r1))
        self.assertEqual(str(list_rectangles_output[1]), str(r2))
        os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
