class Magazine:
    _magazines_table = []

    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.__class__._magazines_table.append({
            "id": self.id, "name": self.name, "category": self.category
        })

    @property
    def articles(self):
        from models.article import Article  # Assuming Article is defined in models.article
        associated_articles = [article for article in Article._articles_table if article["magazine_id"] == self.id]
        return associated_articles

    @property
    def contributors(self):
        associated_articles = self.articles
        contributors = []
        from models.author import Author  # Assuming Author is defined in models.author
        for article in associated_articles:
            for author in Author._authors_table:
                if author["id"] == article["author_id"]:
                    contributors.append(author)
        return contributors

    def article_titles(self):
        associated_articles = self.articles
        if not associated_articles:
            return []  # Returning an empty list instead of None
        titles = [article["title"] for article in associated_articles]
        return titles

    def contributing_authors(self):
        associated_articles = self.articles
        if not associated_articles:
            return []  # Returning an empty list instead of None

        author_article_count = {}
        for article in associated_articles:
            author_id = article["author_id"]
            if author_id not in author_article_count:
                author_article_count[author_id] = 0
            author_article_count[author_id] += 1

        contributing_authors = []
        from models.author import Author  # Assuming Author is defined in models.author
        for author_id, count in author_article_count.items():
            if count > 2:
                for author in Author._authors_table:
                    if author["id"] == author_id:
                        contributing_authors.append(author)

        return contributing_authors if contributing_authors else []  # Returning an empty list if no authors

    def __repr__(self):
        return f'<Magazine {self.name}, Category: {self.category}>'
