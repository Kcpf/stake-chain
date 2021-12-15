from flask_classful import FlaskView, route
from flask import Flask, jsonify, request
from src.models.BlockchainUtils import BlockchainUtils

node = None

class NodeAPI(FlaskView):
  def __init__(self):
    self.app = Flask(__name__)
  
  def start(self, api_port):
    NodeAPI.register(self.app, route_base="/")
    self.app.run(host="localhost", port=api_port)
  
  def inject_node(self, injected_node):
    global node
    node = injected_node

  @route('/info', methods=['GET'])
  def info(self):
    return "This is a communication interface to a blockchain node", 200
  
  @route('/blockchain', methods=['GET'])
  def blockchain(self):
    return node.blockchain.toJson(), 200
  
  @route('/transaction-pool', methods=['GET'])
  def transaction_pool(self):
    transactions = {}
    for ctr, transaction in enumerate(node.transaction_pool.transactions):
      transactions[ctr] = transaction.toJson()

    return jsonify(transactions), 200

  @route('/transaction', methods=['POST'])
  def transaction(self):
    values = request.get_json()

    if 'transaction' not in values:
      return "Missing transaction value", 400
    
    transaction = BlockchainUtils.decode(values["transaction"])
    node.handle_transaction(transaction)

    response = { 'message': 'Received transaction' }
    
    return jsonify(response), 201
