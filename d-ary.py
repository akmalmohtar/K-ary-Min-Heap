class minHeap(object):
    def __init__(self, k):
        self.heap_array = []
        self.k = k
        self.heap_length = 0

    def findMinChild(self, index):
        minChild = self.heap_array[index]
        minChildIndex = -1
        i = 1
        while self.k * index + i < self.heap_length:
            if self.heap_array[self.k * index + i] < minChild:
                minChild = self.heap_array[self.k * index + i]
                minChildIndex = self.k * index + i
            if i == self.k:
                break
            i += 1

        return minChildIndex

    def add_num(self, x):
        self.heap_array.append(x)
        self.heap_length += 1
        self.heapify_up(self.heap_length - 1)

    def pop_min(self):
        root = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        self.heap_array.pop(-1)
        self.heap_length -= 1
        self.heapify_down(0)
        return root

    def heapify_up(self, index):

        parent = (index - 1) // self.k
        if parent == 0:
            parent = self.k

        while (index - 1) // self.k >= 0:
            if self.heap_array[index] < self.heap_array[(index - 1) // self.k]:
                #swap
                temp = self.heap_array[(index - 1) // self.k]
                self.heap_array[(index - 1) // self.k] = self.heap_array[index]
                self.heap_array[index] = temp
            index = (index - 1) // self.k
            if index == 0:
                break
            parent = (index - 1) // self.k
            if parent == 0:
                parent = self.k


    def heapify_down(self, index):
        while index * self.k <= self.heap_length:
            childIndex = self.findMinChild(index)
            if childIndex == -1:
                break
            if self.heap_array[index] > self.heap_array[childIndex]:
                #swap
                temp = self.heap_array[index]
                self.heap_array[index] = self.heap_array[childIndex]
                self.heap_array[childIndex] = temp
            index = childIndex


    # This will print the heap in the requested format. You do not need to modify this function
    def __str__(self):
        # Do not sort the heap array
        s = ""
        for i in self.heap_array:
            s += str(i) + " "
        return s.strip()

# Given Starter Code for IO. You need not modify code beneath this line

[k, c] = [int(x) for x in raw_input().split()]
h = minHeap(k)
for i in range(c):
    command = raw_input().split()
    if command[0] == "add":
        h.add_num(int(command[1]))
    elif command[0] == "remove":
        print h.pop_min()
    elif command[0] == "print":
        print h
