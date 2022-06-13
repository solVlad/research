from brownie import web3, accounts,Wei, config, simpleBalance


def deploy_1():
    account = accounts[0]
    balance = account.balance()
    print('initial balance of account in Eth ', Wei(balance).to('ether'))

    simple_storage = simpleBalance.deploy({"from": account,"gas_price":0,"value":10000000})
    print(f"deploy done ; from={account} ")

    balance=simple_storage.getBalance()
    print(f"contract.getBalance={balance} = {Wei(balance).to('ether')}")
   
    owner=simple_storage.getOwner()
    print(f"contract.getOwner={owner}")

    web3_contract_storage0=web3.eth.getStorageAt(str(simple_storage),0)[-20:].hex()
    web3_account_balance=web3.eth.getBalance(account.address)
    print(f"web3_contract_storage0={web3_contract_storage0} ; web3_account_balance={web3_account_balance}")
    
    simple_storage.burnSomeValue({"from": account,"value":10000000})

    balance=simple_storage.getBalance()
    print(f"contract.getBalance={balance} = {Wei(balance).to('ether')}")
    print(web3.eth.getBalance(account.address))
   

def main():
    deploy_1()

