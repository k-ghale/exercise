def does_name_exist(first_names, last_names, full_name):
    for first in first_names:
        for last in last_names:
            if first + " " + last == full_name:
                return True

    return False