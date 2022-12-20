def func(data, city):
    result = list(filter(lambda item: item['city'], city))
    return result