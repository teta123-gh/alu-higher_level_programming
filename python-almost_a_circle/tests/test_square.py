#!/usr/bin/python3
"""
Test Square class
"""
import os
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

    def test_square_creation_with_string_input(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    # def test_square_creation_with_extra_args(self):
    #     with self.assertRaises(TypeError):
    #         Square(1, 2, 3, 4)

    def test_square_negative_input(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_input(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_str_representation(self):
        s = Square(5, 1, 2, 89)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 5")

    def test_dictionary_method(self):
        s = Square(5, 1, 2, 89)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 89, "size": 5, "x": 1, "y": 2})

    def test_update_method(self):
        s = Square(5, 0, 0, 1)
        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

        s.update(89, 1, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_kwargs(self):
        s = Square(5)
        s.update(id=89)
        self.assertEqual(s.id, 89)

        s.update(id=89, size=1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

        s.update(id=89, size=1, x=2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_class_create_method(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 1)

        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s3.id, 89)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)

        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s4.id, 89)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)

    def test_save_to_file(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists('Square.json'))
        os.remove('Square.json')

        Square.save_to_file([])
        self.assertTrue(os.path.exists('Square.json'))
        os.remove('Square.json')

        s = Square(1)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists('Square.json'))
        os.remove('Square.json')

    def test_load_from_file(self):
        # When file doesn't exist
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

        # When file exists
        s = Square(1, 2, 3, 89)
        Square.save_to_file([s])
        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 1)
        self.assertEqual(loaded_squares[0].id, 89)
        self.assertEqual(loaded_squares[0].size, 1)
        self.assertEqual(loaded_squares[0].x, 2)
        self.assertEqual(loaded_squares[0].y, 3)
        os.remove('Square.json')


if __name__ == '__main__':
    unittest.main()
