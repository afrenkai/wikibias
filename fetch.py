import wikipediaapi as wp

def fetch_article(title: str) -> str:
    print(f"Fetching article: {title}")

    wiki = wp.Wikipedia(
        user_agent='WikiBias (sundai@mit.edu)',
        language='en',
        extract_format=wp.ExtractFormat.WIKI
    )

    text = wiki.page(title).text
    
    return text.split("Notes")[0]

# if __name__ == "__main__":
#     fetch_article("Python (programming language)")