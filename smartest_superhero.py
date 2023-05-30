import requests

def smartest_superhero(superheroes):
    url = "https://akabab.github.io/superhero-api/api"
    all_heroes = "/all.json"
    response = requests.get(url=url+all_heroes)
    heroes_int = []
    for hero_data in response.json():
        if superheroes == []:
            break
        elif hero_data["name"] in superheroes:
            heroes_int += [(hero_data["name"], hero_data["powerstats"]["intelligence"])]
            superheroes.remove(hero_data["name"])
    smart_hero = max(heroes_int, key=lambda i : i[1])[0]
    return smart_hero

superheroes = ["Hulk", "Captain America", "Thanos"]
print(smartest_superhero(superheroes))