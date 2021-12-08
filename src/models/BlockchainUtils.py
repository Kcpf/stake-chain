from Crypto.Hash import SHA256
import json

class BlockchainUtils:
  
  @staticmethod
  def hash(data):
    return SHA256.new(json.dumps(data).encode("utf-8"))
