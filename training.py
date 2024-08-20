class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0

  def get_choice(self):
    valid_choices = [1, 2, 3]
    while True:
      choice = int(input(f"{self.name}, enter your choice (1: Rock, 2: Paper, 3: Scissors): "))
      if choice in valid_choices:
        return choice
      else:
        print("Please enter a correct choice from 1 to 3")

class Game:
  def __init__(self):
    print("Enter your name, Player 1:")
    player1name = input()
    print("Enter your name, Player 2:")
    player2_name = input()
    self.player1 = Player(player1name)
    self.player2 = Player(player2_name)
    self.choices = ["Rock", "Paper", "Scissors"]

  def play_round(self, round_number):
    choice1 = self.player1.get_choice()
    choice2 = self.player2.get_choice()

    print(f"** Round {round_number} **")
    print(f"{self.player1.name} chooses {self.choices[choice1 - 1]}")
    print(f"{self.player2.name} chooses {self.choices[choice2 - 1]}")

    if choice1 == choice2:
      print("It's a draw!")
    elif (choice1 == 1 and choice2 == 3) or \
         (choice1 == 2 and choice2 == 1) or \
         (choice1 == 3 and choice2 == 2):
      print(f"{self.player1.name} wins this round!")
      self.player1.score += 1
    else:
      print(f"{self.player2.name} wins this round!")
      self.player2.score += 1

  def play_game(self):
    rounds = 4
    for round_number in range(1, rounds + 1): 
      self.play_round(round_number)
      print(f"Score: {self.player1.name} = {self.player1.score}, {self.player2.name} = {self.player2.score}\n")

    if self.player1.score > self.player2.score:
      print(f"{self.player1.name} wins the game!")
    elif self.player2.score > self.player1.score:
      print(f"{self.player2.name} wins the game!")
    else:
      print("The game is a draw!")


game = Game()
game.play_game()