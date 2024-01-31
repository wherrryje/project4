class Box:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def volume(self):
        """
        returns the volume of an object of class Box by multiplying length, width,
        height.
        """
        return self._length * self._width * self._height

def box_sort(box_list):
    """
    takes a list of box objects and sorts them (greatest to least) by utilizing volume method.
    """
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1
        while pos >= 0 and box_list[pos].volume() < value.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = value

# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
# box_list = [b1, b2, b3]
# box_sort(box_list)

for box in box_list:
    print(box.volume())