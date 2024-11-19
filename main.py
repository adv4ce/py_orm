from connection import session
from record_data import record_data
from models import Publisher, Book, Shop, Stock, Sale
from connection import Base, engine
from data_out import out_data


def delete_test_table():
    Base.metadata.drop_all(engine)


def main():
    print(out_data("Eksmo"))
    # print(out_data("AST"))
    # print(out_data("Mann, Ivanov & Ferber"))
    # print(out_data("Piter"))


if __name__ == "__main__":
    main()
