#!/usr/bin/python3
"""
Square module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return string representation of the object
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        Return size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        args: id, size, x, y
        """
        if args and len(args) > 0:
            if len(args) == 1:
                self.__init__(self.size, self.x, self.y, args[0])
            elif len(args) == 2:
                self.__init__(args[1], self.x, self.y, args[0])
            elif len(args) == 3:
                self.__init__(args[1], args[2], self.y, args[0])
            elif len(args) == 4:
                self.__init__(args[1], args[2], args[3], args[0])
        else:
            if 'id' in kwargs:
                self.__init__(self.size, self.x, self.y, kwargs['id'])
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Return dictionary
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
