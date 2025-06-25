book_title = input("Book Title ")
book_author = input ("Name of its author ")
id_book = int(input("Assign an ID (between 1000 and 1999): "))
price = float(input("Price of the book: "))

if price > 15:
    total_amount = price
else:
    price += 3
    total_amount = price

print (f"""Title: {book_title};
Author: {book_author};
ID: {id_book};
Total amount: {total_amount}
""")
