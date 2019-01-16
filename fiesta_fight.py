
class Character:

    def __init__(self, name):
        self.name = name
        self.health = 1.0

    def speak(self):
        return str("hello, I'm " + self.name)


def main():
    justin = Character("Justin")
    print(justin.speak())


if __name__ == "__main__":
    main()
