from __future__ import annotations

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 12},
    {"name": "Cavin", "age": 17, "number": 3},
]


def repr_players(
    players: list[dict], sorted: bool = False, keyword: str | None = "number"
) -> None:
    print("TEAM:")
    if sorted:
        players.sort(key=lambda x: x[keyword])
    for pl in players:
        print(f"\t{pl['number']} Name:{pl['name']} Age:{pl['age']}")
    print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <-")


def add_player(players: list[dict], num: int, name: str, age: int) -> None:
    if num not in [player["number"] for player in players]:
        player = {"name": name, "age": age, "number": num}
        team.append(player)
        log(message=f"Adding {player['name']}")
    else:
        log(message=f"There is already a player with #{num}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def update_player(players: list[dict], num: int, name: str, age: int) -> None:
    index = 0
    while True:
        if index == len(players):
            log(message=f"There is no a player with #{num} to update")
            break

        elif num == players[index]["number"]:
            players[index]["name"] = name
            players[index]["age"] = age
            log(message=f"Update player with #{num}")
            break

        else:
            index += 1
            continue


def main():
    repr_players(team)

    add_player(team, num=10, name="Carl", age=31)
    add_player(team, num=18, name="Bob", age=29)
    remove_player(players=team, num=17)

    repr_players(team, True)

    add_player(team, num=18, name="Voo", age=3)
    add_player(team, num=10, name="Serg", age=26)
    update_player(team, num=101, name="Fill", age=55)
    update_player(team, num=12, name="Fill", age=55)

    repr_players(team, True, "name")


if __name__ == "__main__":
    main()
