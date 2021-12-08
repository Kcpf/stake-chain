import time
import copy


class Block:
  def __init__(self, transactions, last_hash, forger, block_count):
    self.transactions = transactions
    self.last_hash = last_hash
    self.forger = forger
    self.block_count = block_count
    self.timestamp = time.time()
    self.signature = ""
  
  def toJson(self):
    data = {}

    data["last_hash"] = self.last_hash
    data["forger"] = self.forger
    data["block_count"] = self.block_count
    data["timestamp"] = self.timestamp
    data["signature"] = self.signature
    data["transactions"] = [tx.toJson() for tx in self.transactions]

    return data
  
  def payload(self):
    json_representation = copy.deepcopy(self.toJson())
    json_representation["signature"] = ""

    return json_representation
  
  def sign(self, signature):
    self.signature = signature
