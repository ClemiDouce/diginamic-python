import random


class GuessNumber:
    difficulty = "easy"
    secret_number = 0
    try_count = 0
    player_number = -1

    def start_game(self, difficulty="easy"):
        self.try_count = 0
        self.player_number = -1

        match difficulty:
            case "easy":
                self.secret_number = random.randint(1, 30)
            case "medium":
                self.secret_number = random.randint(1, 100)
            case "hard":
                self.secret_number = random.randint(1, 200)

        while self.player_number != self.secret_number and self.try_count < 6:
            print(f"Essai no {self.try_count}")
            try:
                self.player_number = int(input("Choisissez un nombre: "))
            except ValueError:
                print("Seul une valeur numérique est accepté")
                continue

            if self.player_number < 1 or self.player_number > 30:
                print("Le chiffre doit etre entre 1 et 30")
                continue

            print(f"Votre proposition: {self.secret_number}")
            # Check nombre
            if self.player_number > self.secret_number:
                print("Trop grand")
            elif self.player_number < self.secret_number:
                print("Trop petit")
            else:
                print(f"Vous avez trouvé en {self.secret_number} en {self.try_count} essais !")
                break
            self.try_count += 1
        else:
            print("Nombre d'essais dépassé !")
