'''

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or insert the key if not already present. When the cache reaches its capacity, it should invalidate and remove the
least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
The functions get and put must each run in O(1) average time complexity.

Example 1:
        Input
            ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
            Output
            [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
            
        Explanation
            // cnt(x) = the use counter for key x
            // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
            LFUCache lfu = new LFUCache(2);
            lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
            lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
            lfu.get(1);      // return 1
                             // cache=[1,2], cnt(2)=1, cnt(1)=2
            lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                             // cache=[3,1], cnt(3)=1, cnt(1)=2
            lfu.get(2);      // return -1 (not found)
            lfu.get(3);      // return 3
                             // cache=[3,1], cnt(3)=2, cnt(1)=2
            lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                             // cache=[4,3], cnt(4)=1, cnt(3)=2
            lfu.get(1);      // return -1 (not found)
            lfu.get(3);      // return 3
                             // cache=[3,4], cnt(4)=1, cnt(3)=3
            lfu.get(4);      // return 4
                             // cache=[4,3], cnt(4)=2, cnt(3)=3
Constraints:
        1 <= capacity <= 104
        0 <= key <= 105
        0 <= value <= 109
        At most 2 * 105 calls will be made to get and put.

'''


from collections import defaultdict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.frequencyMap = defaultdict(LinkedList)
        self.minFreq = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        tempNode = self.cache[key]
        self.frequencyMap[tempNode.freq].removeNode(tempNode)
        if self.frequencyMap[tempNode.freq].head is None:
            del self.frequencyMap[tempNode.freq]
            if self.minFreq == tempNode.freq:
                self.minFreq += 1
        
        self.cache[key].freq += 1
        self.frequencyMap[self.cache[key].freq].insertAtTail(self.cache[key])
        return self.cache[key].value
   
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if self.capacity == 0:
            return
        
        if key in self.cache:
            self.get(key)
            self.cache[key].value = value
            return
        
        if self.size == self.capacity:
            del self.cache[self.frequencyMap[self.minFreq].head.key]
            self.frequencyMap[self.minFreq].removeHead()
            if self.frequencyMap[self.minFreq].head is None:
                del self.frequencyMap[self.minFreq]
            self.size -= 1
        
        self.minFreq = 1
        self.cache[key] = LinkedListNode(key, value, self.minFreq)
        self.frequencyMap[self.cache[key].freq].insertAtTail(self.cache[key])
        self.size += 1
    
    def printFrequencyMap(self):
        print("frequncyMap:")
        for freq, linkedList in self.frequencyMap.items():
            print("frequency", freq)
            print("linked list", printLinkedList(linkedList))

    

def printLinkedList(linkedList):
    current = linkedList.head
    nodes = []
    while current is not None:
        nodes.append(str(current.value))
        current = current.next
    return " -> ".join(nodes)
    
    
class LinkedListNode:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtTail(self, node):
        node.prev, node.next = None, None
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def removeNode(self, node):
        if node is None:
            return
        
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
    
    def removeHead(self):
        self.removeNode(self.head)
    
if __name__ == "__main__":
    lfuCache = LFUCache(2)
    lfuCache.put(1, 1)
    print("put(1, 1)")
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    lfuCache.put(2, 2)
    print("\nput(2, 2)")
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    print("\nget(1)")
    print("value", lfuCache.get(1))
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    lfuCache.put(3, 3)
    print("\nput(3, 3)")
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    print("\nget(2)")
    print("value", lfuCache.get(2))
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    print("\nget(3)")
    print("value", lfuCache.get(3))
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    lfuCache.put(4, 4)
    print("\nput(4, 4)")
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    print("\nget(1)")
    print("value", lfuCache.get(1))
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    print("\nget(3)")
    print("value", lfuCache.get(3))
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()

    print("\nget(4)")
    print("value", lfuCache.get(4))
    print("cache", lfuCache.cache)
    lfuCache.printFrequencyMap()



"""
output: 
put(1, 1)
('cache', {1: <__main__.LinkedListNode instance at 0x10e7237e8>})
frequncyMap:
('frequency', 1)
('linked list', '1')
put(2, 2)
('cache', {1: <__main__.LinkedListNode instance at 0x10e7237e8>, 2: <__main__.LinkedListNode instance at 0x10e723830>})
frequncyMap:
('frequency', 1)
('linked list', '1 -> 2')
get(1)
('value', 1)
('cache', {1: <__main__.LinkedListNode instance at 0x10e7237e8>, 2: <__main__.LinkedListNode instance at 0x10e723830>})
frequncyMap:
('frequency', 1)
('linked list', '2')
('frequency', 2)
('linked list', '1')
put(3, 3)
('cache', {1: <__main__.LinkedListNode instance at 0x10e7237e8>, 3: <__main__.LinkedListNode instance at 0x10e723758>})
frequncyMap:
('frequency', 1)
('linked list', '3')
('frequency', 2)
('linked list', '1')
get(2)
('value', -1)
('cache', {1: <__main__.LinkedListNode instance at 0x10e7237e8>, 3: <__main__.LinkedListNode instance at 0x10e723758>})
frequncyMap:
('frequency', 1)
('linked list', '3')
('frequency', 2)
('linked list', '1')
get(3)
('value', 3)
('cache', {1: <__main__.LinkedListNode instance at 0x10e7237e8>, 3: <__main__.LinkedListNode instance at 0x10e723758>})
frequncyMap:
('frequency', 2)
('linked list', '1 -> 3')
put(4, 4)
('cache', {3: <__main__.LinkedListNode instance at 0x10e723758>, 4: <__main__.LinkedListNode instance at 0x10e7237e8>})
frequncyMap:
('frequency', 1)
('linked list', '4')
('frequency', 2)
('linked list', '3')
get(1)
('value', -1)
('cache', {3: <__main__.LinkedListNode instance at 0x10e723758>, 4: <__main__.LinkedListNode instance at 0x10e7237e8>})
frequncyMap:
('frequency', 1)
('linked list', '4')
('frequency', 2)
('linked list', '3')
get(3)
('value', 3)
('cache', {3: <__main__.LinkedListNode instance at 0x10e723758>, 4: <__main__.LinkedListNode instance at 0x10e7237e8>})
frequncyMap:
('frequency', 1)
('linked list', '4')
('frequency', 3)
('linked list', '3')
get(4)
('value', 4)
('cache', {3: <__main__.LinkedListNode instance at 0x10e723758>, 4: <__main__.LinkedListNode instance at 0x10e7237e8>})
frequncyMap:
('frequency', 2)
('linked list', '4')
('frequency', 3)
('linked list', '3')
"""
