# about

0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9

https://etherscan.io/address/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9#code


slither 0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9 --detect reentrancy-eth --json sliterLog1.json


```

Reentrancy in Muffy._transfer(address,address,uint256) 
(crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#226-257):

        External calls:
        - swapTokensForEth(contractTokenBalance) 
        (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#248)

                - uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(tokenAmount,0,path,address(this),block.timestamp) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#264-270)
        External calls sending eth:
        - sendETHToFee(address(this).balance) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#251)
                - _feeAddrWallet1.transfer(amount.div(2)) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#274)
                - _feeAddrWallet2.transfer(amount.div(2)) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#275)
        State variables written after the call(s):
        - _tokenTransfer(from,to,amount) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#256)
                - _rOwned[address(this)] = _rOwned[address(this)].add(rTeam) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#318)
                - _rOwned[sender] = _rOwned[sender].sub(rAmount) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#308)
                - _rOwned[recipient] = _rOwned[recipient].add(rTransferAmount) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#309)
        - _tokenTransfer(from,to,amount) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#256)
                - _rTotal = _rTotal.sub(rFee) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#322)


                
Reentrancy in Muffy.openTrading() (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#278-290):
        External calls:
        - uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory()).createPair(address(this),_uniswapV2Router.WETH()) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#283)
        - uniswapV2Router.addLiquidityETH{value: address(this).balance}(address(this),balanceOf(address(this)),0,0,owner(),block.timestamp) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#284)
        External calls sending eth:
        - uniswapV2Router.addLiquidityETH{value: address(this).balance}(address(this),balanceOf(address(this)),0,0,owner(),block.timestamp) (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#284)
        State variables written after the call(s):
        - tradingOpen = true (crytic-export/etherscan-contracts/0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9-Muffy.sol#288)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities
0xA3e53C55A889C4841033DAdc37Ed2ACd82dD52C9 analyzed (7 contracts with 1 detectors), 2 result(s) found

```
