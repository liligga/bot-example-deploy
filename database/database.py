import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.CREATE_SURVEY_RESULTS_TABLE)
            conn.execute(Queries.DROP_GENRES_TABLE)
            conn.execute(Queries.CREATE_GENRES_TABLE)
            conn.execute(Queries.POPULATE_GENRES)
            conn.execute(Queries.DROP_BOOKS_TABLE)
            conn.execute(Queries.CREATE_BOOKS_TABLE)
            conn.execute(Queries.POPULATE_BOOKS)


            conn.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)

            conn.commit()

    def fetch(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(query, params)

            return result.fetchall()




# conn.execute(
#     "INSERT INTO survey_results (name, age, gender, genre) VALUES (?, ?, ?, ?)",
#     ("igor", 23, "male", "horror")
# )