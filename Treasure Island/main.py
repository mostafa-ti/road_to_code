treasure = r'''
  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

'''

#print(treasure)
print("Welcome to Treasure Island.  Your mission is to find the treasure.")
path = input("Left or Right?\n").lower()

if not path == "left":
    print("Fall into a hole. Game Over.")
elif path == "left":
    path = input("swim or wait?\n").lower()
    if not path == "wait":
        print("Attacked by trout. Game Over.")
    elif path == "wait":
      path = input("which door?").lower()
      if path == "red":
          print("Burned by fire.Game Over.")
      elif path == "blue":
          print("Eaten by beasts. Game Over.")
      elif path == "yellow":
          print(f"You win!\n{treasure}")
      else:
          print("Game Over.")

print("test")