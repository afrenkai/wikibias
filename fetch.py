import wikipediaapi as wp

def fetch_article(title):
    wiki = wp.Wikipedia(
        user_agent='WikiBias (sundai@mit.edu)',
        language='en',
        extract_format=wp.ExtractFormat.WIKI
    )

    page = wiki.page(title)
    return page

# if __name__ == "__main__":
#     fetch_article("Python (programming language)")