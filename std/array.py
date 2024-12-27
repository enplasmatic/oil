class array:
    def __init__(self, size, default_value=None):
        """
        Initialize an array with a fixed size.
        
        :param size: The number of elements in the array.
        :param default_value: The default value for each element in the array.
        """
        if size < 0:
            raise ValueError("Size must be non-negative")
        self._size = size
        self._data = [default_value] * size
        self._category = {}

    def __getitem__(self, index):
        """
        Get an item from the array.
        
        :param index: Index of the item.
        :return: The value at the specified index.
        """
        self._check_index(index)
        return self._data[index]

    def __setitem__(self, index, value):
        """
        Set an item in the array.
        
        :param index: Index to set the value at.
        :param value: The value to set.
        """
        self._check_index(index)
        self._data[index] = value
        self._setcat(value)

    def __len__(self):
        """
        Get the size of the array.
        
        :return: The number of elements in the array.
        """
        return self._size

    def _check_index(self, index):
        """
        Check if the index is within bounds.
        
        :param index: Index to check.
        """
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        
    def __in__(self, value):
        return (value in self._category)
    
    def _setcat(self, value):
        if not (value in self._category):
            self._category[value] = 1

    def __str__(self):
        """
        Return a string representation of the array.
        
        :return: String representation of the array.
        """
        return f"{self._data}"