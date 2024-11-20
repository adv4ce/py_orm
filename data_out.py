from tabulate import tabulate
from connection import session
from models import Publisher, Book, Shop, Stock, Sale
import json


def out_data(publisher):
    author = session.query(Publisher.id).filter(Publisher.name == publisher).first()

    if author == None:
        return "Автор не найден!"

    book = (
        session.query(Book.id, Book.title).filter(Book.id_publisher == author[0]).all()
    )

    data = [
        {
            "book_id": i[0],
            "stock_id": 0,
            "title": i[1],
            "shop": "",
            "price": "",
            "date": "",
        }
        for i in book
    ]

    shop = session.query(Shop.id, Shop.name).all()
    shop_data = {i[0]: i[1] for i in shop}

    stock = [
        j
        for i in book
        for j in session.query(Stock.id, Stock.id_book, Stock.id_shop)
        .filter(Stock.id_book == i[0])
        .all()
    ]

    for i in data:
        for j in stock:
            if j[1] == i["book_id"]:
                i["shop"] = shop_data[j[2]]
                i["stock_id"] = j[0]

    sale = session.query(Sale.id_stock, Sale.price, Sale.date_sale).all()

    for i in data:
        for j in sale:
            if j[0] == i["stock_id"]:
                i["price"] = int(j[1])
                i["date"] = j[2].strftime("%Y-%m-%d %H:%M:%S")

    for i in data:
        del i["book_id"]
        del i["stock_id"]

    table_data = [[i[j] for j in i.keys()] for i in data]
    headers = ["Title", "Shop", "Price", "Date"]
    table = tabulate(table_data, headers=headers, tablefmt="grid")

    return table
