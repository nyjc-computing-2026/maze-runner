"""adt.py

# Abstract Data Types

This module defines the Stack and Queue abstract data types
"""
############################### 72 chars ###############################

from datastruct import LinkedList


class IsEmptyError(Exception):
    """Error raised when trying to pop/dequeue items from an empty
    Stack/Queue.
    """


class Stack(LinkedList):
    """Implements the Stack ADT using a linkedlist.

    Arguments
        None

    Methods
        - push(item) -> None
        - pop() -> item
    """

    def __repr__(self) -> str:
        return 'Stack()'

    def push(self, item: tuple[int, int]) -> None:
        """Pushes item onto the top of the stack.
        
        Arguments
            - item
              The item to be pushed.
        
        Returns
            None
        """
        self.insert(0, item)

    def pop(self) -> tuple[int, int]:
        """Pops item off the top of the stack, and returns it.

        Arguments
            None

        Returns
            item

        Raises
            Empty - if stack is already empty
        """
        try:
            return self.get(0)
        except IndexError:
            raise IsEmptyError("Stack is empty")


# Queue can also inherit from Array
class Queue(LinkedList):
    """Implements the Queue ADT using a linkedlist.

    Arguments
        None

    Methods
        - enqueue(item) -> None
        - dequeue() -> item
    """

    def __repr__(self) -> str:
        return 'Queue()'

    def enqueue(self, item: tuple[int, int]) -> None:
        """Enqueues item into the end of the queue.

        Arguments
            - item
              The item to be enqueued.

        Returns
            None
        """
        self.append(item)

    def dequeue(self) -> tuple[int, int]:
        """Dequeues item from the front of the queue, and returns it.

        Arguments
            None

        Returns
            item

        Raises
            Empty - if queue is already empty
        """
        try:
            return self.get(0)
        except IndexError:
            raise IsEmptyError("Queue is empty")


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python adt.py`
    pass
