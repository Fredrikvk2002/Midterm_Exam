def count_pattern_matches(text):
    """
    Counts words that start with 'un' and end with 'an'.

    :param text: The input text (string)
    :return: The count of matching words
    """
    words = text.split()  # Split text into words
    count = 0  # Counter for matches

    for word in words:
        if word.startswith("un") and word.endswith("an"):
            count += 1  # Increase count if pattern is found

    return count  # Return the number of matches


# Example usage:
text = "unknown unhuman unitarian underan urban unusual unplan"
print(count_pattern_matches(text))  # Output: 3
