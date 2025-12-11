# classes and objects
# Author: Princeton
# Dec 11


from logging import getLogRecordFactory


class Pokemon:
    def __innit__(self):
        self.name = "Pikachu"
        self.type = "Electric"
        self.shiny = False
        self.age = 0
        self.level = 1
        print(f"{self.name} is born!")

    if __name__ == "__main__":
        pokemon_one = Pokemon()
        print("Pokemon name:", pokemon_one.name)
        pokemon_one.name = Gary
