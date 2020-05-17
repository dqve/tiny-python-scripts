letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter,point in zip(letters,points)}
letter_to_points[" "] = 0

letter_to_points = {letter:point for letter,point in zip(letters,points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for char in word:
    point = letter_to_points.get(char,0)
    point_total += point
    #print(char,point,point_total)
  return point_total
  

player_to_words = {}

player_to_words["player1"] = ["BLUE","TENNIS","EXIT"]
player_to_words["wordNerd"] = ["EARTH","EYES","MACHINE"]
player_to_words["Lexi Con"] = ["ERASER","BELLY","HUSKY"]
player_to_words["Prof Reader"] = ["ZAP","COMA","PERIOD"]

player_to_points = {}

for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

def play_word():
  print("Hello there, ready to srabble !!??")
  player_status = input("Are you a new player?\n[a] yes\n[b] no\n>")

  if player_status == "a":
    player_name = input("Are you a new player?\n[a] yes\n[b] no\n>")
  elif player_status == "b":
    g
  else:
    play_word()