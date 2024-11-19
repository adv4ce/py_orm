from tabulate import tabulate
from connection import session
from models import Publisher, Book, Shop, Stock, Sale
import json


def out_data(publisher):
    author = (
        session.query(Publisher.name, Publisher.id)
        .filter(Publisher.name == publisher)
        .first()
    )
    if author == None:
        return "Автор не найден!"
    publisher_id = author[1]

    book = (
        session.query(Book.id, Book.title)
        .filter(Book.id_publisher == publisher_id)
        .all()
    )
    data = [
        {"book_name": "", "shop_name": "", "price": 0, "date": ""}
        for i in range(len(book))
    ]
    book_id = [i[0] for i in book]

  
    stock = [
        j
        for i in book_id
        for j in session.query(Stock.id, Stock.id_shop, Stock.id_book)
        .filter(Stock.id_book == i)
        .all()
    ]

    shop = [j for i in stock for j in session.query(Shop.name).filter(Shop.id == i[1])]

    sale = [
        j
        for i in stock
        for j in session.query(Sale.price, Sale.date_sale)
        .filter(Sale.id_stock == i[0])
        .all()
    ]

    for i in range(len(data)):
        for j in range(len(book)):
            print(sale, book)
            if i == j:
                data[i]["book_name"] = book[j][1]
                data[i]["shop_name"] = shop[j][0]
                data[i]["price"] = sale[j][0]
                data[i]["date"] = sale[j][1].strftime("%Y-%m-%d %H:%M:%S")

    return data
