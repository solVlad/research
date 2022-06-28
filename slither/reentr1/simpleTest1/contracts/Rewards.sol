pragma solidity ^0.4.8;

contract Rewards {
    uint public gifts;

    function allowGifts(uint num_gifts) public { gifts = num_gifts; }

    function withdraw() public {
        uint _amount = 1 ether;
        if (gifts > 0) {
            // msg.sender.call() calls the fallback-function on msg.sender
           if (!msg.sender.call.value(_amount)()) 
            revert(); 
           gifts -= 1;
        }
    }

    function deposit() payable public {}

    function getBalance() public constant returns(uint) { 
        address a = this;
        return a.balance; 
    }    
}

