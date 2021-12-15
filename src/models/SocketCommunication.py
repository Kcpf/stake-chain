import json
from p2pnetwork.node import Node
from src.models.PeerDiscoveryHandler import PeerDiscoveryHandler
from src.models.SocketConnector import SocketConnector
from src.models.BlockchainUtils import BlockchainUtils


class SocketCommunication(Node):
  def __init__(self, ip, port):
    super(SocketCommunication, self).__init__(ip, port, None)
    self.peers = []
    self.peer_discovery_handler = PeerDiscoveryHandler(self)
    self.socket_connector = SocketConnector(ip, port)

  def connect_to_first_node(self):
    if self.socket_connector.port != 10001:
      self.connect_with_node("localhost", 10001)
  
  def start_socket_communication(self):
    self.start()
    self.peer_discovery_handler.start()
    self.connect_to_first_node()
  
  def inbound_node_connected(self, connected_node):
    self.peer_discovery_handler.handshake(connected_node)

  def outbound_node_connected(self, connected_node):
    self.peer_discovery_handler.handshake(connected_node)

  def node_message(self, connected_node, data):
    message = BlockchainUtils.decode(json.dumps(data))
    
    if message.message_type == 'DISCOVERY':
      self.peer_discovery_handler.handle_message(message)
  
  def send(self, receiver, data):
    self.send_to_node(receiver, data)
  
  def broadcast(self, data):
    self.send_to_nodes(data)
