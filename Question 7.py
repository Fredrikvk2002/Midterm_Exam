def calculate_days_since_birth(birthday):
    """
    Calculates how many whole years have passed since birth and converts to days.

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: Number of days passed (whole years only)
    """

    # Extract the birth year from the last 4 characters of the input string
    birth_year = int(birthday[-4:])

    # Set the current year (since we can't use imports)
    current_year = 2025

    # Calculate the number of whole years passed (excluding birth year and current year)
    years_passed = current_year - birth_year - 1

    # Convert years to days (assuming 365 days per year)
    days_passed = years_passed * 365

    # Return the total number of days
    return days_passed
