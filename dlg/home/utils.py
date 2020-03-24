def clean_number_list(numbers_to_add):
    """
    Input: a List of numbers to be added together
    Function will clean the list and then return the new list.
    Cleaning involves conversion of string to numbers
    Function will return False if an invalid value has been found
    """

    # Verify that the input is a list
    if not isinstance(numbers_to_add, list):
        return False

    # Build a new list with cleaned values
    numbers_to_add_list = []
    for item in numbers_to_add:
        if isinstance(item, str):
            if item.isdigit():
                numbers_to_add_list.append(int(item))
            else:
                try:
                    float_value = float(item)
                    numbers_to_add_list.append(float_value)
                except Exception as e:
                    # print(type(e))
                    # TODO # Print to log file
                    return False
        if isinstance(item, (int, float)):
            numbers_to_add_list.append(item)

    return (numbers_to_add_list)
