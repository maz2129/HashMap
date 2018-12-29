#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:25:16 2018

A Hashmap implemented in Python. Uses separate chaining to handle collisions.

Public methods:
    insert(x):   Inserts x into hashmap.
    remove(x):   Removes x from hashmap.
    contains(x): Returns a boolean indicating if x is in hashmap.
    clear():     Removes all elements of hashmap.

@author: mattzinman
"""
import math

class Hashmap:

    """
    Constructor
    @param the size of the hashmap
    """
    def __init__(self, size):
        size = self.next_prime(size)
        self.table = []        # List of chained lists in HashTable
        self.filled = 0        # Number of cells that are occupied
        self.table_size = size # Size of table at any time
        self.og_size = size    # Size that Hashtable will be set to if you clear() it
        for i in range(0,size):
            self.table.append([])

    """
    Inserts x into hashmap
    @param x the element to be inserted
    """
    def insert(self, x):
        chained_list = self.table[self.hash_it(x)]
        if not x in chained_list:
            chained_list.append(x)
            self.filled += 1
        if self.filled > self.table_size:
            # Means that load factor > 1
            self.rehash()
    
    """
    Removes x from hashmap
    @param x the element to be removed
    """
    def remove(self, x):
        chained_list = self.table[self.hash_it(x)]
        if x in chained_list:
            chained_list.remove(x)
            self.filled -= 1
        
    """
    Checks if x is in hashmap
    @param x is the element in question
    @return boolean indiciating if x is in hashmap
    """
    def contains(self, x):
        chained_list = self.table[self.hash_it(x)]
        return x in chained_list
    
    """
    Clears all elements from hashamp
    """
    def clear(self):
        self.table = []
        self.filled = 0
        self.table_size = self.og_size
        for i in range(0,self.og_size):
            self.table.append([])
    
    """
    Increases the size of the Hashmap by ~2 times
    """
    def rehash(self):
        old_filled = self.filled
        old_table = self.table
        new_table = []
        self.table_size = self.next_prime(self.table_size*2)
        for i in range(0, self.table_size):
            new_table.append([])
        self.table = new_table
        for chained_list in old_table:
            for x in chained_list:
                self.insert(x)
        self.filled = old_filled

    """
    Hashes a value to an index on the hashmap
    @param any type
    @return int
    """
    def hash_it(self, x):
        h = hash(x) % self.table_size
        if h<0:
            h += self.table_size
        return h
        
    """
    Finds the next prime number
    @param any int
    @return the next prime
    """
    def next_prime(self, n):
        while not self.is_prime(n):
            n += 1
        return n
    
    """
    Determines if a number is prime
    @param any int
    @return boolean indicating if number is prime
    """
    def is_prime(self, n):
        return (2**n - 2)%n == 0
