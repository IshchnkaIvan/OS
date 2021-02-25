import threading


class LockingStack:
    items: list[object] = None
    lock_object: threading.Lock = None

    def __init__(self):
        self.items = []
        self.lock_object = threading.Lock()

    def is_empty(self) -> bool:
        return self.items == []

    def push(self, item) -> None:
        with self.lock_object.acquire(blocking=True):
            self.items.append(item)

    def pop(self) -> object:
        with self.lock_object.acquire(blocking=True):
            return self.items.pop()

    def peek(self) -> object:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def contains(self, item) -> bool:
        return item in self.items
