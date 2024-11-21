from tabulate import tabulate
from connection import session
from models import Publisher, Book, Shop, Stock, Sale
import json


def out_data(publisher):
    data = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .select_from(Shop)
        .join(Stock)
        .join(Book)
        .join(Publisher)
        .join(Sale)
    )
    if publisher.isdigit():
        author = data.filter(Publisher.id == publisher).all()
    else:
        author = data.filter(Publisher.name == publisher).all()

    author = [[i[0], i[1], i[2], i[3].strftime("%d-%m-%Y")] for i in author]
    table_data = author
    headers = ["Title", "Shop", "Price", "Date"]
    table = tabulate(table_data, headers=headers, tablefmt="grid")
    return table
