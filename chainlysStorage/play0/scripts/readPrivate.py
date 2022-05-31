from brownie import web3, accounts, config, PrivateExploit


password="0x1234567890123456789012345678901234567890123456789012345678903132"

def deploy_1():
    account = accounts[0]
    simple_storage = PrivateExploit.deploy(1,password,{"from": account})
    print(f"deploy done ; from={account} ; simple_storage={simple_storage}")

def getStorage():
    simple_storage = PrivateExploit[-1] 
    print(simple_storage)
    # a=web3.eth.getStorageAt(str(simple_storage),0)[-20:].hex()
    for i in range(0,10):
        a=web3.eth.getStorageAt(str(simple_storage),i).hex()
        print(f"slot #{i} = {a}")
    

def main():
    deploy_1()
    getStorage()

