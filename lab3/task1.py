import json
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("can not pop empty queue.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


q = Queue()

print("Is queue empty?", q.is_empty())  

q.insert(1)
q.insert(2)
q.insert(3)

print("Is queue empty?", q.is_empty())  
print("Popped value:", q.pop()) 

print("Popped value:", q.pop()) 
print("Popped value:", q.pop())
print("Popped value:", q.pop())   

class QueueExtended(Queue):
    queues = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.__class__.queues[name] = self

    def insert(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException("Queue size exceeded.")
        super().insert(value)

    @classmethod
    def get_queue(cls, name):
        return cls.queues.get(name, None)

    @classmethod
    def save(cls, filename):
        queues_data = {name: {'items': queue.items, 'size': queue.size} for name, queue in cls.queues.items()}
        with open(filename, 'w') as f:
            json.dump(queues_data, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            queues_data = json.load(f)
            for name, queue_data in queues_data.items():
                queue = QueueExtended(name, queue_data['size'])
                queue.items = queue_data['items']
                cls.queues[name] = queue
        return cls.queues.get(name, None)


class QueueOutOfRangeException(Exception):
    pass

def test_queue_extended():
    q = QueueExtended("queue1", 3)
    q.insert(1)
    q.insert(2)
    q.insert(3)
    assert q.is_empty() == False
    try:
        q.insert(4)
    except QueueOutOfRangeException:
        assert True
    else:
        assert False

    q = QueueExtended("queue2", 3)
    q.insert(10)
    q.insert(20)
    q.insert(30)
    q.save("test_queue.json")
    loaded_queue = QueueExtended.load("test_queue.json")
    print("Popped value:", loaded_queue.pop()) 
    print("Popped value:", loaded_queue.pop()) 
    print("Popped value:", loaded_queue.pop()) 
    print("Popped value:", loaded_queue.pop()) 

test_queue_extended()
