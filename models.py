class Book:
    def __init__(self, book_id, title, author,is_bestseller = False):
        if not book_id or not title:
            return
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_bestseller = is_bestseller
        