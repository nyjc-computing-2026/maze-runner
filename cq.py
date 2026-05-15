"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self._data = [None] * size
        # -1 represents invalid slot
        self.head = -1  # First item to be dequeued
        self.tail = 0  # First empty slot (for enqueueing)

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def is_full(self) -> bool:
        return self.tail == -1

    def is_empty(self) -> bool:
        return self.head == -1

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.is_full():
            raise IndexError("Queue is full")
        self._data[self.tail] = item
        # If head was previously invalid (empty queue),
        # Update it to point to newly enqueued item
        if self.head == -1:
            self.head = self.tail
        # Advance tail
        self.tail = (self.tail + 1) % self.size
        # If tail is now at head, queue is full
        # Update tail to sentinel value
        if self.tail == self.head:
            self.tail = -1

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._data[self.head]
        # If tail was previously invalid (full queue),
        # Update it to point to newly freed slot
        if self.tail == -1:
            self.tail = self.head
        # Advance head
        self.head = (self.head + 1) % self.size
        # If head is now at tail, queue is empty
        # Update head to sentinel value
        if self.head == self.tail:
            self.head = -1
        return item

    def contains(self, item: tuple[int, int]) -> bool:
        """Check if the queue contains the item.

        Arguments
            - item
              The item to be checked.

        Return
            True if the item is in the queue, False otherwise.
        """
        # Cannot use `item in self._data` because it would include
        # invalid items
        # Have to do linear search from head to tail
        i = self.head
        if self.is_full():
            # No valid tail
            # Since tail wraps around, next index is head
            end = self.head
        else:
            end = self.tail
        while i != self.tail:
            if self._data[i] == item:
                return True
            i = (i + 1) % self.size
        return False


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    pass
