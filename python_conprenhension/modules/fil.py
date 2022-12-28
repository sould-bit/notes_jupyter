# %%
#funcion  toma dos parametros  y filtra un dic 
def func(data, city):
    result = list(filter(lambda item: item['city'] == city, data  ))
    return result








