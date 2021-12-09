from src.models.Block import Block
from src.models.BlockchainUtils import BlockchainUtils

class Blockchain:
  def __init__(self):
    self.blocks = [Block.genesis()]
  
  def add_block(self, block):
    self.blocks.append(block)
  
  def toJson(self):
    data = {}
    data["blocks"] = [block.toJson() for block in self.blocks]

    return data
  
  def block_count_validation(self, block):
    return self.blocks[-1].block_count == block.block_count - 1
  
  def last_block_hash_validation(self, block):
    latest_block_hash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
    
    return latest_block_hash == block.last_hash