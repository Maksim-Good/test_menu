from django import template
from trees.models import ChieldMenu, Menu
from django.shortcuts import get_object_or_404 # надо прикрутить к несуществующему айди
register = template.Library()




@register.inclusion_tag('trees/menu.html', takes_context=True)
def draw_menu(context, id, father_id=None, fathers=[]):
    if not id:
        menues = ChieldMenu.objects.filter(father_name=None)
        return {'menues': menues}
    menues = ChieldMenu.objects.filter(father_name=father_id)
    if fathers == []:
        main_menu = ChieldMenu.objects.get(chield_name=id)
        fathers.append(main_menu.chield_name)
        while main_menu.father_name:
            father = main_menu.father_name
            fathers.append(father)
            main_menu = ChieldMenu.objects.get(chield_name=father)
    if father_id is not None and fathers != []:
        fathers.remove(Menu.objects.get(id=father_id))
    return {
        "context": context,
        'id': id,
        'menues': menues,
        'fathers': fathers,
    }
