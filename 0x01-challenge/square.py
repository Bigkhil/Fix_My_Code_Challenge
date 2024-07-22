#!/usr/bin/python3
'''this is a square module'''


class square():
    '''instantiation of the square class'''
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        '''instantiation of the square class'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        '''method to print the perimeter of the square'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''method to print the representation of the class'''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    '''make an instance of the class'''
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
