DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5
    },
    'pasta': {
        'макароны, г': 200,
        'сыр, г': 50,
        'масло, г': 20
    }
}
from django.http import HttpResponse


def recipe_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    ingredients = DATA.get(dish, {})

    if servings > 1:
        for ingredient, amount in ingredients.items():
            ingredients[ingredient] = amount * servings

    response = '\n'.join([f'{ingredient}: {amount}' for ingredient, amount in ingredients.items()])
    return HttpResponse(response)
