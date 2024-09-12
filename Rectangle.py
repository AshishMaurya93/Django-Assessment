class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Create an iterator that returns the length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 20)

# Iterate over the rectangle instance
for dimension in rect:
    print(dimension)
    
