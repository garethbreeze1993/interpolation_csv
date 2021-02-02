from typing import List


def get_interpolate_value(coordinates: List[int], overall_list: List[List]) -> float:
    """
    Function which takes in a 'coordinate' and a structure of the values as a list of lists and gets the non diagonal
    values around them and calculates the interpolated values.
    :param coordinates: A list of ints which says which the first index
    denotes which the row of the missing value and the second index is the column e.g. [0, 2]
    is the first inner list and the 3rd item of that inner list
    :param overall_list: A list of lists which says the overall structure of the values
    :return:
    """
    one = (coordinates[0] + 1, coordinates[1])
    two = (coordinates[0] - 1, coordinates[1])
    three = (coordinates[0], coordinates[1] + 1)
    four = (coordinates[0], coordinates[1] - 1)

    first_list = []
    list_of_vals = []

    for x, y in [one, two, three, four]:
        if x >= 0 and y >= 0:
            first_list.append((x, y))

    for x_co, y_co in first_list:
        try:
            value = overall_list[x_co][y_co]
        except IndexError:
            continue
        else:
            list_of_vals.append(float(value))

    interpolated_val = sum(list_of_vals) / len(list_of_vals)
    return interpolated_val


def get_new_csv_structure(overall_list: List[List]) -> List[List]:
    """
    Goes through the list of lists and if the value is 'nan' calls the get_interpolate_value to get the
    new interpolated value
    for that index and replaces the nan value with the interpolated value
    :param overall_list: a list of lists
    :return:
    """
    for index, row in enumerate(overall_list):
        for index_inner, value in enumerate(row):
            if value == 'nan':
                new_value = get_interpolate_value(coordinates=[index, index_inner], overall_list=overall_list)
                overall_list[index][index_inner] = new_value

    return overall_list
