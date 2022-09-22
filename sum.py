def my_list(ki: list):
    assert isinstance(ki, list), "Only list is accepted"
    return sum(ki)


print(my_list([1, 2, 3, 4, 5]))
