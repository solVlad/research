
# What is meter Blockchain?
* Meter.io is a highly decentralized Ethereum scaling solution with a built-in metastable gas currency. It connects to Ethereum and other blockchains as a layer-two protocol and allows smart contracts to scale and communicate seamlessly through heterogeneous blockchain networks.


* Meter_io Passport is a fork of ChainSafe's ChainBridge
* with one change introduced to the deposit method of the ERC20 Handler.

```
This change basically assumes that if the token being bridged is wrapped Native token then it doesn’t burn or lock since the wrapped Native token is already unwrapped and the amount transferred to the handler contract.
```

##  method 1

* The assumption holds true for one of the deposit methods depositEth which also asserts the value of amount in calldata
* (which will then ultimately get passed to the handler's deposit method):

## method 2

* the assumption doesn't hold true for another method deposit in the same contract which is mostly unguarded.

* The extended code had a wrong trust assumption which allowed hacker to call the underlying ERC20 deposit function to fake an BNB or ETH transfer.

## hack

* Hacker notices method2 - and sends an arbitrary amount in the calldata, which gets passed on the handler's deposit.

* The extended code had a wrong trust assumption which allowed hacker to call the underlying ERC20 deposit function to fake an BNB or ETH transfer.

