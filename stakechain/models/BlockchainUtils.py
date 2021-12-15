from Crypto.Hash import SHA256
import json
import jsonpickle

class BlockchainUtils:
  
  @staticmethod
  def hash(data):
    return SHA256.new(json.dumps(data).encode("utf-8"))
  
  @staticmethod
  def encode(object_to_encode):
    return jsonpickle.encode(object_to_encode, unpicklable=True)
  
  @staticmethod
  def decode(string_to_decode):
    return jsonpickle.decode(string_to_decode)
