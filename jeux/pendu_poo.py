from wonderwords import RandomWord


class Pendu:
    random_word = ""
    displayed_word = ""
    letter_used = set()
    try_count = 0

    def __init__(self):
        self.r = RandomWord()

    def start_game(self, difficulty="easy"):
        min_length = 0
        max_length = 2
        match difficulty:
            case "easy":
                min_length = 2
                max_length = 5
            case "medium":
                min_length = 5
                max_length = 10
            case "hard":
                min_length = 8
                max_length = 26

        self.random_word = self.r.word(word_min_length=min_length, word_max_length=max_length)
        self.displayed_word = ["_" for char in self.random_word]
        self.try_count = 0
        self.letter_used = set()

        # Debut du jeu
        while "_" in self.displayed_word:
            print(f"Lettres déja utilisé : {self.letter_used}")
            player_input = input("Entrez une lettre ou '?' pour abandonner : ")
            if player_input == "?":
                print("Au revoir !")
                break
            if len(player_input) > 1:
                print("Il faut entrer une lettre")
                continue

            if player_input in self.letter_used:
                print(f"Vous avez déja utilisé la lettre {player_input}")
                continue

            if player_input in self.random_word:
                for index, i in enumerate(self.random_word):
                    if i == player_input:
                        self.displayed_word[index] = player_input
                print(self.displayed_word)
            else:
                print("Cette lettre n'est pas dans le mot a trouver")

            self.letter_used.add(player_input)
            self.try_count += 1
        else:
            print(f"Bravo, vous avez trouvé en {self.try_count} essais")
