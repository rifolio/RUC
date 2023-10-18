#Code authors: Frederik Christian Klee, Vladyslav Horbatenko, Lucie Navrátilová

import hashlib, json, server_client
from time import time
from threading import Thread
from socket import gethostname

class Blockchain():
    chain = [] # Where blocks are stored.
    header_hashes = [] # Hash of each block in the chain is stored here.
    pending_credentials = [] # Credentials to be stored in the next block.

    # Modified version of Michael Chrupcala's work. Source: https://github.com/mchrupcala/blockchain-walkthrough
    # Initial method to be executed when class is instantiated as an object.
    def __init__(self, proof_difficulty):
        self.difficulty = "0" * proof_difficulty # The length of this string depends on the proof_difficulty int.
        self.chain.append(self.new_block(proof=None, previous_hash=None)) # Creates genesis block.
        self.header_hashes.append(self.hash(self.chain[0])) # Creates hash of genesis block and adds it to the header_hashes list.

    # Modified version of Michael Chrupcala's work. Source: https://github.com/mchrupcala/blockchain-walkthrough
    # Creates a block object for storing in the blockchain.
    def new_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'credentials': self.pending_credentials,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_credentials = []
        return block

    # Verifies the proof for the latest block using the given nonce.
    def verify_proof(self, nonce):
        proof = hashlib.sha256(self.header_hashes[len(self.header_hashes) - 1].encode() + str(nonce).encode()).hexdigest()
        if proof[:len(self.difficulty)] == self.difficulty:
            return True
        else:
            return False
    
    # Adds the given block to the blockchain if its proof is valid.
    def append_block_if_proof(self, block):
        if self.verify_proof(block["proof"]):
            self.chain.append(block)
            self.header_hashes.append(self.hash(block))
            return True
        else:
            return False

    # A composed method for executing the task of adding/mining a block to the blockchain.
    # Intended to be the main function for adding/mining blocks.
    def mine_block(self):
        new_block = self.new_block(proof=self.proof_of_work(), previous_hash=self.header_hashes[-1])
        self.append_block_if_proof(new_block)
        return True

    # Modified version of Michael Chrupcala's work. Source: https://github.com/mchrupcala/blockchain-walkthrough
    # Creates a dict containing information about a person with credentials.
    def new_credentials(self, name, identification, date_of_birth):
        credentials = {
            'name': name,
            'identification': identification,
            'date of birth': date_of_birth
        }
        self.pending_credentials.append(credentials) # Adds it to the list, waiting for a block to be mined/added.
        return True

    # Modified version of Michael Chrupcala's work. Source: https://github.com/mchrupcala/blockchain-walkthrough
    # Turns an object into a hexidecimal string which represents the hash of that object.
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        return raw_hash.hexdigest()
    
    # Prints all information contained in every block on the blockchain.
    def print_info(self):
        for i in self.chain:
            for u in i:
                print(u + ":", i[u])

    # Returns the block object using its index value.
    def get_block(self, n):
        return self.chain[n]

    # Compares the hashes of two given blocks.
    def compare_hash(self, block1, block2):
        return self.hash(block1) == self.hash(block2)

    # Validates the entire blockchain by comparing the stored "previous_hash" in a block to the calculated hash of the previous block.
    def validate_chain(self):
        for i in range(len(self.chain) - 1):
            if self.chain[i+1]["previous_hash"] != self.hash(self.chain[i]):
                return False
        return True
    
    # Calculates the required hash for mining a block.
    # Returns the nonce required to verify the proof.
    def proof_of_work(self):
        block_hash = self.header_hashes[-1]
        hash_iteration = ""
        nonce = -1
        while hash_iteration[:len(self.difficulty)] != self.difficulty:
            nonce += 1
            hash_iteration = hashlib.sha256(block_hash.encode() + str(nonce).encode()).hexdigest()
        return nonce

class Blockchain_network(Blockchain):
    # Creates a server as an attribute of the class.
    # It'll boot up the server. and wait for clients to connect.
    def start_server(self, port):
        self.SERVER = server_client.P2P_server(port)
        self.SERVER.run_server()
        return self.SERVER.new_clients_handler()

    # Creates a client as a socket object and connects to a server.
    # Returns the socket as the object itself IS the connection,
    # and makes us able to send data to specific clients at will.
    def start_client(self, address, port):
        CLIENT = server_client.P2P_client(port)
        CLIENT.connect_to_network((address, port))
        CLIENT.client_handler()
        return CLIENT

    # Connects to all servers in a server list at once.
    # server_list argument must be a dict.
    def connect_to_servers(self, server_list, client_list):
        for i in server_list:
            client_list.append(self.start_client(i, server_list[i]))

    # Sends the entire local server blockchain to a client.
    # JSON casts the entire blockchain to a string,
    # so it can be sent through the socket.
    def send_blockchain(self, client):
        data = json.dumps(self.chain)
        print("Sending blockchain to:", client.object_socket.getpeername())
        client.send_data(data)
        print("Blockchain sent to:", client.object_socket.getpeername())

    # Same as send_blockchain(), but here it's sent to all connected clients.
    def send_blockchain_to_all(self, clients):
        for i in clients:
            self.send_blockchain(i)

    # Parses received data and returns it. 
    # In this case it'll be a blockchain string parsed to a blockchain list.
    def parse_received_blockchain(self, index):
        while True:
            if self.SERVER.communications[index]:
                print("Replacing old blockchain with new one...")
                self.chain = json.loads(self.SERVER.communications[index])
                print("Old blockchain replaced!")
                print("Hash for new blockchain:", self.hash(self.chain))
                return True

    # Threader for the parse_received_blockchain() function.
    # Functions the same way as any of the other threader functions.
    def blockchain_handler(self, index):
        t = Thread(target=self.parse_received_blockchain, args=(index,))
        t.start()
        return t

    # Composed method. Calling this is a more convenient way to start up the blockchain network.
    # Arguments must be port you want to use for your server and the dict of server you wants connect to.
    def blockchain_network_startup(self, port, server_list):
        clients = []
        print("Local blockchain hash:", self.hash(self.chain))
        server_thread = self.start_server(port)
        self.connect_to_servers(server_list, clients)
        return server_thread, clients

if __name__ == "__main__":
    # Function for testing if the blokchain network can receive data from a peer, in this case a complete blockchain.
    def test_peer_receiver(server_list):
        # Creates a blockchain network.
        my_blockchain = Blockchain_network(proof_difficulty=6)
        # Boots up the server for the blockchain network and connects to the given servers using client objects.
        server_thread, clients = my_blockchain.blockchain_network_startup(1111, server_list)
        blockchain_thread = my_blockchain.blockchain_handler(0) # Thread for parsing and printing the new blockchain.

        # Function for testing if the blokchain network can send a blockchain to another peer.
    def test_peer_sender(server_list):
            their_blockchain = Blockchain_network(proof_difficulty=5)
            their_blockchain.new_credentials("Roland", "21857", "10.03.00")
            their_blockchain.mine_block()
            their_blockchain.new_credentials("John", "21865", "15.04.00")
            their_blockchain.mine_block()
            their_blockchain.new_credentials("Mike", "21888", "21.01.96")
            their_blockchain.mine_block()
            server_thread2, clients2 = their_blockchain.blockchain_network_startup(1112, server_list)
            their_blockchain.send_blockchain_to_all(clients2) # Sends a copy of the host's blockchain to all connected peers.

    # gethostname() will return your own IPv4-address, basically connecting to a different server on your own machine.
    # gethostname() can be replaced with any IPv4-address (string) you wish to connect to,
    # but it has to be available on your local network.
    # These functions are intended to be run seperately in each of their own terminals,
    # since the first function call will block the next one. They are not required to be called in a particular order.
    test_peer_receiver({'172.20.10.7': 1112})
    # test_peer_sender({'172.20.10.12' : 1111})