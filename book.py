class Book:
    def __init__(self,title,author,year,ISBN):
        self.title=title
        self.author=author
        self.year=year
        self.ISBN=ISBN
        # self.review_count=review_count
        # self.average_score=average_score
    def print_info(self):
        print(F'title:{self.title}')
        print(f"author:{self.author}")
        print(f"year:{self.year}")
        print(f"ISBN:{self.ISBN}")

def main():
        f1=Book(title="a",author="hh",year="2000",ISBN="1111")
        f1.print_info()

if __name__ =="__main__":
    main()
