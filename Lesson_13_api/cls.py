import requests
import random
from time import perf_counter

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 50


def get_pokemon(id_: int) -> str:
    url = BASE_URL + str(id_)
    response = requests.get(url)

    return response.json()["name"]


def get_random_pokemon() -> str:
    rand_id = random.randint(1, MAX_POKEMON + 1)
    return get_pokemon(rand_id)


def main():
    print("=" * 30)

    start = perf_counter()
    random_pokemons = []
    for _ in range(SIZE):
        pokemon = get_random_pokemon()
        random_pokemons.append(pokemon)
    end = perf_counter()
    print(f"Pokemons: {random_pokemons}")
    print(f"Execute time ={start - end}")


if __name__ == "__main__":
    main()
