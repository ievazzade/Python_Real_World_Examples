from heapq import *

class median_of_age:
    minHeap = []
    maxHeap = []

    def insert_age(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return -self.maxHeap[0] 

if __name__ == "__main__":
    medianAge = median_of_age()
    medianAge.insert_age(25)
    medianAge.insert_age(35)
    medianAge.insert_age(30)
    print(medianAge.find_median())
    medianAge.insert_age(22)
    print(medianAge.find_median())