class TransactionPool:
  def __init__(self):
    self.transactions = []
  
  def add_transaction(self, transaction):
    self.transactions.append(transaction)
  
  def transaction_exists(self, transaction):
    return any(transaction.equals(tx) for tx in self.transactions)