from stakechain.models.Wallet import Wallet
from stakechain.models.BlockchainUtils import BlockchainUtils
import requests

def post_transaction(sender, receiver, amount, type):
  transaction = sender.create_transaction(receiver.public_key_export(), amount, type)
  url = 'http://localhost:5000/transaction'
  package = { "transaction": BlockchainUtils.encode(transaction) }
  request = requests.post(url, json=package)


if __name__ == "__main__":
  bob = Wallet()
  alice = Wallet()
  alice.from_key('./keys/stakerPrivateKey.pem')
  exchange = Wallet()

  post_transaction(exchange, alice, 100, "EXCHANGE")
  post_transaction(exchange, bob, 100, "EXCHANGE")
  post_transaction(exchange, bob, 100, "EXCHANGE")
  
  post_transaction(alice, alice, 25, "STAKE")
  post_transaction(alice, bob, 1, "TRANSFER")
  post_transaction(alice, bob, 1, "TRANSFER")

  print(request.text)
