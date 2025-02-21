def is_valid_url(url):
    """
    Checks if a given string is a valid URL based on basic rules.

    :param url: The input string to check
    :return: True if it's a valid URL, False otherwise
    """

    # Check if the URL starts with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):

        # Find the first "." after the 8th character (to skip "http://")
        dot_index = url.find(".", 8)

        # Check if there is a "." and it's not the last character
        if dot_index != -1 and dot_index < len(url) - 1:
            return True  # URL is valid

    return False  # URL is invalid

