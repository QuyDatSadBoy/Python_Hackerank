from queue import LifoQueue

stack = LifoQueue(maxsize=4)
stack.put(1)
stack.put(2)
stack.put(5)
stack.put(0)
print(stack.get())
