# pool contract


* https://bscscan.com/address/0x135CF5f01CE4f3f651a6fDf338620C768EACe9f1#code


pools addr

0    address :  0x135CF5f01CE4f3f651a6fDf338620C768EACe9f1
1    address :  0xB4A60F4b236A557d12Ce4c6f38c99BEC8bc6bDA9
2    address :  0x10C280f446e3C92583F292cc08BEeaBBFC92a570
3    address :  0xa0F75bF86aDEceE9d85064D130289c22F39DC6Df
4    address :  0x6aEfD539E534b295AAdF5Fa3b52998094d5128DB


## code

```
#
#  Panoramix v4 Oct 2019 
#  Decompiled source of bsc:0x135CF5f01CE4f3f651a6fDf338620C768EACe9f1
# 
#  Let's make the world open source 
# 
#
#  I failed with these: 
#  - unknown684a5843(?)
#  - deposit(uint256 _userId, address _userAddress)
#  - _fallback()
#  All the rest is below.
#

const unknown63fe3e3a = 0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c

def storage:
  stor0 is uint256 at storage 0
  stor0 is uint32 at storage 0
  owner is addr at storage 0
  depositorAddress is addr at storage 1
  stor2 is addr at storage 2
  stor3 is uint256 at storage 3
  unknown2495a599Address is addr at storage 4
  stor5 is uint32 at storage 5
  stor5 is uint256 at storage 5
  unknown13f14feeAddress is addr at storage 5
  stor6 is uint32 at storage 6
  unknown87557642Address is addr at storage 6
  stor6 is uint256 at storage 6
  unknownadb51980 is mapping of uint256 at storage 7
  stor8 is mapping of uint256 at storage 8
  stor9 is array of addr at storage 9
  stor10 is mapping of uint256 at storage 10
  stor11 is uint256 at storage 11
  stor12 is uint256 at storage 12
  stor15 is uint256 at storage 15
  stor16 is uint256 at storage 16
  unknown357930f4 is uint8 at storage 18

def unknown13f14fee(): # not payable
  return addr(unknown13f14feeAddress)

def unknown2495a599(): # not payable
  return unknown2495a599Address

def unknown357930f4(): # not payable
  return bool(unknown357930f4)

def unknown87557642(): # not payable
  return addr(unknown87557642Address)

def owner(): # not payable
  return addr(owner)

def unknownadb51980(addr _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  return unknownadb51980[_param1][_param2]

def depositor(): # not payable
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  return depositorAddress

#
#  Regular functions
#

def unknown2305817f(): # not payable
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor11

def unknown31c64010(): # not payable
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor16

def unknown4ed46249(): # not payable
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor15

def unknown7bcacbfb(): # not payable
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor12

def totalUsers(): # not payable
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor9.length

def unknown3e1ad29e(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if not _param1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  44,
                  0x735363686564756c65723a206e6577207363686564756c657220697320746865207a65726f20616464726573,
                  mem[208 len 20]
  stor2 = _param1

def unknown175e0931(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if not _param1:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  46,
                  0x724465706f73697461626c653a206e6577206465706f7369746f7220697320746865207a65726f20616464726573,
                  mem[210 len 18]
  depositorAddress = _param1

def unknown4e1e58f9(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor8[addr(_param1)]

def unknown3ad48551(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  return stor10[addr(_param1)]

def unknown5cf53ef3(uint256 _param1, uint256 _param2): # not payable
  require calldata.size - 4 >= 64
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  stor11 = _param1
  stor12 = _param2

def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if not _newOwner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  38,
                  0x724f776e61626c653a206e6577206f776e657220697320746865207a65726f20616464726573,
                  mem[202 len 26]
  log OwnershipTransferred(
        address previousOwner=addr(owner),
        address newOwner=_newOwner)
  addr(owner) = _newOwner

def unknown2c4f2416(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if addr(unknown13f14feeAddress):
      if not ext_code.size(unknown2495a599Address):
          revert with 0, 'Address: call to non-contract'
      mem[260 len 64] = approve(address spender, uint256 value), Mask(224, 0, stor5), uint32(stor5), 0
      call unknown2495a599Address with:
         funct uint32(stor5)
           gas gas_remaining wei
          args 0, mem[324 len 4]
      if not return_data.size:
          if not ext_call.success:
              revert with approve(address spender, uint256 value), Mask(224, 0, stor5), uint32(stor5), 0
          if not approve(address spender, uint256 value), Mask(224, 0, stor5):
              revert with 0, 32, 42, 0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
      else:
          mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              if return_data.size:
                  revert with ext_call.return_data[0 len return_data.size]
              revert with 0, 'SafeERC20: low-level call failed'
          if return_data.size:
              require return_data.size >= 32
              if not mem[292]:
                  revert with 0, 
                              32,
                              42,
                              0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 371 len 22]
  addr(unknown13f14feeAddress) = _param1

def unknowne8974635(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if addr(unknown87557642Address):
      if not ext_code.size(unknown2495a599Address):
          revert with 0, 'Address: call to non-contract'
      mem[260 len 64] = approve(address spender, uint256 value), Mask(224, 0, stor6), uint32(stor6), 0
      call unknown2495a599Address with:
         funct uint32(stor6)
           gas gas_remaining wei
          args 0, mem[324 len 4]
      if not return_data.size:
          if not ext_call.success:
              revert with approve(address spender, uint256 value), Mask(224, 0, stor6), uint32(stor6), 0
          if not approve(address spender, uint256 value), Mask(224, 0, stor6):
              revert with 0, 32, 42, 0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
      else:
          mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              if return_data.size:
                  revert with ext_call.return_data[0 len return_data.size]
              revert with 0, 'SafeERC20: low-level call failed'
          if return_data.size:
              require return_data.size >= 32
              if not mem[292]:
                  revert with 0, 
                              32,
                              42,
                              0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 371 len 22]
  addr(unknown87557642Address) = _param1

def unknown2d8189a4(array _param1): # not payable
  require calldata.size - 4 >= 32
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + (32 * _param1.length) + 36 <= calldata.size
  mem[128 len 32 * _param1.length] = call.data[_param1 + 36 len 32 * _param1.length]
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[(32 * _param1.length) + 234 len 26]
  require _param1.length <= 18446744073709551615
  mem[(32 * _param1.length) + 128] = _param1.length
  if _param1.length:
      mem[(32 * _param1.length) + 160 len 32 * _param1.length] = call.data[calldata.size len 32 * _param1.length]
  idx = 0
  while idx < _param1.length:
      require idx < _param1.length
      require mem[(32 * idx) + 128] < stor9.length
      mem[0] = 9
      require idx < _param1.length
      mem[(32 * idx) + (32 * _param1.length) + 160] = stor9[mem[(32 * idx) + 128]]
      idx = idx + 1
      continue 
  mem[(64 * _param1.length) + 160] = 32
  mem[(64 * _param1.length) + 192] = _param1.length
  mem[(64 * _param1.length) + 224 len floor32(_param1.length)] = mem[(32 * _param1.length) + 160 len floor32(_param1.length)]
  return memory
    from (64 * _param1.length) + 160
     len (161 * _param1.length) + 64

def unknowna873ffec(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if stor3 == 2:
      revert with 0, 'ReentrancyGuard: reentrant call'
  stor3 = 2
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown87557642Address))
  call addr(unknown87557642Address).0x2a9040b3 with:
       gas gas_remaining wei
      args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if not ext_code.size(unknown2495a599Address):
      revert with 0, 'Address: call to non-contract'
  mem[324 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor0), uint32(stor0), 0
  mem[388 len 0] = 0
  call unknown2495a599Address with:
     funct uint32(stor0)
       gas gas_remaining wei
      args Mask(480, -256, transfer(address to, uint256 value), Mask(224, 0, stor0), uint32(stor0), 0) << 256, mem[388 len 4]
  if not return_data.size:
      require not ext_call.success
      revert with 'SafeMath: subtraction overflow'
  mem[356 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not ext_call.success:
      if return_data.size:
          revert with ext_call.return_data[0 len return_data.size]
      revert with 0, 'SafeERC20: low-level call failed'
  if return_data.size:
      require return_data.size >= 32
      if not mem[356]:
          revert with 0, 
                      32,
                      42,
                      0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                      mem[ceil32(return_data.size) + 435 len 22]
  stor8[addr(stor6)] += _param1
  stor3 = 1
  return 1

def unknown1f992604(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if stor3 == 2:
      revert with 0, 'ReentrancyGuard: reentrant call'
  stor3 = 2
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown13f14feeAddress))
  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
       gas gas_remaining wei
      args _param1, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if not ext_code.size(unknown2495a599Address):
      revert with 0, 'Address: call to non-contract'
  mem[324 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor0), uint32(stor0), 0
  mem[388 len 0] = 0
  call unknown2495a599Address with:
     funct uint32(stor0)
       gas gas_remaining wei
      args Mask(480, -256, transfer(address to, uint256 value), Mask(224, 0, stor0), uint32(stor0), 0) << 256, mem[388 len 4]
  if not return_data.size:
      require not ext_call.success
      revert with 'SafeMath: subtraction overflow'
  mem[356 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not ext_call.success:
      if return_data.size:
          revert with ext_call.return_data[0 len return_data.size]
      revert with 0, 'SafeERC20: low-level call failed'
  if return_data.size:
      require return_data.size >= 32
      if not mem[356]:
          revert with 0, 
                      32,
                      42,
                      0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                      mem[ceil32(return_data.size) + 435 len 22]
  stor8[addr(stor5)] += _param1
  stor3 = 1
  return 1

def unknown574fb4e3(): # not payable
  if addr(owner) != caller:
      revert with 0, 'wOwnable: caller is not the owne'
  if stor3 == 2:
      revert with 0, 'ReentrancyGuard: reentrant call'
  stor3 = 2
 
 
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0xa0e99fcb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
 
 
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32


  require ext_code.size(addr(unknown87557642Address))
  call addr(unknown87557642Address).0x2a9040b3 with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


  require ext_code.size(addr(unknown13f14feeAddress))
  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
       gas gas_remaining wei
      args ext_call.return_data[0], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
 
 
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


  require return_data.size >= 32
  if not ext_code.size(unknown2495a599Address):
      revert with 0, 'Address: call to non-contract'


  mem[260 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor0), uint32(stor0), ext_call.return_data[0 len 28]
  mem[324 len 0] = 0
 
 
 
  call unknown2495a599Address with:
     funct uint32(stor0)
       gas gas_remaining wei
      args Mask(480, -256, ext_call.return_data << 256, mem[324 len 4]
  if not return_data.size:
      if not ext_call.success:
          revert with transfer(address to, uint256 value), Mask(224, 0, stor0), uint32(stor0), ext_call.return_data[0]
      if not transfer(address to, uint256 value), Mask(224, 0, stor0):
          revert with 0, 32, 42, 0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]


  else:
      mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
      if not ext_call.success:
          if return_data.size:
              revert with ext_call.return_data[0 len return_data.size]
          revert with 0, 'SafeERC20: low-level call failed'
      if return_data.size:
          require return_data.size >= 32
          if not mem[292]:
              revert with 0, 
                          32,
                          42,
                          0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                          mem[ceil32(return_data.size) + 371 len 22]
  stor8[addr(stor6)] += ext_call.return_data[0]
  stor8[addr(stor5)] += ext_call.return_data[0]
  stor3 = 1
  return 1

















def unknown85e822ce(): # not payable
  if addr(owner) != caller:
      if stor2 != caller:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      38,
                      0xfe5363686564756c65723a2063616c6c6572206973206e6f7420746865207363686564756c65,
                      mem[202 len 26]
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).0xca7fc63f with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      require ext_code.size(addr(unknown87557642Address))
      static call addr(unknown87557642Address).0x77c7b8fc with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(addr(unknown87557642Address))
      static call addr(unknown87557642Address).0xa0e99fcb with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_call.return_data[0]:
          return 0
      if ext_call.return_data * ext_call.return_data / ext_call.return_data[0] != ext_call.return_data[0]:
          revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
      if ext_call.return_data * ext_call.return_data / 10^18 < 0:
          revert with 0, 'SafeMath: addition overflow'
      return (ext_call.return_data * ext_call.return_data / 10^18)
  if ext_call.return_data * ext_call.return_data / ext_call.return_data[0] != ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0x77c7b8fc with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0xa0e99fcb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not ext_call.return_data[0]:
      if ext_call.return_data * ext_call.return_data / 10^18 < ext_call.return_data * ext_call.return_data / 10^18:
          revert with 0, 'SafeMath: addition overflow'
      return (ext_call.return_data * ext_call.return_data / 10^18)
  if ext_call.return_data * ext_call.return_data / ext_call.return_data[0] != ext_call.return_data[0]:
      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
  if 2 * ext_call.return_data * ext_call.return_data / 10^18 < ext_call.return_data * ext_call.return_data / 10^18:
      revert with 0, 'SafeMath: addition overflow'
  return (2 * ext_call.return_data * ext_call.return_data / 10^18)

def unknown594774d1(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0x77c7b8fc with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknownadb51980[addr(stor6)][addr(_param1)]:
      require ext_code.size(addr(unknown13f14feeAddress))
      static call addr(unknown13f14feeAddress).0xca7fc63f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not unknownadb51980[addr(stor5)][addr(_param1)]:
          return 0
      if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / unknownadb51980[addr(stor5)][addr(_param1)] != ext_call.return_data[0]:
          revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
      if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / 10^18 < ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / 10^18:
          revert with 0, 'SafeMath: addition overflow'
      return (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / 10^18)
  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param1)] / unknownadb51980[addr(stor6)][addr(_param1)] != ext_call.return_data[0]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  33,
                  0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                  mem[197 len 31]
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).0xca7fc63f with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknownadb51980[addr(stor5)][addr(_param1)]:
      if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param1)] / 10^18 < 0:
          revert with 0, 'SafeMath: addition overflow'
      return (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param1)] / 10^18)
  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / unknownadb51980[addr(stor5)][addr(_param1)] != ext_call.return_data[0]:
      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
  if (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param1)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / 10^18) < ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / 10^18:
      revert with 0, 'SafeMath: addition overflow'
  return ((ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param1)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param1)] / 10^18))

def unknown19bf5922(addr _param1): # not payable
  require calldata.size - 4 >= 32
  if depositorAddress != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  40,
                  0x734465706f73697461626c653a2063616c6c6572206973206e6f7420746865206465706f7369746f,
                  mem[204 len 24]
  if not unknown357930f4:
      revert with 0, 'not bnb'
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0xa0e99fcb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknownadb51980[addr(stor6)][addr(_param1)] > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if ext_call.return_dataunknownadb51980[addr(stor6)][addr(_param1)] < stor11:
      revert with 0, 'Fail Amount Threshold'
  require ext_code.size(addr(unknown87557642Address))
  call addr(unknown87557642Address).withdraw(uint256 amount) with:
       gas gas_remaining wei
      args unknownadb51980[addr(stor6)][addr(_param1)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0xa0e99fcb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if 0 > unknownadb51980[addr(stor6)][addr(_param1)]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknownadb51980[addr(stor5)][addr(_param1)] > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if ext_call.return_dataunknownadb51980[addr(stor5)][addr(_param1)] < stor12:
      revert with 0, 'Fail Amount Threshold'
  require ext_code.size(addr(unknown13f14feeAddress))
  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
       gas gas_remaining wei
      args unknownadb51980[addr(stor5)][addr(_param1)], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if 0 > unknownadb51980[addr(stor5)][addr(_param1)]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c)
  static call 0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data >= 0:
      require ext_code.size(0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c)
      call 0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c.withdraw(uint256 amount) with:
           gas gas_remaining wei
          args 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  call caller with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with 0, 'Failed to sent BNB'
  return 1

def withdrawAll(address _recipient): # not payable
  require calldata.size - 4 >= 32
  if depositorAddress != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  40,
                  0x734465706f73697461626c653a2063616c6c6572206973206e6f7420746865206465706f7369746f,
                  mem[204 len 24]
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0xa0e99fcb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknownadb51980[addr(stor6)][addr(_recipient)] > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if ext_call.return_dataunknownadb51980[addr(stor6)][addr(_recipient)] < stor11:
      revert with 0, 'Fail Amount Threshold'
  require ext_code.size(addr(unknown87557642Address))
  call addr(unknown87557642Address).withdraw(uint256 amount) with:
       gas gas_remaining wei
      args unknownadb51980[addr(stor6)][addr(_recipient)]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0xa0e99fcb with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if 0 > unknownadb51980[addr(stor6)][addr(_recipient)]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if unknownadb51980[addr(stor5)][addr(_recipient)] > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if ext_call.return_dataunknownadb51980[addr(stor5)][addr(_recipient)] < stor12:
      revert with 0, 'Fail Amount Threshold'
  require ext_code.size(addr(unknown13f14feeAddress))
  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
       gas gas_remaining wei
      args unknownadb51980[addr(stor5)][addr(_recipient)], 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if 0 > unknownadb51980[addr(stor5)][addr(_recipient)]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if not ext_code.size(unknown2495a599Address):
      revert with 0, 'Address: call to non-contract'
  mem[708 len 64] = transfer(address to, uint256 value), caller, 0
  call unknown2495a599Address with:
     funct uint32(caller)
       gas gas_remaining wei
      args 0, mem[772 len 4]
  if not return_data.size:
      require not ext_call.success
      revert with 'SafeMath: subtraction overflow'
  mem[740 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not ext_call.success:
      if return_data.size:
          revert with ext_call.return_data[0 len return_data.size]
      revert with 0, 'SafeERC20: low-level call failed'
  if return_data.size:
      require return_data.size >= 32
      if not mem[740]:
          revert with 0, 
                      32,
                      42,
                      0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                      mem[ceil32(return_data.size) + 819 len 22]
  return 1

def unknown07d1b247(uint256 _param1, addr _param2): # not payable
  require calldata.size - 4 >= 64
  if depositorAddress != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  40,
                  0x734465706f73697461626c653a2063616c6c6572206973206e6f7420746865206465706f7369746f,
                  mem[204 len 24]
  if not unknown357930f4:
      revert with 0, 'not bnb'
  if _param1 < 10^6:
      revert with 0, 'Amount too low'
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0x77c7b8fc with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknownadb51980[addr(stor6)][addr(_param2)]:
      require ext_code.size(addr(unknown13f14feeAddress))
      static call addr(unknown13f14feeAddress).0xca7fc63f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not unknownadb51980[addr(stor5)][addr(_param2)]:
          if not _param1 / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if not unknownadb51980[addr(stor6)][addr(_param2)]:
              if not 0 / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not 0 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / 0 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / 0 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / 0 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / 0 / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not 0 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / 0 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / 0 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6, 0
          else:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / unknownadb51980[addr(stor6)][addr(_param2)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not 0 / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not 0 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / 0 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / 0 / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not 0 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / 0 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / 0 / _param1 / 10^6, 0
      else:
          if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != ext_call.return_data[0]:
              revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
          if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 < ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18:
              revert with 0, 'SafeMath: addition overflow'
          if not _param1 / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if not unknownadb51980[addr(stor6)][addr(_param2)]:
              if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
          else:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / unknownadb51980[addr(stor6)][addr(_param2)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
  else:
      if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / unknownadb51980[addr(stor6)][addr(_param2)] != ext_call.return_data[0]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      require ext_code.size(addr(unknown13f14feeAddress))
      static call addr(unknown13f14feeAddress).0xca7fc63f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not unknownadb51980[addr(stor5)][addr(_param2)]:
          if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 < 0:
              revert with 0, 'SafeMath: addition overflow'
          if not _param1 / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if not unknownadb51980[addr(stor6)][addr(_param2)]:
              if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
          else:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / unknownadb51980[addr(stor6)][addr(_param2)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18 / _param1 / 10^6, 0
      else:
          if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != ext_call.return_data[0]:
              revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
          if (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) < ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18:
              revert with 0, 'SafeMath: addition overflow'
          if not _param1 / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if not unknownadb51980[addr(stor6)][addr(_param2)]:
              if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6, 0
          else:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / unknownadb51980[addr(stor6)][addr(_param2)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_param2)]:
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / unknownadb51980[addr(stor5)][addr(_param2)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > unknownadb51980[addr(stor5)][addr(_param2)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_param2)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_param2)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_param2)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_param2)] / 10^18) / _param1 / 10^6, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require ext_code.size(addr(unknown13f14feeAddress))
  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  if 0 > unknownadb51980[addr(stor5)][addr(_param2)]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(unknown2495a599Address)
  static call unknown2495a599Address.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data > ext_call.return_data[0]:
      revert with 0, 'SafeMath: subtraction overflow'
  require ext_code.size(0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c)
  static call 0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if ext_call.return_data >= 0:
      require ext_code.size(0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c)
      call 0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c.withdraw(uint256 amount) with:
           gas gas_remaining wei
          args 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
  call caller with:
       gas gas_remaining wei
  if not ext_call.success:
      revert with 0, 'Failed to sent BNB'
  return 1

def withdraw(uint256 _amount, address _recepient): # not payable
  require calldata.size - 4 >= 64
  if depositorAddress != caller:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                  32,
                  40,
                  0x734465706f73697461626c653a2063616c6c6572206973206e6f7420746865206465706f7369746f,
                  mem[204 len 24]
  if _amount < 10^6:
      revert with 0, 'Amount too low'
  require ext_code.size(addr(unknown87557642Address))
  static call addr(unknown87557642Address).0x77c7b8fc with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32
  if not unknownadb51980[addr(stor6)][addr(_recepient)]:
      require ext_code.size(addr(unknown13f14feeAddress))
      static call addr(unknown13f14feeAddress).0xca7fc63f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not unknownadb51980[addr(stor5)][addr(_recepient)]:
          if not _amount / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if not unknownadb51980[addr(stor6)][addr(_recepient)]:
              if not 0 / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not 0 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / 0 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / 0 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args 0, mem[1156 len 4]
              else:
                  if not 0 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / 0 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / 0 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / 0 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / 0 / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  mem[1156 len 0] = 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
          else:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / unknownadb51980[addr(stor6)][addr(_recepient)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not 0 / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if not 0 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / 0 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / 0 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / 0 / _amount / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not 0 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / 0 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / 0 / _amount / 10^6, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(unknown13f14feeAddress))
              static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data > ext_call.return_data[0]:
                  revert with 0, 'SafeMath: subtraction overflow'
              if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(unknown2495a599Address)
              static call unknown2495a599Address.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data > ext_call.return_data[0]:
                  revert with 0, 'SafeMath: subtraction overflow'
              if not ext_code.size(unknown2495a599Address):
                  revert with 0, 'Address: call to non-contract'
              mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
              mem[1156 len 0] = 0
              call unknown2495a599Address with:
                 funct uint32(caller)
                   gas gas_remaining wei
                  args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
      else:
          if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != ext_call.return_data[0]:
              revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
          if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 < ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18:
              revert with 0, 'SafeMath: addition overflow'
          if not _amount / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if unknownadb51980[addr(stor6)][addr(_recepient)]:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / unknownadb51980[addr(stor6)][addr(_recepient)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args 0, mem[1156 len 4]
              else:
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  mem[1156 len 0] = 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
          else:
              if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require ext_code.size(addr(unknown13f14feeAddress))
              static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data > ext_call.return_data[0]:
                  revert with 0, 'SafeMath: subtraction overflow'
              if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                  revert with 0, 'SafeMath: subtraction overflow'
              require ext_code.size(unknown2495a599Address)
              static call unknown2495a599Address.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data > ext_call.return_data[0]:
                  revert with 0, 'SafeMath: subtraction overflow'
              if not ext_code.size(unknown2495a599Address):
                  revert with 0, 'Address: call to non-contract'
              mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
              mem[1156 len 0] = 0
              call unknown2495a599Address with:
                 funct uint32(caller)
                   gas gas_remaining wei
                  args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
  else:
      if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / unknownadb51980[addr(stor6)][addr(_recepient)] != ext_call.return_data[0]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      32,
                      33,
                      0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                      mem[197 len 31]
      require ext_code.size(addr(unknown13f14feeAddress))
      static call addr(unknown13f14feeAddress).0xca7fc63f with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if unknownadb51980[addr(stor5)][addr(_recepient)]:
          if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != ext_call.return_data[0]:
              revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[261 len 31]
          if (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) < ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18:
              revert with 0, 'SafeMath: addition overflow'
          if not _amount / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if unknownadb51980[addr(stor6)][addr(_recepient)]:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / unknownadb51980[addr(stor6)][addr(_recepient)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args 0, mem[1156 len 4]
              else:
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  mem[1156 len 0] = 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
          else:
              if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args 0, mem[1156 len 4]
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / (ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18) + (ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / 10^18) / _amount / 10^6, 0
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if not ext_code.size(unknown2495a599Address):
                      revert with 0, 'Address: call to non-contract'
                  mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
                  mem[1156 len 0] = 0
                  call unknown2495a599Address with:
                     funct uint32(caller)
                       gas gas_remaining wei
                      args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
      else:
          if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 < 0:
              revert with 0, 'SafeMath: addition overflow'
          if not _amount / 10^6:
              revert with 0, 'SafeMath: division by zero'
          if not unknownadb51980[addr(stor6)][addr(_recepient)]:
              if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
          else:
              if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / unknownadb51980[addr(stor6)][addr(_recepient)] != 10^6:
                  revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[453 len 31]
              if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6:
                  revert with 0, 'SafeMath: division by zero'
              if not unknownadb51980[addr(stor5)][addr(_recepient)]:
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 0 / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
              else:
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / unknownadb51980[addr(stor5)][addr(_recepient)] != 10^6:
                      revert with 0, 32, 33, 0x73536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[517 len 31]
                  if not ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6:
                      revert with 0, 'SafeMath: division by zero'
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > unknownadb51980[addr(stor5)][addr(_recepient)]:
                      revert with 0, 'Insufficient fund'
                  require ext_code.size(unknown2495a599Address)
                  static call unknown2495a599Address.balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor11:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown87557642Address))
                  call addr(unknown87557642Address).withdraw(uint256 amount) with:
                       gas gas_remaining wei
                      args (10^6 * unknownadb51980[addr(stor6)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6)
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require ext_code.size(addr(unknown87557642Address))
                  static call addr(unknown87557642Address).0xa0e99fcb with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if ext_call.return_data > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if 0 > unknownadb51980[addr(stor6)][addr(_recepient)]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                          gas gas_remaining wei
                         args this.address
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  if 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6 > ext_call.return_data[0]:
                      revert with 0, 'SafeMath: subtraction overflow'
                  if ext_call.return_data * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6) < stor12:
                      revert with 0, 'Fail Amount Threshold'
                  require ext_code.size(addr(unknown13f14feeAddress))
                  call addr(unknown13f14feeAddress).withdraw(uint256 devAmount, uint256 submissionAmount) with:
                       gas gas_remaining wei
                      args 10^6 * unknownadb51980[addr(stor5)][addr(_recepient)] / ext_call.return_data * unknownadb51980[addr(stor6)][addr(_recepient)] / 10^18 / _amount / 10^6, 0
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require ext_code.size(addr(unknown13f14feeAddress))
          static call addr(unknown13f14feeAddress).balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data > ext_call.return_data[0]:
              revert with 0, 'SafeMath: subtraction overflow'
          if 0 > unknownadb51980[addr(stor5)][addr(_recepient)]:
              revert with 0, 'SafeMath: subtraction overflow'
          require ext_code.size(unknown2495a599Address)
          static call unknown2495a599Address.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if ext_call.return_data > ext_call.return_data[0]:
              revert with 0, 'SafeMath: subtraction overflow'
          if not ext_code.size(unknown2495a599Address):
              revert with 0, 'Address: call to non-contract'
          mem[1092 len 64] = transfer(address to, uint256 value), caller, 0
          mem[1156 len 0] = 0
          call unknown2495a599Address with:
             funct uint32(caller)
               gas gas_remaining wei
              args Mask(480, -256, transfer(address to, uint256 value), caller, 0) << 256, mem[1156 len 4]
  if not return_data.size:
      require not ext_call.success
      revert with 'SafeMath: division by zero'
  mem[1124 len return_data.size] = ext_call.return_data[0 len return_data.size]
  if not ext_call.success:
      if return_data.size:
          revert with ext_call.return_data[0 len return_data.size]
      revert with 0, 'SafeERC20: low-level call failed'
  if return_data.size:
      require return_data.size >= 32
      if not mem[1124]:
          revert with 0, 
                      32,
                      42,
                      0x725361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                      mem[ceil32(return_data.size) + 1203 len 22]
  return 1


```