# Name: Derek Casini
# OSU Email: Casinid@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 4/30/2024
# Description: An array which handles memory management itself


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------
    # Name: resize
    #
    # Resizes the capacity of a dynamic array
    #
    # Preconditions: Initialized self
    #
    # Postconditions: None
    #
    # Recieves: Self, capacity to change to
    #
    # Returns: Nothing
    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        if (new_capacity > 0) and (new_capacity >= self._size):
            temp = self._data
            self._data = StaticArray(new_capacity)
            if new_capacity > self._capacity:
                for i in range(temp.length()):
                    self._data[i] = temp[i]
            else:
                for i in range(new_capacity):
                    self._data[i] = temp[i]
            self._capacity = new_capacity

    # -----------------------------------------------------------------------
    # Name: append
    #
    # Adds an item onto the end of the dynamic array
    #
    # Preconditions: Initialized self
    #
    # Postconditions: New item at end, size is one larger
    #
    # Recieves: Self, value to add
    #
    # Returns: Nothing
    # -----------------------------------------------------------------------

    def append(self, value: object) -> None:
        if self._capacity == self._size:
            self.resize(self._capacity * 2)

        self._data[self._size] = value
        self._size += 1

    # -----------------------------------------------------------------------
    # Name: insert_at_index
    #
    # Puts an item at a specified index and moves all indexes on the right
    # over one.
    #
    # Preconditions: Initialized self, index in range of [0, _size]
    #
    # Postconditions: Size increases by one
    #
    # Recieves: Self, index to change, value to change to
    #
    # Returns: Nothing
    # -----------------------------------------------------------------------

    def insert_at_index(self, index: int, value: object) -> None:
        if (index >= 0) and (index <= self._size):
            if self._capacity == self._size:
                self.resize(self._capacity * 2)
            
            temp = self._data
            self._data = StaticArray(self._capacity)
            for i in range(index):
                self._data[i] = temp[i]

            self._data[index] = value
            for i in range(index, self._size):
                self._data[i + 1] = temp[i]
            self._size += 1
        else:
            raise DynamicArrayException('Index out of bounds')

    # -----------------------------------------------------------------------
    # Name: remove_at_index
    #
    # Removes the item at a specified index and moves all items after it down
    #
    # Preconditions: Initialized self, index in range [0, _size - 1]
    #
    # Postconditions: Size is one less
    #
    # Recieves: Self, index to remove
    #
    # Returns: Nothing
    # -----------------------------------------------------------------------

    def remove_at_index(self, index: int) -> None:
        if (index >= 0) and (index <= self._size - 1):
            if (self._size < self._capacity / 4) and (self._capacity / 2 > 10):
                self.resize(self._size * 2)
            elif (self._size < self._capacity / 4) and (self._size > 1):
                self.resize(10)

            temp = self._data
            self._data = StaticArray(self._capacity)
            for i in range(index):
                self._data[i] = temp[i]

            for i in range(index + 1, self._size):
                self._data[i - 1] = temp[i]

            self._size -= 1
        else:
            raise DynamicArrayException('Index out of bounds')

    # -----------------------------------------------------------------------
    # Name: slice
    #
    # Returns a new DynamicArray slice from start_index to start_index + size - 1
    #
    # Preconditions: Initialized self, valid start_index and size within bounds
    #
    # Postconditions: New DynamicArray slice returned
    #
    # Receives: Self, start_index, size
    #
    # Returns: DynamicArray slice
    # -----------------------------------------------------------------------

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        if (start_index >= 0) and (start_index <= self._size - 1) and (size >= 0) and ((size + start_index) <= self._size):
            new = DynamicArray()
            for i in range(size):
                new.append(self._data[start_index + i])
            
            return new
        else:
            raise DynamicArrayException('Index out of bounds')

    # -----------------------------------------------------------------------
    # Name: map
    #
    # Returns a new DynamicArray with each element transformed by map_func
    #
    # Preconditions: Initialized self
    #
    # Postconditions: New DynamicArray mapped with map_func
    #
    # Receives: Self, map_func
    #
    # Returns: Mapped DynamicArray
    # -----------------------------------------------------------------------

    def map(self, map_func) -> "DynamicArray":
        new = DynamicArray()
        for i in range(self._size):
            new.append(map_func(self._data[i]))

        return new
    
    # -----------------------------------------------------------------------
    # Name: filter
    #
    # Returns a new DynamicArray containing elements filtered by filter_func
    #
    # Preconditions: Initialized self
    #
    # Postconditions: New DynamicArray filtered by filter_func
    #
    # Receives: Self, filter_func
    #
    # Returns: Filtered DynamicArray
    # -----------------------------------------------------------------------

    def filter(self, filter_func) -> "DynamicArray":
        new = DynamicArray()
        for i in range(self._size):
            if(filter_func(self._data[i])):
                new.append(self._data[i])

        return new

    # -----------------------------------------------------------------------
    # Name: reduce
    #
    # Reduces the DynamicArray with reduce_func and optional initializer
    #
    # Preconditions: Initialized self
    #
    # Postconditions: Reduction result with reduce_func
    #
    # Receives: Self, reduce_func, initializer
    #
    # Returns: Reduction result
    # -----------------------------------------------------------------------

    def reduce(self, reduce_func, initializer=None) -> object:
        total = None
        if initializer:
            total = initializer
            if self._size > 0:
                for x in range(self._size ):
                    total = reduce_func(total, self._data[x])
        
        elif self._size > 0:
            total = self._data[0]
            for x in range(1, self._size):
                total = reduce_func(total, self._data[x])
        return total

# -----------------------------------------------------------------------
# Name: chunk
#
# Chunks the DynamicArray into subarrays of non-decreasing sequences
#
# Preconditions: Initialized arr DynamicArray
#
# Postconditions: DynamicArray of subarrays representing chunks
#
# Receives: arr (DynamicArray)
#
# Returns: DynamicArray of subarrays (chunks)
# -----------------------------------------------------------------------

def chunk(arr: DynamicArray) -> "DynamicArray":
    new = DynamicArray()
    temp = DynamicArray()
    indexT = 0
    for i in range(arr.length()):
        if temp.length() > 0:
            if arr[i] >= temp[indexT - 1]:
                temp.append(arr[i])
                indexT += 1
            else:
                new.append(temp)
                temp = DynamicArray()
                temp.append(arr[i])
                indexT = 1
        else:
            temp.append(arr[i])
            indexT += 1

    if temp.length() > 0:
        new.append(temp)
    return new

# -----------------------------------------------------------------------
# Name: find_mode
#
# Finds the mode(s) and frequency of occurrence in the DynamicArray
#
# Preconditions: Initialized arr DynamicArray
#
# Postconditions: Tuple of DynamicArray containing modes and their frequency
#
# Receives: arr (DynamicArray)
#
# Returns: Tuple (DynamicArray of modes, frequency)
# -----------------------------------------------------------------------

def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    mode = DynamicArray()
    freq = 0
    tempCount = 0
    tempItem = None
    for i in arr:
        if tempItem:
            if i == tempItem:
                tempCount += 1
            else:
                if tempCount == freq:
                    mode.append(tempItem)
                    freq = tempCount
                elif tempCount > freq:
                    mode = DynamicArray()
                    mode.append(tempItem)
                    freq = tempCount
                tempCount = 1
                tempItem = i
        else:
            tempItem = i
            tempCount += 1
    
    if tempCount == freq:
        mode.append(tempItem)
        freq = tempCount
    elif tempCount > freq:
        mode = DynamicArray()
        mode.append(tempItem)
        freq = tempCount

    return (mode, freq)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
