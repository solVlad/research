###########################################################################################
###########################################################################################
# initiate a new blockchain with the following commands:
from manticore.ethereum import ManticoreEVM
m = ManticoreEVM()



###########################################################################################
###########################################################################################
## A non-contract account is created:
ETHER = 10**18
user_account = m.create_account(balance=1000*ETHER)


###########################################################################################
###########################################################################################
## A Solidity contract can be deployed
with open('example.sol') as f:
    contract_account = m.solidity_create_contract(f, owner=user_account)


###########################################################################################
###########################################################################################
## Raw transaction: all the functions are explored
symbolic_value = m.make_symbolic_value()
symbolic_data = m.make_symbolic_buffer(320)
m.transaction(caller=user_account,
              address=contract_account,
              data=symbolic_data,
              value=symbolic_value)
#If the data is symbolic, Manticore will explore all the functions of the contract during the transaction execution.              


###########################################################################################
###########################################################################################
## Named transaction
 # To execute f(uint var) with a symbolic value, from user_account, and with 0 ether, use:
symbolic_var = m.make_symbolic_value()
contract_account.f(symbolic_var, caller=user_account, value=0)
##If value of the transaction is not specified, it is 0 by default.


###########################################################################################
###########################################################################################
# m.workspace is the directory used as output directory for all the files generated:
print("Results are in {}".format(m.workspace))



###########################################################################################
###########################################################################################
#To stop the exploration 
m.finalize() # stop the exploration

