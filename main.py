from pprint import pprint

from src.models.Transaction import Transaction
from src.models.Wallet import Wallet
from src.models.TransactionPool import TransactionPool
from src.models.Block import Block
from src.models.Blockchain import Blockchain
from src.models.BlockchainUtils import BlockchainUtils

if __name__ == '__main__':
  sender = "sender"
  receiver = "receiver"
  amount = 1
  transaction_type = "TRANSFER"

  wallet = Wallet()
  pool = TransactionPool()
  blockchain = Blockchain()

  transaction = wallet.create_transaction(receiver, amount, transaction_type)

  if not pool.transaction_exists(transaction): 
    pool.add_transaction(transaction)
  
  last_hash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
  block_count = blockchain.blocks[-1].block_count + 1
  block = wallet.create_block(pool.transactions, last_hash, block_count)

  if blockchain.last_block_hash_validation(block) and blockchain.block_count_validation(block): 
    blockchain.add_block(block)

  pprint(blockchain.toJson())
