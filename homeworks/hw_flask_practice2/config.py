class Config:
    BLOG_TITLE = "Blog Cursor"
    MENU_ITEMS = [
        {
            "name": "Articles",
            "link": "/articles",
        },
        {
            "name": "Categories",
            "link": "/categories",
        },
    ]

    FOOTER_LINKS = [
        {
            "name": "Articles",
            "link": "/articles",
        },
        {
            "name": "Categories",
            "link": "/categories",
        },
        {
            "name": "About us",
            "link": "/aboutus",
        },
        {
            "name": "Questions",
            "link": "/questions",
        },
    ]


def articles():
    return [
        {
            "title": "Test Article",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": "test-article"
        },
        {
            "title": "Test Article2",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": "test-article2"
        },
    ]


def foot_cat():
    return {
        "img": "https://www.cats.org.uk/media/2297/tabby-cat-looking-up.jpg?width=1600"
    }
