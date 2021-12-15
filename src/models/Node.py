from src.models.TransactionPool import TransactionPool
from src.models.Wallet import Wallet
from src.models.Blockchain import Blockchain
from src.models.SocketCommunication import SocketCommunication
from src.models.BlockchainUtils import BlockchainUtils
from src.models.Message import Message
from src.models.NodeAPI import NodeAPI

class Node:
  def __init__(self, ip, port):
    self.p2p = None
    self.ip = ip
    self.port = port
    self.transaction_pool = TransactionPool()
    self.wallet = Wallet()
    self.blockchain = Blockchain()
  
  def start_p2p(self):
    self.p2p = SocketCommunication(self.ip, self.port)
    self.p2p.start_socket_communication(self)
  
  def start_api(self, api_port):
    self.api = NodeAPI()
    self.api.inject_node(self)
    self.api.start(api_port)
  
  def handle_transaction(self, transaction):
    data = transaction.payload()
    signature = transaction.signature
    signer_public_key = transaction.sender_public_key

    signature_valid = Wallet.signature_validation(data, signature, signer_public_key)
    transaction_exists = self.transaction_pool.transaction_exists(transaction)

    if (not transaction_exists) and signature_valid:
      self.transaction_pool.add_transaction(transaction)
      
      message = Message(self.p2p.socket_connector, 'TRANSACTION', transaction)
      encoded_message = BlockchainUtils.encode(message)
      self.p2p.broadcast(encoded_message)
