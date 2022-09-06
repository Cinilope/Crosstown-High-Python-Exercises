

import random
def main():
  RhymingNouns = [ "food", "mood", "dude", "lewd"]
  RhymingAdj = ["Happy", "crappy", "flappy", "slappy"]
  for _ in range(10):
      rhymeWords = [random.choice(RhymingAdj), random.choice(RhymingNouns),random.choice(RhymingAdj), random.choice(RhymingNouns)]
      print("Yo, I am a " + rhymeWords[0] +  " " + rhymeWords[1] + " in the "+ rhymeWords[2] +  " " + rhymeWords[3])

if __name__ == "__main__":
    main()