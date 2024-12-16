class Author:
    _authors_table = []
    _id_counter = 1

    def __init__(self, id: int, name: str):
        if not isinstance(id, int):
            raise ValueError("id must be of type int.")
        
        self._id = id

        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string.")
        
        if hasattr(self, "_name"):
            raise AttributeError("Cannot modify name after initialization")
        
        self._name = name

        self.__class__._authors_table.append({"id": self._id, "name": self._name})
        self.__class__._id_counter += 1

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("Cannot modify id.")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify name.")

    @classmethod
    def get_all_authors(cls):
        return cls._authors_table

    @property
    def articles(self):
        from models.article import Article  # Assuming Article is defined in models.article
        associated_articles = [article for article in Article._articles_table if article["author_id"] == self._id]
        return associated_articles

    @property
    def magazines(self):
        associated_articles = self.articles
        associated_magazines = []
        from models.magazine import Magazine  # Assuming Magazine is defined in models.magazine
        for article in associated_articles:
            for magazine in Magazine._magazines_table:
                if magazine["id"] == article["magazine_id"]:
                    associated_magazines.append(magazine)
        return associated_magazines

    def __repr__(self):
        return f'<Author {self._name}>'
