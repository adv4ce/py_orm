import json
from models import Publisher, Book, Shop, Stock, Sale
from connection import session
from datetime import datetime

def record_data():
    with open("fixtures.json") as file:
        fixtures = json.load(file)
    
    for data in fixtures:
        fields = data['fields']
        match data['model']:
            case 'publisher':
                new_line = Publisher(name=fields['name'])

            case 'book':
                new_line = Book(title=fields['title'], id_publisher=fields['id_publisher'])

            case 'shop':
                new_line = Shop(name=fields['name'])
            
            case 'stock':
                new_line = Stock(id_shop=fields['id_shop'], id_book=fields['id_book'], count=fields['count'])
            
            case 'sale':
                new_line = Sale(price=fields['price'], date_sale = datetime.strptime(fields['date_sale'], '%Y-%m-%dT%H:%M:%S.%fZ'), count=fields['count'], id_stock=fields['id_stock'])
        
        session.add(new_line)
    
    session.commit()
    
    return 'Данные успешно перенесены в таблицы!'
