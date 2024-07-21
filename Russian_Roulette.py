import random


class Gun:
    def __init__(self, chambers: int):
        self.chambers = chambers
        self.bullet_chamber = random.randint(1, self.chambers)

    def pull_trigger(self, chamber):
        return self.bullet_chamber == chamber


class Player:
    def __init__(self, name: str):
        self.name = name
        self.is_alive = True


def create_players():
    players = []
    number_of_players = int(input("Wie viele Spieler gibt es? "))
    for i in range(number_of_players):
        name = input(f"Wie heißt Spieler {i + 1}? ")
        players.append(Player(name))
    return players


def play_game(players, gun):
    current_chamber = 1
    while len([player for player in players if player.is_alive]) > 1:
        for player in players:
            if player.is_alive:
                print(f"{player.name} ist an der Reihe. Drücke den Abzug...")
                input("Drücke Enter, um den Abzug zu ziehen...")
                if gun.pull_trigger(current_chamber):
                    print(f"{player.name} wurde erschossen!\n")
                    player.is_alive = False
                    return
                else:
                    print("Klick! Glück gehabt.\n")
                current_chamber = current_chamber + 1 if current_chamber < gun.chambers else 1
                input("Drücke Enter, um fortzufahren...")
    print("Spiel beendet. Überlebende Spieler:")
    for player in players:
        if player.is_alive:
            print(player.name)


if __name__ == '__main__':
    gun = Gun(6)
    players = create_players()
    play_game(players, gun)
