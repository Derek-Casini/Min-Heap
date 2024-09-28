# Name: Derek Casini
# OSU Email: casinid@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 5/28/2024
# Description: My implementation of a MinHeap data structure


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Add a new node to the MinHeap.

        :param node: The node to add
        :return: None
        """
        self._heap.append(node)
        self._move_up(self._heap.length() - 1)
    
    def _move_up(self, index: int) -> None:
        """
        Move a node up the heap to maintain the heap property.

        :param index: The index of the node to move
        :return: None
        """
        last = (index - 1) // 2
        if index >0 and self._heap[index] < self._heap[last]:
            self._heap[index], self._heap[last] = self._heap[last], self._heap[index]
            self._move_up(last)
        
    def is_empty(self) -> bool:
        """
        Check if the MinHeap is empty.

        :return: True if the heap is empty, False otherwise
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Get the minimum element from the heap without removing it.

        :return: The minimum element
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty!")
        
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Remove and return the minimum element from the heap.

        :return: The minimum element
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty!")
        
        min = self._heap[0]
        end = self._heap[self._heap.length() - 1]
        self._heap[0] = end
        self._heap.remove_at_index(self._heap.length() - 1)
        self._move_down(0)
        return min

    def _move_down(self, index: int) -> None:
        """
        Move a node down the heap to maintain the heap property.

        This method ensures that the subtree rooted at the given index 
        satisfies the heap property. It swaps the node at the given index 
        with its smallest child if the child is smaller, and continues 
        this process recursively.

        :param index: The index of the node to move down
        :return: None
        """
        next = 2 * index + 1
        if next >= self._heap.length():
            return
        
        right = next + 1
        if right < self._heap.length() and self._heap[right] < self._heap[next]:
            next = right
        
        if self._heap[next] < self._heap[index]:
            self._heap[next], self._heap[index] = self._heap[index], self._heap[next]
            self._move_down(next)

    def build_heap(self, da: DynamicArray) -> None:
        """
        Build the heap from an existing dynamic array.

        This method builds the heap by using the bottom-up approach.

        :param da: The dynamic array to build the heap from
        :return: None
        """
        self._heap = DynamicArray(da)
        
        start = (self._heap.length() - 2) // 2
        for i in range(start, -1, -1):
            self._move_down(i)
            

    def size(self) -> int:
        """
        Return the number of elements in the heap.

        :return: The number of elements in the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clear all elements from the heap.

        :return: None
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Perform heapsort on the given dynamic array.

    :param da: The dynamic array to sort
    :return: None
    """
    for i in range(da.length() // 2 - 1, -1, -1):
        _fix_heap(da, da.length(), i)
        
    for i in range(da.length() - 1, 0, -1):
        da[i], da[0] = da[0], da[i]
        _fix_heap(da, i, 0)

def _fix_heap(da: DynamicArray, n: int, i: int) -> None:
    """
    Ensure the subtree rooted at index i is a min-heap.
    
    :param da: The array representing the heap
    :param n: The size of the heap
    :param i: The root index of the subtree
    :return: None
    """
    lowest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and da[left] < da[lowest]:
        lowest = left
    
    if right < n and da[right] < da[lowest]:
        lowest = right
    
    if lowest != i:
        da[i], da[lowest] = da[lowest], da[i]
        _fix_heap(da, n, lowest)
    


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
