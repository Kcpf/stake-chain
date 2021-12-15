from src.models.Wallet import Wallet
from src.models.BlockchainUtils import BlockchainUtils
import requests

if __name__ == "__main__":
  bob = Wallet()
  alice = Wallet()
  exchange = Wallet()

  transaction = exchange.create_transaction(alice.public_key_export(), 10, 'EXCHANGE')\
  
  url = 'http://localhost:5000/transaction'
  package = { "transaction": BlockchainUtils.encode(transaction) }
  request = requests.post(url, json=package)

  print(request.text)
