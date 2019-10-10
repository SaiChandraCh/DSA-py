class Heap:

    __heap = None

    def __init__(self,val):
        self.__heap = [val]

    def heapify(self, index = 0,max=True):
        left = 2 * index + 1
        right = 2 * index + 2
        length = len(self.__heap)
        if index < length and left < length and right < length:
            if max:
                temp = self.__heap
                if left < temp[index] < temp[left]:
                    temp[index],temp[left] = temp[left], temp[index]
                if temp[index] < temp[right]:
                    temp[index],temp[right] = temp[right], temp[index]
                index += 1
                self.heapify(index)
            else:
                pass

    def pop(self):
        self.__heap.pop(0)
        self.heapify()

    def push(self, val):
        self.__heap.append(val)
        self.heapify()

    def insert(self,val,index=0):
        if index == 0:
            self.push(val)
        else:
            pass

    def print(self):
        for i in self.__heap:
            print(i)