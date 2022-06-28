

0x07af67b392B7A202fAD8E0FBc64C34F33102165B

slither bsc:0x07af67b392B7A202fAD8E0FBc64C34F33102165B --detect reentrancy-eth --json jsonResult.json


```
Reentrancy in Aquagoat._transfer(address,address,uint256) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1018-1062):
        External calls:
        - swapAndLiquify(contractTokenBalance) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1049)
                - uniswapV2Router.addLiquidityETH{value: ethAmount}(address(this),tokenAmount,0,0,owner(),block.timestamp) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1110-1117)
                - uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(tokenAmount,0,path,address(this),block.timestamp) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1096-1102)
        External calls sending eth:
        - swapAndLiquify(contractTokenBalance) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1049)
                - uniswapV2Router.addLiquidityETH{value: ethAmount}(address(this),tokenAmount,0,0,owner(),block.timestamp) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1110-1117)
        State variables written after the call(s):
        - _tokenTransfer(from,to,amount,takeFee) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1061)
                - _rOwned[address(this)] = _rOwned[address(this)].add(rLiquidity) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#974)
                - _rOwned[sender] = _rOwned[sender].sub(rAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1152)
                - _rOwned[sender] = _rOwned[sender].sub(rAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1143)
                - _rOwned[recipient] = _rOwned[recipient].add(rTransferAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1144)
                - _rOwned[sender] = _rOwned[sender].sub(rAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1163)
                - _rOwned[sender] = _rOwned[sender].sub(rAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#890)
                - _rOwned[recipient] = _rOwned[recipient].add(rTransferAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1154)
                - _rOwned[recipient] = _rOwned[recipient].add(rTransferAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1164)
                - _rOwned[recipient] = _rOwned[recipient].add(rTransferAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#892)
        - _tokenTransfer(from,to,amount,takeFee) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1061)
                - _rTotal = _rTotal.sub(rFee) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#929)
        - _tokenTransfer(from,to,amount,takeFee) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1061)
                - _tOwned[address(this)] = _tOwned[address(this)].add(tLiquidity) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#976)
                - _tOwned[sender] = _tOwned[sender].sub(tAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1162)
                - _tOwned[sender] = _tOwned[sender].sub(tAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#889)
                - _tOwned[recipient] = _tOwned[recipient].add(tTransferAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#1153)
                - _tOwned[recipient] = _tOwned[recipient].add(tTransferAmount) (crytic-export/etherscan-contracts/0x07af67b392B7A202fAD8E0FBc64C34F33102165B.bscscan.com-Aquagoat.sol#891)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities
bsc:0x07af67b392B7A202fAD8E0FBc64C34F33102165B analyzed (10 contracts with 1 detectors), 1 result(s) found



```

