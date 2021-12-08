from src.models.Transaction import Transaction
from src.models.Wallet import Wallet
from src.models.TransactionPool import TransactionPool

if __name__ == '__main__':
  sender = 'sender'
  receiver = 'receiver'
  amount = 1
  transaction_type = "TRANSFER"

  wallet = Wallet()
  pool = TransactionPool()

  transaction = wallet.create_transaction(receiver, amount, transaction_type)

  signature_validation = Wallet.signature_validation(transaction.payload(), transaction.signature, wallet.public_key_export())

  if not pool.transaction_exists(transaction): 
    pool.add_transaction(transaction)
  
  if not pool.transaction_exists(transaction): 
    pool.add_transaction(transaction)
  
  print(pool.transactions)