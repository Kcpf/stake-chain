from src.models.Block import Block
from src.models.BlockchainUtils import BlockchainUtils
from src.models.AccountModel import AccountModel
from src.models.PoS import ProofOfStake

class Blockchain:
  def __init__(self):
    self.blocks = [Block.genesis()]
    self.account_model = AccountModel()
    self.pos = ProofOfStake()
  
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

    if transaction.type == 'STAKE':
      if sender == receiver:
        self.pos.update(sender, amount)
        self.account_model.update_balance(sender, -amount)
    else:
      self.account_model.update_balance(sender, -amount)
      self.account_model.update_balance(receiver, amount)
  
  def next_forger(self):
    last_block_hash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()

    return self.pos.forger(last_block_hash)
  
  def create_block(self, transactions_from_pool, forger_wallet):
    covered_transactions = self.get_covered_transaction_set(transactions_from_pool)
    self.execute_transactions(covered_transactions)

    new_block = forger_wallet.create_block(
      covered_transactions, 
      BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(),
      len(self.blocks)
    )
    self.blocks.append(new_block)
    
    return new_block
  
  def transaction_exists(self, transaction):
    for block in self.blocks:
      for block_transaction in block.transactions:
        if transaction.equals(block_transaction): return True
    
    return False
  
  def forger_valid(self, block):
    return self.pos.forger(block.last_hash) == block.forger
  
  def transactions_valid(self, transactions):
    covered_transactions = self.get_covered_transaction_set(transactions)

    return len(transactions) == len(covered_transactions)
