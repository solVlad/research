# multi transactions

Use Manticore to find if an overflow is possible

nitialization

    Create one user account
    Create the contract account

Exploration

    Call two times add with two symbolic values
    Call sellerBalance()

Property

    Check if it is possible for the value returned by sellerBalance() to be lower than the first input.


The value returned by the last transaction can be accessed through:

    state.platform.transactions[-1].return_data

The data returned needs to be deserialized:

    data = ABI.deserialize("uint", data)


## run

```

(manticore_native) (REDF)vlad@vladis:play/7_multi_transactions ‹main*›$ python 7_run.py    
2022-06-09 23:28:45,021: [1290986] m.c.plugin:WARNING: Caught will_solve in state None, but failed to capture its initialization
Bug found, results are in /data/redef/research/manticore/play/7_multi_transactions/mcore_f4l99zeq


Transactions No. 0
Type: CREATE (0)
From: normal0(0x1a6f6f69e907a3cf4ef447b2758b5465dc0015ed) 
To: contract0(0xa49105ffccd1f7442b72a5bd4a96a5a4445eab27) 
Value: 0 
Gas used: 3000000 
Data: 0x60806040526000805534801561001457600080fd5b5060e7806100236000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80631003e2d2146037578063867a06b314607a575b600080fd5b606060048036036020811015604b57600080fd5b81019080803590602001909291905050506096565b604051808215151515815260200191505060405180910390f35b608060ac565b6040518082815260200191505060405180910390f35b6000816000808282540192505081905550919050565b6000548156fea265627a7a72315820319fbd14742de70f49e637a1492685902d5f47e53f5d391bcf1bf6d3cee785f964736f6c634300050c0032 
Return_data: 0x6080604052348015600f57600080fd5b506004361060325760003560e01c80631003e2d2146037578063867a06b314607a575b600080fd5b606060048036036020811015604b57600080fd5b81019080803590602001909291905050506096565b604051808215151515815260200191505060405180910390f35b608060ac565b6040518082815260200191505060405180910390f35b6000816000808282540192505081905550919050565b6000548156fea265627a7a72315820319fbd14742de70f49e637a1492685902d5f47e53f5d391bcf1bf6d3cee785f964736f6c634300050c0032  (*)
Function call:
Constructor() -> RETURN 


Transactions No. 1
Type: CALL (0)
From: normal0(0x1a6f6f69e907a3cf4ef447b2758b5465dc0015ed) 
To: contract0(0xa49105ffccd1f7442b72a5bd4a96a5a4445eab27) 
Value: 0 
Gas used: 210000 
Data: 0x1003e2d2fffffffffffffffffffffffdffffffffffffffffffffffffffffffffffffffb6 (*)
Return_data: 0x0000000000000000000000000000000000000000000000000000000000000000 () (*)

Function call:
add(115792089237316195423570985005764904578608178829233194374025017968601264553910) -> RETURN (*)
return: 0 (*)


Transactions No. 2
Type: CALL (0)
From: normal0(0x1a6f6f69e907a3cf4ef447b2758b5465dc0015ed) 
To: contract0(0xa49105ffccd1f7442b72a5bd4a96a5a4445eab27) 
Value: 0 
Gas used: 210000 
Data: 0x1003e2d2800000000000000000000002000000000000000000000000000000000000008d (*)
Return_data: 0x0000000000000000000000000000000000000000000000000000000000000000 () (*)

Function call:
add(57896044618658097711785492507266957201296798169227651685161358043268429906061) -> RETURN (*)
return: 0 (*)


Transactions No. 3
Type: CALL (0)
From: normal0(0x1a6f6f69e907a3cf4ef447b2758b5465dc0015ed) 
To: contract0(0xa49105ffccd1f7442b72a5bd4a96a5a4445eab27) 
Value: 0 
Gas used: 210000 
Data: 0x867a06b3 
Return_data: 0x7ffffffffffffffffffff3ebfffffffffffffff4fffffffffffffffffffffe01 () (*)

Function call:
sellerBalance() -> RETURN 
return: 57896044618658097711785487985380891299483169246155269473324787514284158483969 (*)




(*) Example solution given. Value is symbolic and may take other values

```