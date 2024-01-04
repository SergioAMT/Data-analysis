class Rectangle:
    # area = 0
    
    def __init__(self, height, width):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_height(self, height):
        self.height = height
    
    def set_widht(self, width):
        self.width = width
        
    def get_area(self):
        # self.area = self.width*self.height
        # print(self.area)
        print(self.width * self.height)
    
    def get_perimeter(self):
        print((2* self.width) + (2 * self.height))
    
    def get_diagonal(self):
        print(((self.width ** 2) + (self.height ** 2)) ** .5)
    
    def get_picture(self):
        # if (self.height > 49) | (self.width > 50):
        #     print('Too big for picture')
        # else:
        #     for h in range (self.height):
        #         print('*' * self.width + '\n')
        
        if(self.width > 50 or self.height > 50):
            return 'Too big for picture'
        string = (('*' * self.width) + '\n') * self.height
        print(string)
        
    def get_amount_inside(self, shape):
        print((self.get_area() / shape.get_area()))
        
class Square(Rectangle):
    
    def __init__(self, side):
        self.height = side
        self.width = side 
    
    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side
        
    
    