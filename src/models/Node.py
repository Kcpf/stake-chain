from src.models.TransactionPool import TransactionPool
from src.models.Wallet import Wallet
from src.models.Blockchain import Blockchain


class Node:
  def __init__(self):
    self.transaction_pool = TransactionPool()
    self.wallet = Wallet()
    self.blockchain = Blockchain()
