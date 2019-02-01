from Simple_db import Simple_db


if __name__ == "__main__":
    db = Simple_db("fruitstore.db")

    db.write_to_db("pineapple", "3")
    db.write_to_db("orange", "1.5")
    db.write_to_db("apple", "8")
    db.write_to_db("blueberry", "12")
    db.write_to_db("carrot", "2")