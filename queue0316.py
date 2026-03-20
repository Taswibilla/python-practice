from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.popleft()

    def sizequeue(self):
        return len(self.queue)


if __name__ == "__main__":
    q = Queue()

    (q.enqueue(10))
    (q.enqueue(20))
    (q.enqueue(30))
    print(list(q.queue))

    print(q.dequeue())
    print("Is queue empty?", q.is_empty())
    print("Queue size:", q.sizequeue())