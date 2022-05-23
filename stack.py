from random import randrange

class Stack:
    def __init__(self, len_array:int):
        self.len_array = len_array
        self.array = []
    
    def append_values(self):
        while(True):
            if(len(self.array) == self.len_array):
                break
            self.array.append(randrange(0, 100))

    def lifo(self):
        while(self.array):
            value = self.array.pop()
            print(f"The value '{value}' will be removed of stack.", self.array, sep="\n")

    def fifo(self):
        index = 0
        while(self.array):
            value = self.array.pop(index)
            print(f"The value '{value}' will be removed of stack.", self.array, sep="\n")


if __name__ == "__main__":
    stack  = Stack(10)
    stack.append_values()
    print(stack.array)
    stack.fifo()