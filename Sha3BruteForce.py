from web3 import *
from hexbytes import *

for i in range(0,256):
    a = Web3.soliditySha3(['uint8'],[i])    
    print(i,a)
    if a == HexBytes('0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365'):
        print(f'The answer is {i}')
        break
