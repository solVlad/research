
0xdAC17F958D2ee523a2206206994597C13D831ec7
https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#code


docker pull ethereum/solc:stable


https://github.com/crytic/solc-select


docs
docker run -v /data/redef/research/solcTests/test1:/sources ethereum/solc:0.4.17 -o /sources/output --userdoc --devdoc /sources/srcCodeFromEthScan.sol


docker run -v /data/redef/research/solcTests/test1:/sources ethereum/solc:0.4.17 -o /sources/output --combined-json userdoc,devdoc /sources/srcCodeFromEthScan.sol
