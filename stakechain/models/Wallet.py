from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from stakechain.models.BlockchainUtils import BlockchainUtils
from stakechain.models.Transaction import Transaction
from stakechain.models.Block import Block

class Wallet:
  def __init__(self):
    self.key_pair = RSA.generate(2048)
  
  def from_key(self, file):
    key = ''
    
    with open(file, 'r') as key_file:
      key = RSA.import_key(key_file.read())
    
    self.key_pair = key

  def sign(self, data):
    data_hash = BlockchainUtils.hash(data)
    signature = PKCS1_v1_5.new(self.key_pair).sign(data_hash)

    return signature.hex()
  
  @staticmethod
  def signature_validation(data, signature, public_key):
    signature = bytes.fromhex(signature)
    data_hash = BlockchainUtils.hash(data)
    public_key = RSA.importKey(public_key)
    
    return PKCS1_v1_5.new(public_key).verify(data_hash, signature)

  def public_key_export(self):
    return self.key_pair.public_key().exportKey().decode('utf-8')
  
  def create_transaction(self, receiver_public_key, amount, transaction_type):
    transaction = Transaction(self.public_key_export(), receiver_public_key, amount, transaction_type)

    signature = self.sign(transaction.toJson())
    transaction.sign(signature)

    return transaction
  
  def create_block(self, transactions, last_hash, block_count):
    block = Block(transactions, last_hash, self.public_key_export(), block_count)

    signature = self.sign(block.toJson())
    block.sign(signature)

    return block
