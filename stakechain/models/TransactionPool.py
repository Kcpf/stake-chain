class TransactionPool:
  def __init__(self):
    self.transactions = []
  
  def add_transaction(self, transaction):
    self.transactions.append(transaction)
  
  def transaction_exists(self, transaction):
    return any(transaction.equals(tx) for tx in self.transactions)
  
  def remove_from_pool(self, transactions):
    new_pool = []
    for pool_transaction in self.transactions:
      insert = True
      
      for transaction in transactions:
        if pool_transaction.equals(transaction):
          insert = False
      
      if insert: new_pool.append(pool_transaction)
    
    self.transactions = new_pool
  
  def forger_required(self):
    return len(self.transactions) >= 3
