
// File: contracts/SanctionsList.sol

import "./Ownable.sol";

pragma solidity >=0.4.22 <0.9.0;


contract SanctionsList is Ownable {

  //mapping(address => bool) private sanctionedAddresses;
  //change boot to int to test read real value
  mapping(address => int) private sanctionedAddresses;


  constructor() {}


  event SanctionedAddress(address indexed addr);
  event NonSanctionedAddress(address indexed addr);
  event SanctionedAddressesAdded(address[] addrs);
  event SanctionedAddressesRemoved(address[] addrs);

  function name() external pure returns (string memory) {
    return "Chainalysis sanctions oracle";
  }

  function addToSanctionsList(address[] memory newSanctions) public onlyOwner {
    for (uint256 i = 0; i < newSanctions.length; i++) {
      /////sanctionedAddresses[newSanctions[i]] = true;  
      sanctionedAddresses[newSanctions[i]] = 12345;  

    }
    emit SanctionedAddressesAdded(newSanctions);
  }

  function removeFromSanctionsList(address[] memory removeSanctions) public onlyOwner {
    for (uint256 i = 0; i < removeSanctions.length; i++) {
      ///sanctionedAddresses[removeSanctions[i]] = false;  
      sanctionedAddresses[removeSanctions[i]] = 6789;  

    }
    emit SanctionedAddressesRemoved(removeSanctions);
  }

  function isSanctioned(address addr) public view returns (bool) {
    ///return sanctionedAddresses[addr] == true ;
    return sanctionedAddresses[addr] == 12345 ;

  }

  function isSanctionedVerbose(address addr) public returns (bool) {
    if (isSanctioned(addr)) {
      emit SanctionedAddress(addr);
      return true;
    } else {
      emit NonSanctionedAddress(addr);
      return false;
    }
  }

}
