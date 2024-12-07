# GLORY BE TO GOD,
# ARTICLES - PROJECT, MAIN FILE
# BY ISRAEL MAFABI EMMANUEL

class Magazine:
    magazines:list = []

    def __init__(self, name:str, category:str)->None:
        self.name:str     = name
        self.category:str = category

        # Magazine.magazines.append(self) -> old school 🤭
        # correct implementation
        self.__class__.magazines.append(self)

    # since the two instance vars are immutable... 
    # so😉...
    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self, value:str)->None:
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("error: Name must be a string, more so a non-empty string. ranging between 2 and 16 characters.")

    @property
    def category(self)->str:
        return self._category
    
    @category.setter
    def category(self, value:str)->None:
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("error: Category must be a string, more so a non-empty string.")

    # Methods...
    def articles(self)->list:
        # returning a list of all the articles published by this magazine...
        return [article for article in Article.all if article.magazine == self]

    def article_titles(self)->list:
        # returning a list of article titles published by this magazine...
        # if empty or uninitialized return an empty list ... instead of None.
        if not self.articles():
            return []
        return [article.title for article in self.articles()]

    def contributors(self)->list:
        # though unique...
        # eliminating the duplicates and remaining with single unique entries
        # then compiling the result to a list...
        if not self.articles():
            return []
        return list(set(article.author for article in self.articles()))

    def contributing_authors(self)->list:
        # for authors who have written more than two articles for the magazine...
        # thus... checking the number of articles each author has written
        if not self.contributors():
            return []
        return [author for author in self.contributors() if len([article for article in self.articles() if article.author == author]) > 2]

    @classmethod
    def top_publisher(cls):
        top_magazine:int = lambda magazine: len(magazine.articles())
        if not Article.all:
            return None
        else:
            return max(cls.magazines, key=top_magazine)

    def __str__(self)->str: 
        return f"Magazine(Name: {self.name}, Category: {self.category})" 
        
    def __repr__(self)->str: 
        return self.__str__()
    
class Author:
    def __init__(self, name:str)->None:
        # ensuring there are no rewrites to the name which is read-only...after initialization
        # immutability if the author's name
        if isinstance(name, str) and len(name) > 0:
            # also ensuring the author's name is a non-empty string...
            self._name:str = name
        else:
            # we'll have to error out...
            # expecting the author's name to be a string... more so a non-empty string
            raise ValueError("error: Author name must be a string, more so a non-empty string.")

    @property
    def name(self)->str:
        return self._name
    
    def articles(self)->list:
        # returning all the articles written by the author...
        # which will involve -> checking and matching... if they correspond we return
        return [article for article in Article.all if article.author == self]

    def magazines(self)->list:
        # retrieving the magazines the author has contributed to...
        # also -> ensuring the returned items are unique, no duplicates.
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine:Magazine, title:str): # returns -> Article, an article instance
        # the instance is associated with the author and the given magazine...
        return Article(self, magazine, title)

    def topic_areas(self)->list:
        # if no value -> returning an empty list, instead of None...
        # makes it more consistent 😉
        if not self.articles():
            return []
        # areas where the author has contributed to...
        return list(set(article.magazine.category for article in self.articles()))

    def __str__(self)->str:
        return f"Author(Name: {self.name})"

    def __repr__(self)->str:
        return self.__str__()

    def print_author(self):
        print(self)

class Article:
    # list to hold all the articles...
    all:list = []

    def __init__(self, author:Author, magazine:Magazine, title:str)->None:
        if isinstance(title, str) and 5 <= len(title) <= 50:
            # title validation and ensuring immutability -> title should be read-only!
            self._title:str = title
        else:
            raise ValueError("error: Title must be a string between 5 and 50 characters long...")

        self._author:Author     = author
        self._magazine:Magazine = magazine
        self.__class__.all.append(self)

    @property
    def title(self)->str:
        return self._title
    
    @property
    def author(self)->Author:
        return self._author
    
    @author.setter
    def author(self, value:Author)->None:
        # Ensuring the author is an instance of the author class...
        if not isinstance(value, Author):
            raise ValueError("error: Author must be an instance of the Author Class!")
        else:
            self._author = value
    
    @property
    def magazine(self)->Magazine:
        return self._magazine
    
    @magazine.setter
    def magazine(self, value:Magazine)->None:
        # Ensuring that the magazine is an instance of the magazine class...
        if not isinstance(value, Magazine):
            raise ValueError("error: Magazine must be an instance of the Magazine Class!")
        else:
            self._magazine = value

    def __str__(self)->str: 
        return f"Article(Title: {self.title}, Author: {self.author.name}, Magazine: {self.magazine.name})" 
    
    def __repr__(self)->str:
        return self.__str__()

magazine = Magazine("Daily Planet", "Technology")
author = Author("Israel Mafabi Emmanuel")
# author.print_author()

article_1 = author.add_article(magazine, "Personal wellness in the Digital Age")
article_2 = author.add_article(magazine, "The Future of Ai")
article_3 = author.add_article(magazine, "Learning with Ai")

print(magazine.article_titles())
print(magazine.contributors())
print(magazine.contributing_authors())
print(author.magazines())
print(author.articles())
print(author.topic_areas())
print(magazine.top_publisher())