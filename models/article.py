class Article:
    _articles_table = []

    def __init__(self, id, title, content, author_id, magazine_id):
        if not isinstance(id, int):
            raise ValueError("id must be of type int.")
        self.id = id

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("title must be a string with 5 to 50 characters.")
        self.title = title

        if not isinstance(content, str) or len(content) == 0:
            raise ValueError("content must be a non-empty string.")
        self.content = content

        if not isinstance(author_id, int):
            raise ValueError("author_id must be of type int.")
        self.author_id = author_id

        if not isinstance(magazine_id, int):
            raise ValueError("magazine_id must be of type int.")
        self.magazine_id = magazine_id

        self.__class__._articles_table.append({
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "magazine_id": self.magazine_id
        })

    def __repr__(self):
        return f'<Article {self.title}>'

    @classmethod
    def get_all_articles(cls):
        return cls._articles_table

    @classmethod
    def find_by_id(cls, article_id):
        for article in cls._articles_table:
            if article["id"] == article_id:
                return article
        return None

    @classmethod
    def find_by_author_id(cls, author_id):
        return [article for article in cls._articles_table if article["author_id"] == author_id]

    @classmethod
    def find_by_magazine_id(cls, magazine_id):
        return [article for article in cls._articles_table if article["magazine_id"] == magazine_id]

    @property
    def author(self):
        from models.author import Author  # Assuming Author is defined in models.author
        for author in Author._authors_table:
            if author["id"] == self.author_id:
                return author
        return None  # No matching author found

    @property
    def magazine(self):
        from models.magazine import Magazine  # Assuming Magazine is defined in models.magazine
        for magazine in Magazine._magazines_table:
            if magazine["id"] == self.magazine_id:
                return magazine
        return None  # No matching magazine found
