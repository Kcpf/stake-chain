from src.models.Block import Block
from src.models.BlockchainUtils import BlockchainUtils
from src.models.AccountModel import AccountModel


class Blockchain:
  def __init__(self):
    self.blocks = [Block.genesis()]
    self.account_model = AccountModel()
  
  def add_block(self, block):
    self.execute_transactions(block.transactions)
    self.blocks.append(block)
  
  def toJson(self):
    data = {}
    data["blocks"] = [block.toJson() for block in self.blocks]

    return data
  
  def block_count_validation(self, block):
    return self.blocks[-1].block_count == block.block_count - 1
  
  def last_block_hash_validation(self, block):
    latest_block_hash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
    
    return latest_block_hash == block.last_hash
  
  def get_covered_transaction_set(self, transactions):
    covered_transactions = []

    for transaction in transactions:
      if self.transaction_covered(transaction):
        covered_transactions.append(transaction)
      else:
        print("Transaction is not covered")
      
    return covered_transactions
  
  def transaction_covered(self, transaction):
    if transaction.type == "EXCHANGE": return True 

    sender_balance = self.account_model.get_balance(transaction.sender_public_key)

    return sender_balance >= transaction.amount

  def execute_transactions(self, transactions):
    for transaction in transactions:
      self.execute_transaction(transaction)
  
  def execute_transaction(self, transaction):
    sender = transaction.sender_public_key
    receiver = transaction.receiver_public_key
    amount = transaction.amount

    self.account_model.update_balance(sender, -amount)
    self.account_model.update_balance(receiver, amount)
