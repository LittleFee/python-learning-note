# def city_country(city,country):
#     back=city.title()+', '+country.title()
#     return back
def city_country(city,country,population=None):
    if population:
        back=city.title()+', '+country.title()+' - population '+str(population)
    else:
        back = city.title() + ', ' + country.title()
    return back