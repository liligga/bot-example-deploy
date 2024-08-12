import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.CREATE_SURVEY_RESULTS_TABLE)

            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)

            conn.commit()


# conn.execute(
#     "INSERT INTO survey_results (name, age, gender, genre) VALUES (?, ?, ?, ?)",
#     ("igor", 23, "male", "horror")
# )