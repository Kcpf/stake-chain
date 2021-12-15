from pprint import pprint
import sys

from src.models.Transaction import Transaction
from src.models.Wallet import Wallet
from src.models.TransactionPool import TransactionPool
from src.models.Block import Block
from src.models.Blockchain import Blockchain
from src.models.BlockchainUtils import BlockchainUtils
from src.models.AccountModel import AccountModel
from src.models.Node import Node

if __name__ == '__main__':
  ip = sys.argv[1]
  port = int(sys.argv[2])
  
  node = Node(ip, port)
  node.start_p2p()
