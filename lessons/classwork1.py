def hero_name(color, animal, superpower="невидимость"):
    return "Капитан " + color.lower() + " " + animal.lower() + " (" + superpower + ")"

pass
print(hero_name("Синий", "Енот"))
print(hero_name("Красный", "Тигр", "суперсила"))
print(hero_name(color="Белый", animal="Кот", superpower="полет"))
