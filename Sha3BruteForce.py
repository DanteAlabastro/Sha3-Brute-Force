from web3 import *
from hexbytes import *
# ^ HexBytes allows for the type identifier.

# Loop through all uint8 values, 0-255.
for i in range(0,256):
    
# It is important to hash the value the same way Solidity would.
# You must declare the value as a uint8 as it will change the resulting hash.
    a = Web3.soliditySha3(['uint8'],[i])
    
# Unneccary but provides nice feedback. Does not print value as hexbyte!
    print(i,a)
    
# The hash of the secret number goes here.
    if a == HexBytes('0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365'):
        
# Prints the answer and stops.
        print(f'The answer is {i}')
        break
