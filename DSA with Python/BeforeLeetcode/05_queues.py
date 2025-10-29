# Queues Data Structure

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue1:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def main():
    print("\n ------ Queue Implementation using List/Arrays ------")
    # Create a queue
    myQueue = Queue()

    myQueue.enqueue('A')
    myQueue.enqueue('B')
    myQueue.enqueue('C')
    print("Queue: ", myQueue.queue)

    print("Dequeue: ", myQueue.dequeue())
    print("Peek: ", myQueue.peek())
    print("isEmpty: ", myQueue.isEmpty())
    print("Size: ", myQueue.size())

    print("\n ------ Queue Implementation using Linked List ------")
    # Create a queue
    myQueue1 = Queue1()

    myQueue1.enqueue('A')
    myQueue1.enqueue('B')
    myQueue1.enqueue('C')
    print("Queue: ", end="")
    myQueue1.printQueue()

    print("Dequeue: ", myQueue1.dequeue())
    print("Peek: ", myQueue1.peek())
    print("isEmpty: ", myQueue1.isEmpty())
    print("Size: ", myQueue1.size())



if __name__ == "__main__":
    main()