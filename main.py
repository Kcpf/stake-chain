from pprint import pprint

from src.models.Transaction import Transaction
from src.models.Wallet import Wallet
from src.models.TransactionPool import TransactionPool
from src.models.Block import Block

if __name__ == '__main__':
  sender = "sender"
  receiver = "receiver"
  amount = 1
  transaction_type = "TRANSFER"

  wallet = Wallet()
  pool = TransactionPool()

  transaction = wallet.create_transaction(receiver, amount, transaction_type)

  if not pool.transaction_exists(transaction): 
    pool.add_transaction(transaction)
  
  block = wallet.create_block(pool.transactions, 'last hash', 1)
