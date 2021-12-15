from stakechain.models.PoS import ProofOfStake
from stakechain.models.Lot import Lot
import string
import random

def get_random_string(length):
  letters = string.ascii_lowercase
  
  return ''.join(random.choice(letters) for _ in range(length))

if __name__ == '__main__':
  pos = ProofOfStake()
  pos.update('bob', 100)
  pos.update('alice', 100)

  bob_wins = 0
  alice_wins = 0

  for i in range(100):
    forger = pos.forger(get_random_string(i))
    if forger == 'bob':
      bob_wins += 1
    else:
      alice_wins += 1
  
  print(bob_wins, alice_wins)
