import unittest
from task import Node, DoubleLinkedNode


class TestNode(unittest.TestCase):

    def setUp(self) -> None:
        self.node = Node(1)
        self.node.next = None

    def test_node_value(self):
        result = self.node.value
        self.assertEqual(result, 1)

    def test_node_cls(self):
        self.assertEqual(type(Node(5)), type(self.node))

    def test_node_next(self):
        self.node.next = Node(2)
        result = self.node.next.value
        self.assertEqual(result, 2)

    def test_node_next_cls(self):
        self.node.next = Node(2)
        self.assertEqual(type(self.node.next), type(self.node))


class TestDoubleNode(unittest.TestCase):

    def setUp(self) -> None:
        self.double_node = DoubleLinkedNode(1)
        self.double_node.next = None
        self.double_node.prev = None

    def test_double_node_value(self):
        self.assertEqual(self.double_node.value, 1)

    def test_double_node_next(self):
        pass


if __name__ == '__main__':
    unittest.main()