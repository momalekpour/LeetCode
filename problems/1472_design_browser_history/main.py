class ListUrl:
    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListUrl(homepage)
        self.head = ListUrl(-1, prev=None, next=self.curr)
        self.tail = ListUrl(-1, prev=self.curr, next=None)
        self.curr.prev = self.head
        self.curr.next = self.tail

    def visit(self, url: str) -> None:
        new_url = ListUrl(url, prev=self.curr, next=self.tail)
        self.curr.next = new_url
        self.tail.prev = new_url
        self.curr = new_url

    def back(self, steps: int) -> str:
        tmp_url = self.curr.prev
        s = 1
        while tmp_url and tmp_url != self.head:
            if s == steps:
                self.curr = tmp_url
                return tmp_url.url
            tmp_url = tmp_url.prev
            s += 1
        self.curr = self.head.next
        return self.head.next.url

    def forward(self, steps: int) -> str:
        tmp_url = self.curr.next
        s = 1
        while tmp_url and tmp_url != self.tail:
            if s == steps:
                self.curr = tmp_url
                return tmp_url.url
            tmp_url = tmp_url.next
            s += 1
        self.curr = self.tail.prev
        return self.tail.prev.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory("varzesh3.com")
# obj.visit("google.com")
# obj.visit("youtube.com.com")
# param_2 = obj.back(1)
# param_3 = obj.forward(1)
