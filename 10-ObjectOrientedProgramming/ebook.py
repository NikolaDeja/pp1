class Ebook():
    def __init__(self, title, author, num_of_pages, curr_page):
        self.title=title
        self.author=author
        self.num=num_of_pages
        self.curr=curr_page

    def open(self):
        self.is_open=True

    def close(self):
        self.is_open=False
        
    def reding_pages(self):
        if self.is_open==True:
            self.curr+=1
        else:
            print("book is closed")

    def pervious_pages(self):
        if self.is_open==True:
            self.curr-=1
        else:
            print("book is closed")
    
    def book_status(self):
        print(self.curr)

    def __str__(self):
        return self.title +" "+ self.author +" "+ str(self.num )+" "+ str(self.curr)

    