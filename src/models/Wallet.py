from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from src.models.BlockchainUtils import BlockchainUtils
from src.models.Transaction import Transaction

class Wallet:
  def __init__(self):
    self.key_pair = RSA.generate(2048)

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
