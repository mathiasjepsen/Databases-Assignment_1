from Simple_db import Simple_db


if __name__ == "__main__":
    db = Simple_db("fruitstore.db")
    db.populate()
    db.print_db_contents()
