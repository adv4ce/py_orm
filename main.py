from record_data import record_data
from connection import Base, engine
from data_out import out_data


def delete_test_table():
    Base.metadata.drop_all(engine)


def main():
    print(out_data(input("Введите автора: ").encode("utf-8").decode("unicode_escape")))


if __name__ == "__main__":
    main()
