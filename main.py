import sys
from stakechain.Node import Node

if __name__ == '__main__':
  ip = sys.argv[1]
  port = int(sys.argv[2])
  api_port = int(sys.argv[3])
  key_file = None
  
  if len(sys.argv) > 4:
    key_file = sys.argv[4]
  
  node = Node(ip, port, key_file)
  node.start_p2p()
  node.start_api(api_port)
