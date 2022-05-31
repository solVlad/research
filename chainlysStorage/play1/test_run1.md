
(main)vlad@vladis:chainlysStorage/play1 ‹main*›$ brownie run scripts/deploy.py
Brownie v1.17.2 - Python development framework for Ethereum

Play1Project is the active project.

Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...

Running 'scripts/deploy.py::main'...
Transaction sent: 0x18f98a551e763d6e529b3ddafc7a2bd0ad91e6d1bcf01bb70ebeced0ae821ff0
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  SanctionsList.constructor confirmed   Block: 1   Gas used: 475074 (3.96%)
  SanctionsList deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

deploy done ; from=0x66aB6D9362d4F35596279692F0251Db635165871 ; simple_storage=0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87
run isSanctioned on 0x0000000000000000000000000000000000000004
False
add ['0x1111111111111111111111111111111111111111', '0x0000000000000000000000000000000000000004', '0x0000000000000000000000000000000000000006'] to Sanctioned
Transaction sent: 0xb8f1f196af519e63553ec0b313e86037429070bd2e789d59d8ce1218dfda0c9c
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
  SanctionsList.addToSanctionsList confirmed   Block: 2   Gas used: 87281 (0.73%)

<Transaction '0xb8f1f196af519e63553ec0b313e86037429070bd2e789d59d8ce1218dfda0c9c'>
<Transaction '0x18f98a551e763d6e529b3ddafc7a2bd0ad91e6d1bcf01bb70ebeced0ae821ff0'>
run isSanctioned on 0x0000000000000000000000000000000000000004
True
0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87
slot #0 = 0x66ab6d9362d4f35596279692f0251db635165871
slot #1 = 0x00
slot #2 = 0x00
slot #3 = 0x00
slot #4 = 0x00
slot #5 = 0x00
slot #6 = 0x00
slot #7 = 0x00
slot #8 = 0x00
slot #9 = 0x00
slot #107553882524790531947385985832592837884442228935463780553192851707863573624387 = 0x3039
Terminating local RPC client...
(main)vlad@vladis:chainlysStorage/play1 ‹main*›$ 



