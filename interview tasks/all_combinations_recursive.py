# Задача: получение всех комбинаций различных сущностей произвольного количества


def get_combination(*rest, context=None):
    if context is None:
        context = []
    if not rest:
        yield context
        return
    head, *local_rest = rest
    for item in head:
        local_context = [item] + context
        yield from get_combination(*local_rest, context=local_context)


# Пример использования

cities = ['Moscow', 'London', 'Paris', 'Verona']
ages = list(range(18, 26))
genders = ['F', 'M']

all_combinations = [combination for combination in get_combination(cities, ages, genders)]
print(all_combinations)
print('{} combinations expected, {} generated'.format(len(all_combinations), len(cities) * len(ages) * len(genders)))
