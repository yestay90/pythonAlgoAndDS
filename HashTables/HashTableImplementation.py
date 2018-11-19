
class HashTable(object):

    def __init__(self, size):

        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self, key, data):

        hashValue = self.hashFuncton(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextSlot = self.rehash(hashValue, len(self.slots ))

                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data

                else:
                    self.data[nextSlot] = data

    def get(self,key):

        startSlot = self.hashFuncton(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startSlot

        while self.slots[position] != None and not stop and not found:

            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

                if position == startSlot:
                    stop = True

        return data


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


    def hashFuncton(self, key, size):

        return key%size

    def rehash(self,oldHash, size):
        reutrn (oldHash + 1) % size