
'''
browser History
= visit(stirng url) -> url that we will visti 
= back(int stpes) -> go back upto steps, steps > len(browserHistory) we shoudl return to the last url, clears up all fthe forward histories 
= froward(int steps) -> go foraward steps, steps > len(crowse) we should return to the first one

-- array,
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        # self.array = [] not efficdent 
        self.root = Node(homepage)
        self.current = self.root

    def visit(self, url: str) -> None:
        page = Node(url)
        self.current.next = page
        page.prev = self.current 
        self.current = page
        

    def back(self, steps: int) -> str:
        while self.current.prev and steps:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
        

    def forward(self, steps: int) -> str:
        while self.current.next and steps:
            self.current = self.current.next
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)