pragma solidity ^0.8.19;

import "libfactorial.sol";

contract PermutationCombination {
    using Factorial for uint;

    function nPr(uint n, uint r) public pure returns(uint) {
        return n.calculate() / (n-r).calculate();
    }
}