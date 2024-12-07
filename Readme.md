# Publishing System Project 

# By Israel Mafabi Emmanuel

## Description
This project implements a basic publishing system with three main classes: 

- `Magazine`
-  `Author`
-  `Article`

The system allows magazines to keep track of their published articles and contributors, authors to manage their articles and view the magazines they have contributed to, and articles to associate authors with magazines.

## Features
- **Magazine Class**:
  - Manage a list of magazines.
  - Track published articles, article titles, contributors, and contributing authors.

- **Author Class**:
  - Manage authors' details.
  - Track articles written by the author.
  - View magazines the author has contributed to.
  - Add new articles.
  - Track topic areas the author has contributed to.

- **Article Class**:
  - Manage articles' details.
  - Track authors and magazines associated with articles.

## Getting Started

### Prerequisites
- Python 3.6+

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Emmanuel-Mafabi-Israel/mafabi-articles.git
    ```
2. Navigate to the project directory:
    ```bash
    cd mafabi-articles
    ```

## Usage

### Creating a Magazine
```python
# Create a new magazine instance
# Publisher Name, Category
magazine_1 = Magazine("Daily Planet", "Technology")
magazine_2 = Magazine("Health and Mafabi", "Health")
```

### Creating an Author

```python
# Create a new author instance
author = Author(name="Israel Mafabi Emmanuel")
```

### Adding an Article

```python
# Add a new article
article_1 = author.add_article(magazine_1, "The Future of AI")
article_2 = author.add_article(magazine_2, "Personal Wellness in the Digital Age")
```

### Retrieving Information

```python
# Get articles published in a magazine
print(magazine_1.article_titles())

# Get the contributors and contributing authors from the magazines - magazine_1
print(magazine_1.contributors())
print(magazine_1.contributing_authors())

# Get author contributions...
print(author.magazines())
print(author.articles())
print(author.topic_areas())
```



### **Enjoy the Project!!!**

Feel free to reach out... 🤭😍😉

Made with Love... 😎

More so, Glory to God!!!