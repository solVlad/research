# Arbix-rekt

## ref
* https://rekt.news/arbix-rekt/

## where
Binance Smart Chain

## party involved
* Arbix Finance - Rug pulls company
    contract: https://bscscan.com/address/0xd20ef93050c0943f74f5f8ff0cc97c74139d6437

* certik - Security review company



## timeline

### Nov 19th, 2021
* Security Assessment:
```
     Static Analysis
     Manual Review
```
* https://www.certik.com/projects/arbix


### 10th December
* on the 10th December ```0x161262d172699cf0a5e09b6cdfa5fee7f32c183d``` minted 4.5M ARBX.

    * https://bscscan.com/tx/0x4707d30a8d8152eebad1cdcae1d93af24cb9a344b447412ee1d65638b5c3db6f

```
From:
0xfe9972385c56edbb918cc671eda3437a591f8373 (Arbix Finance: Deployer)
Interacted With (To):
Contract 0xd20ef93050c0943f74f5f8ff0cc97c74139d6437 (Arbix Finance: ARBX Token)
Tokens Transferred:
    From Null Address: 0x000...000
    To 0x161262d172699cf0a5e09b6cdfa5fee7f32c183d For 4,500,000 ARBIX (ARBX) 

```


* Once the rug pull had begun, these tokens were dumped via PancakeSwap, tanking the price from $1.42 to ~$0.00. 
* The ~$50k in proceeds were then sent to the main rug wallet.



### Jan 4th

* Starting around 3 AM +UTC on Jan 4th, the project drained the vaults of users
* Around $10M in user’s assets were drained directly from the vaults into this wallet
    * https://bscscan.com/address/0x4714a26e4e2e1334c80575332ec9eb043b61a2c4

```
 0x4714A26e4E2e1334C80575332EC9eB043B61a2C4
```

* beginning with ~$1M in BTCB.
    * https://bscscan.com/tx/0xfbba507c8e90a264d5e77e5db854f5697572da1681f3647d4fa4381f7ef825b9





* Funds were sent from the BSC wallet: ```0x4714a26e4e2e1334c80575332ec9eb043b61a2c4```
* To Ethereum: ``` 0x4714a26e4e2e1334c80575332ec9eb043b61a2c4 ```
* And from there, converted into ~2.5k ETH (currently worth ~$9.9M)
* then sent to ```0xdc85c1eb22b0ece7be559a83fd788fe57f5a7a9f```


# related
* [what is farming](farming.md)



# summary

* [cetrix_anal](cetrix_anal.md)

* classified as a rugpull after the token's smart contract was detected minting 10 million ARBIX to addresses under the owner's control and then dumping them for Ethereum.

* The ARBX contract includes mint() with onlyOwner function, 10 million ARBX tokens were minted to 8 addresses.

