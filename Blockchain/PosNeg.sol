pragma solidity ^0.8.0;

/*contract CheckNumber {
    function isPositive(int number) public pure returns (bool) {
        if (number >= 0) {
            return true;
        } else {
            return false;
        }
    }
}*/

contract PositiveNegative {
    function checkNumber(int256 num) public pure returns (string memory) {
        if (num >= 0) {
            return "Positive";
        } else {
            return "Negative";
            }
        }
}