from random import randrange

class Queue:
    def __init__(self, len_array:int):
        self.len_array = len_array
        self.array = []
    
    def append_values(self):
        while(True):
            if(len(self.array) == self.len_array):
                break
            self.array.append(randrange(0, 100))

    def fifo(self):
        index = 0
        while(self.array):
            value = self.array.pop(index)
            print(f"The value '{value}' will be removed of queue.", self.array, sep="\n")

if __name__ == "__main__":
    queue = Queue(10)
    queue.append_values()
    print(queue.array)
    queue.fifo()