from hashlib import sha512
import hashlib
import random
import datetime
length = 8

#CREATING BLOCK.
class Block:
    def __init__(this,data,block_no,timestamp,previous_hassh,hashh):
        this.block_no=block_no
        this.noonce=noonce
        this.data=data
        this.timestamp=timestamp
        this.hashh=hashh
        this.previous_hassh=previous_hassh
        
#PRINTING BLOCK.
    def print_block(this):
        print('Block No: ',this.block_no)
        print('Nonce: ',this.noonce)
        print('Message: ',this.data)
        print('Timestamp: ',this.timestamp)
        print('Previous Hash: ',this.previous_hassh)
        print('Hash: ',this.hashh)
        
#TAKING INPUTS.
block_no =int(input("Enter block number: "))
noonce="".join ([str(random.randint(0,9)) for i in range (length)])
#print(noonce)
data = input("Enter a message: ")
timestamp= str(datetime.datetime.now())
#print(timestamp)
previous_hassh=00
hashh_conc= "{}{}{}".format(str(block_no), noonce, str(data), timestamp,previous_hassh)
hashh = hashlib.sha512(hashh_conc.encode()).hexdigest()

#CREATING OBJECT.
b=Block(data,block_no,timestamp,previous_hassh,hashh)
b.print_block()
