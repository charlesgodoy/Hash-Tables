# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [[]] * capacity
        self.size = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # hashsum = 0
        # for idx, c in enumerate(key):
        #     hashsum += (idx + len(key)) ** ord(c)
        #     hashsum = hashsum % self.capacity

        hashsum = hash(key) % self.capacity

        return hashsum


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        hash_key = self._hash(key)
        key_exists = False
        bucket = self.storage[hash_key]
        for i, pair in enumerate(bucket):
            if key is pair.key:
                key_exists = True
                break
            
        newPair = LinkedPair(key, value)
        if key_exists:
            bucket[i] = newPair

        else:
            bucket.append(newPair)
            self.size += 1

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash(key)
        key_exists = False
        bucket = self.storage[hash_key]
        for i, pair in enumerate(bucket):
            if key == pair.key:
                key_exists = True
                break

        if key_exists:
            del bucket[i]
            print('key removed')
            self.size -= 1

        else:
            print('Key not found: ')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash(key)
        bucket = self.storage[hash_key]
        for i, pair in enumerate(bucket):
            if key == pair.key:
                return pair.value

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        currentStorage = self.storage
        self.storage = [[]] * (self.capacity * 2)
        for bucket in currentStorage:
            for pair in bucket:
                self.insert(pair.key, pair.value)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
