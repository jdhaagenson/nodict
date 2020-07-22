#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Jordan Haagenson'


class Node:
    def __init__(self, key, value=None):
        """
        initialize the instance of Node
        :param key: key
        :type key: str
        :param value: value for key
        :type value: int or str
        """
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """
        string representation of object
        :return:
        :rtype:
        """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """
        compare the key, value pair of this instance with another instance
        :param other: other instance with key, value wrong sometimes
        :type other: Node object
        :return: true or false based on how they compare
        :rtype: bool
        """
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """
        initialize new instance of NoDict
        :param num_buckets:
        :type num_buckets:
        """
        self.buckets = []
        self.size = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                         for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """
        Adds a node to NoDict contents
        :param key: key
        :type key: str
        :param value: value for key
        :type value: int or str
        :return: new node added
        :rtype: Node
        """
        new_node = Node(key, value)
        h = new_node.hash % self.size
        for node in enumerate(self.buckets[h]):
            if new_node == node[1]:
                del self.buckets[h][node[0]]
        self.buckets[h].append(new_node)

    def get(self, key):
        """
        Lookup key inside of NoDict class
        :param key: key to look up
        :type key: str
        :return: value of Node with matching key
        :rtype: int or str
        """
        node_to_find = Node(key)
        h = node_to_find.hash % self.size
        val = None
        for node in self.buckets[h]:
            if node_to_find == node:
                val = node.value
        if val is None:
            raise KeyError(key)
        return val

    def __getitem__(self, key):
        """
        Enables square bracket reading behavior
        :param key: key
        :type key: str
        :return: value
        :rtype: str or int
        """
        val = self.get(key)
        if val is None:
            raise KeyError(key)
        return val

    def __setitem__(self, key, value):
        """
        Enables square bracket assignment behavior
        :param key: key
        :type key: str
        :param value: value
        :type value: str or int
        :return: Node
        :rtype: Node
        """
        return self.add(key, value)
