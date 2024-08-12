class Queries:
    CREATE_SURVEY_RESULTS_TABLE = """
        CREATE TABLE IF NOT EXISTS book_survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            genre TEXT
        )
    """