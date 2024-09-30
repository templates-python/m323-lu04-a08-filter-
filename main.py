def filter_long_words(words):
    """
    Filtert Wörter aus der gegebenen Liste, die mehr als 5 Zeichen lang sind.
    Args:
    - words (list): Eine Liste von Wörtern.
    Returns:
    - list: Eine Liste der Wörter mit mehr als 5 Zeichen.
    """
    # Ihr Code hier
    return list(filter(lambda x: len(x) > 5, words))


if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry', 'date']
    long_words = filter_long_words(words)
    print(long_words)
