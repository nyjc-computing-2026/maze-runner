"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        # store data and next pointer
        self._data = data
        self.next: "Node | None" = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self._data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        _head: Node object if linked list is not empty
               None if linked list is empty

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        count = 0
        current = self._head
        while current is not None:
            current = current.next
            count += 1
        return count

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved (zero-indexed).

        Returns
            item

        Raises
            IndexError if n >= length
        """
        # Validation: ensure index is 0 or positive
        if n < 0:
            raise IndexError("n must be 0 or positive")
        # Check if linkedlist is empty
        if self._head is None:
            raise IndexError("linkedlist is empty")
        current = self._head
        # Attempt to reach the nth node
        while (
                n > 0  # Exit if nth node reached
                and current is not None  # Exit if passed tail
        ):
            current = current.next
            n -= 1
        # If passed the tail, raise IndexError
        if current is None:
            raise IndexError("n >= length")
        # nth node is reached: return item
        return current.get()

    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        # Validation: ensure index is 0 or positive
        if n < 0:
            raise IndexError("n must be 0 or positive")
        if n == 0:
            node = Node(item)
            node.next = self._head
            self._head = node
        else:  # n > 0
            # Get the prev node (at index n - 1)
            prev = self._head
            while (
                n > 1
                and prev is not None
            ):
                prev = prev.next
                n -= 1
            if prev is None:  # passed tail
                raise IndexError("n > length")
            node = Node(item)
            node.next = prev.next
            prev.next = node

    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        # Check if linked list is empty
        if self._head is None:
            self._head = Node(item)
        else:
            # get last node
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(item)

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved (zero-indexed).

        Raises
            IndexError if n >= length
        """
        # Validation: ensure index is 0 or positive
        if n < 0:
            raise IndexError("n must be 0 or positive")
        if self._head is None:
            raise IndexError("linked list is empty")
        if n == 0:  # head deletion
            self._head = self._head.next
            return
        prev = self._head
        while (
                n > 1
                and prev.next is not None
        ):
            prev = prev.next
            n -= 1
        if prev.next is None:
            raise IndexError("n >= length")
        prev.next = prev.next.next

    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        # Check for empty linkedlist
        if self._head is None:
            return False
        current = self._head
        while current is not None:
            if current.get() == item:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    llist = LinkedList()
    llist.append("a")  # type: ignore
    llist.append("b")  # type: ignore
    print("Index 0:", llist.get(0))  # a
    print("Index 1:", llist.get(1))  # b
    print("Length:", llist.length())  # 2
