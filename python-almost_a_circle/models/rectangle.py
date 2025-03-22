
#!/usr/bin/python3
"""
Rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, w):
        """
        Setter for width
        """
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, h):
        """
        Setter for height
        """
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter for x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter for y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Calculate area
        """
        return self.__width * self.__height

    def display(self):
        """
        Display rectangle
        """
        print("\n" * self.__y + '\n'.join(
            " " * self.__x +
            "#" * self.__width for _ in range(self.__height))
              )

    def __str__(self):
        """
        String representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        args: id, width, height, x, y
        """
        if args and len(args) > 0:
            # self.__init__(args[1], args[2], args[3], args[4], args[0])
            if len(args) == 1:
                self.__init__(self.__width, self.__height,
                              self.__x, self.__y, args[0])
            elif len(args) == 2:
                self.__init__(args[1], self.__height,
                              self.__x, self.__y, args[0])
            elif len(args) == 3:
                self.__init__(args[1], args[2], self.__x, self.__y, args[0])
            elif len(args) == 4:
                self.__init__(args[1], args[2], args[3], self.__y, args[0])
            elif len(args) == 5:
                self.__init__(args[1], args[2], args[3], args[4], args[0])

        else:
            if 'id' in kwargs:
                self.__init__(self.__width, self.__height,
                              self.__x, self.__y, kwargs['id'])
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
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
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
