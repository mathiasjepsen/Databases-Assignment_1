# Assignment 1 - Simple DB with Hashmap-based Index

## Prerequisites:
Python 3+ or Docker

## How to run:
Clone the repository, move into /Assignment_1, and run the following command:
```
python simple_db_write.py && python simple_db_read.py
```
You might need to substitute _python_ with _python3_ if you have multiple versions of Python installed.

If you don't have Python installed, run the following Docker command:
```
docker run -it --rm -v "$PWD":/src -w /src python:slim sh -c "python simple_db_write.py;python simple_db_read.py"
```

## Results

The _simple_db_write.py_ file is run, which creates the database file and populates it with five records.
```python
from Simple_db import Simple_db


if __name__ == "__main__":
    db = Simple_db("fruitstore.db")

    db.write_to_db("ananas", "3")
    db.write_to_db("banana", "1.5")
    db.write_to_db("mango", "8")
    db.write_to_db("avocado", "12")
    db.write_to_db("strawberry", "2")
```

Then the _simple_db_read.py_ file is run to print out the contents of the database in the terminal.
```python
from Simple_db import Simple_db


if __name__ == "__main__":
    db = Simple_db("fruitstore.db")
    db.populate_in_memory_dict()
    db.print_db_contents()
```

Producing the results shown below:
```
Database contents
————————————————————————
Key: ananas, value: 3
Key: banana, value: 1.5
Key: mango, value: 8
Key: avocado, value: 12
Key: strawberry, value: 2
————————————————————————
```
