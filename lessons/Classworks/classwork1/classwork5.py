movies = [
    {"title": "Начало", "genre": "фантастика"},
    {"title": "Один дома", "genre": "комедия"},
    {"title": "Интерстеллар", "genre": "фантастика"},
]

def pick_movie(movies, genre):
    a = []
    for b in movies:
        if b["genre"] == genre:
            a.append(b["title"])
    return a
pass
print(pick_movie(movies, "фантастика"))
