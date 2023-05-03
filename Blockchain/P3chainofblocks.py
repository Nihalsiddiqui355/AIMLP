import hashlib 
import random 
import datetime

class Block:
    def __init__(self, data, Id, previous_hash):
        self.Id = Id
        self.data = str(data)
        self.nonce = random.randint(10000, 99999)
        self.hash = hashlib.sha256((self.data + str(self.nonce)).encode())
        self.hash = self.hash.hexdigest()
        self.timestamp = str(datetime.datetime.now())
        self.previous_hash = previous_hash
        print("Block Id: {}".format(self.Id))
        print("Block Data: {}".format(self.data))
        print("Block Previous hashcode: {}".format(self.previous_hash))
        print("Block Nonce: {}".format(self.nonce))
        print("Block Timestamp: {}".format(self.timestamp))
        print("Block Hash: {}".format(self.hash))
        print("\n")

    def getHash(self):
        hash = hashlib.sha256((str(self.previous_hash) + str(self.Id)
        + self.data + str(self.nonce) + str(self.timestamp)).encode())
        hash = hash.hexdigest()
        return hash

def genesis_hash():
    zero_hash = []
    for x in range(64):
        zero_hash.append("0")
    zero_hash = str("".join(zero_hash))
    return zero_hash

Block_No = int(input("Enter the number of blocks in blockchain: "))

for i in range(1, Block_No+1):
    if i == 1:
        Data = input("Enter Transaction Data: ")
        previous_hash = genesis_hash()
        BlockName = "Block " + str(i)
        print(BlockName)
    else:
        BlockName = Block(Data, i, previous_hash)
        Data = input("Enter Transaction Data: ")
        previous_hash = BlockName.hash
        BlockName = "Block " + str(i)
        print(BlockName)
        BlockName = Block(Data, i, previous_hash)
