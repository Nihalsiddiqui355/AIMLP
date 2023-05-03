pragma solidity ^0.8.19;

contract Contract_A {
    uint256 value;
    constructor (uint256 n) public {
        value = n;
    }

    function incrementValue(uint256 x) public {
        value += x;
    }
}

contract Contract_B is Contract_A(22){
    function decrementVaule(uint256 x) public {
        value -= x;
    }
}

contract Contract_C is Contract_B{
    function getValue() public view returns(uint256){
        return value;
    }
}