
class MedianFinder:

    def __init__(self):
        self.total_count = 0
        self.mx_heap = []
        self.mn_heap = []
        
    def addNum(self, num: int) -> None:
        self.total_count+=1
        if len(self.mx_heap)==0 or -self.mx_heap[0]>num:
            heapq.heappush(self.mx_heap,-num)
        else:
            heapq.heappush(self.mn_heap,num)
        #balance the heaps
        if len(self.mx_heap)>len(self.mn_heap)+1:
            heapq.heappush(self.mn_heap,-heapq.heappop(self.mx_heap))
        if len(self.mn_heap)>len(self.mx_heap):
            heapq.heappush(self.mx_heap,-heapq.heappop(self.mn_heap))
        #print(self.mx_heap)
        #print(self.mn_heap)
    def findMedian(self) -> float:
        #print('total {}'.format(self.total_count))
        if self.total_count%2 != 0:
           # print('here')
            return -self.mx_heap[0]
        else:
            #print('return value {}'.format((self.mn_heap[0]+(-self.mx_heap[0]))//2))
            return (self.mn_heap[0]+(-self.mx_heap[0]))/2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
