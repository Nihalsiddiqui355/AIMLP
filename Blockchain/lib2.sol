pragma solidity ^0.8.19;

import "lib1.sol";

contract useLibrary{
    using lib for uint;

    function testIncrement(uint userValue) public pure returns (uint){
        return lib.increment(userValue);
    }

    function testDecrement(uint userValue) public pure returns (uint){
        return lib.decrement(userValue);
    }

    function testIncrementbyValue(uint userValue, uint x) public pure returns (uint){
        return lib.incrementByValue(userValue, x);
    }

    function testDecrementbyValue(uint userValue, uint x) public pure returns (uint){
        return lib.decrementByValue(userValue, x);
    }
}