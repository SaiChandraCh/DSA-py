class Heap:
    def __init__(self,capacity):
        # self.heap_type = heap_type
        self.capacity = capacity
        self.heap_arr = [None] * capacity
        # self.heap = []

    def parent(self, i):
        if i < 0 or i > self.capacity:
            return -1
        return (i-1)//2

    def get_left_child(self, i):
        left = 2*i + 1
        if left < 0 or left >= self.capacity or i < 0 or i >= self.capacity:
            return -1
        return left

    def get_right_child(self, i):
        right = 2*i + 2
        if right < 0 or right >= self.capacity or i < 0 or i >= self.capacity:
            return -1
        return right

    def get_max(self):
        if len(self.heap_arr) == 0:
            return -1
        return self.heap_arr[0]

    def push(self, value):
        self.heap_arr.append(value)

    def pop(self):
        if len(heap) == 0:
            return Exception("Heap is empty")
        val = heap[0]
        heap[0] = heap[-1]
        del heap[-1]
        self.percolate_down(heap,0)
        return val

    # def update(self, value, index):
    #     self.heap_arr[index] = value
    #     self.percolate_down(self.heap_arr, index)

    def heap_sort(self,heap,index):
        pass

    def percolate_down(self,heap,index):
        left_child = self.get_left_child(index)
        right_child = self.get_right_child(index)
        if index < 0 or index >= len(heap):
            return
        largest = -1
        if(not (left_child < 0 or left_child >= len(heap)) and (heap[left_child] > heap[index])):
            largest = left_child
        if(not (right_child < 0 or right_child >= len(heap)) and heap[right_child] > heap[largest]):
            largest = right_child
        if largest != -1:
            heap[index],heap[largest] = heap[largest],heap[index]
            self.percolate_down(heap,largest)
        return heap

    def heapify(self,heap):
        length = len(heap)
        for i in range((length-1)//2-1,-1,-1):
            self.percolate_down(heap,i)
        return heap

if __name__ == '__main__':
    A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
    heap = Heap(10)
    print(heap.heapify(A))
    heap.update(A,)