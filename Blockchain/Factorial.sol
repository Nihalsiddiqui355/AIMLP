pragma solidity ^0.8.0;

contract Factorial {
    function factorial(uint n) public pure returns (uint) {
        uint result = 1;
        for (uint i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}