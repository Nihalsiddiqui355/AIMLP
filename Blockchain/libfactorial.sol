/*create a lib for factorial 
write a smart contract to calculate the value ncr npr*/

pragma solidity ^0.8.19;

library Factorial {
    function calculate(uint n) public pure returns (uint) {
        uint result = 1;
        for (uint i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}