class Simple_db:
    def __init__(self, db):
        self.db = db
        self.in_memory_dict = {}


    def write_to_db(self, key, value):
        with open(self.db, "a") as db:
            self.in_memory_dict[key] = len(key) + 1 + db.tell()
            db.write(f"{key};{value}\n")


    def populate(self):
        with open(self.db) as db:
            key = ""
            was_key_found = False
            while True:
                character = db.read(1)
                if not character:
                    break
                if (character == "\n"):
                    was_key_found = False
                elif (character != ";" and not was_key_found):
                    key += character
                elif (character == ";"):
                    self.in_memory_dict[key] = db.tell()
                    was_key_found = True
                    key = ""


    def print_db_contents(self):
        print("\nDatabase contents\n————————————————————————")
        with open(self.db) as db:
            for key, offset in self.in_memory_dict.items():
                db.seek(offset)
                value = db.readline().rstrip()
                print(f"Key: {key}, value: {value}")
        print("————————————————————————\n")
