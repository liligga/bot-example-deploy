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

    DROP_GENRES_TABLE = """
        DROP TABLE IF EXISTS genres
    """

    CREATE_GENRES_TABLE = """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """

    POPULATE_GENRES = """
        INSERT INTO genres(name) VALUES 
            ("Детектив"),
            ("Фантастика"),
            ("Триллер"),
            ("Роман")
    """

    DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books"

    CREATE_BOOKS_TABLE = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            price INTEGER,
            cover TEXT,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    """

    POPULATE_BOOKS = """
    INSERT INTO books(name, author, price, cover, genre_id) VALUES 
    ('Тень в зеркале', 'Алексей Смирнов', 2000, 'images/book1.jpg', 1),
    ('Хроники Серебряного леса', 'Елена Волкова', 2500, 'images/book2.webp', 2),
    ('Квантовый разлом', 'Игорь Петров', 1400, 'images/book3.jpg', 3),
    ('Осенние письма', 'Мария Соколова', 2450, 'images/book2.webp', 4),
    ('Код мести', 'Сергей Антонов', 1239, 'images/book3.jpg', 1)
    """