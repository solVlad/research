from brownie import web3, accounts, config, SanctionsList
from Crypto.Hash import keccak
import binascii

blockAddr1="0x0000000000000000000000000000000000000004"
blockList1=["0x1111111111111111111111111111111111111111","0x0000000000000000000000000000000000000004","0x0000000000000000000000000000000000000006"]


def deploy_1():
    account = accounts[0]
    simple_storage = SanctionsList.deploy({"from": account})
    print(f"deploy done ; from={account} ; simple_storage={simple_storage}")


def addSanctioned():
    simple_storage = SanctionsList[-1]  
    print(f"add {blockList1} to Sanctioned")
    print(simple_storage.addToSanctionsList(blockList1))    
    print(simple_storage.tx)    



def isSanctioned():
    simple_storage = SanctionsList[-1]  
    print(f"run isSanctioned on {blockAddr1}")
    print(simple_storage.isSanctioned(blockAddr1))    


def getStorage():
    simple_storage = SanctionsList[-1] 
    print(simple_storage)
    #get first 10
    for i in range(0,10):
        a=web3.eth.getStorageAt(str(simple_storage),i).hex()
        print(f"slot #{i} = {a}")

    # get at key:
    slotOfAddr1=getIntegerStorageForKEY(blockAddr1)
    a=web3.eth.getStorageAt(str(simple_storage),slotOfAddr1).hex()
    print(f"slot #{slotOfAddr1} = {a}")
    # >>> hex(12345)
    # '0x3039'


def getIntegerStorageForKEY(keyHex):
    mappingSLOT=1
    x=web3.soliditySha3(['uint256', 'uint256'], [int(keyHex,16),mappingSLOT]).hex()
    return int(x,16)

def main():
    # calcMapping()
    deploy_1()
    isSanctioned()
    addSanctioned()
    isSanctioned()
    getStorage()

