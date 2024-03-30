# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.flatList = []
        self.iterator = 0
        self.flattenList(nestedList)
    
    def flattenList(self, nestedList):
        for ele in nestedList:
            if ele.isInteger():
                self.flatList.append(ele.getInteger())
            else:
                self.flattenList(ele.getList())
    
    def next(self):
        if self.hasNext():
            val = self.flatList[self.iterator]
            self.iterator += 1
            return val
        else:
            return None
    
    def hasNext(self):
        return self.iterator < len(self.flatList)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())