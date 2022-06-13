// Solidity program to
// retrieve address and
// balance of owner
pragma solidity ^0.6.8;     
  
// Creating a contract
contract simpleBalance
{
    // Private state variable
    address payable private owner;
  
     // Defining a constructor   
     constructor() payable public{   
        owner=msg.sender;
        owner.transfer(msg.value);

    }
  
    // Function to get 
    // address of owner
    function getOwner(
    ) public view returns (address) {    
        return owner;
    }
  
    // Function to return 
    // current balance of owner
    function getBalance(
    ) public view returns(uint256){
        return owner.balance;
    }

    function burnSomeValue() public payable{
        require(msg.value>0);
        // owner.transfer(msg.value);
        }  


}