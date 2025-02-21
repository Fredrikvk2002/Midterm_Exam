def calculate_days_since_birth(birthday):
    """
    Calculates how many whole years have passed since birth and converts to days.

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: Number of days passed (whole years only)
    """

    birth_year = int(birthday[-4:])


    current_year = 2025


    years_passed = current_year - birth_year - 1


    days_passed = years_passed * 365

    return days_passed

# Example usage:
print(calculate_days_since_birth("15-08-2002"))

