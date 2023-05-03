pragma solidity ^0.8.19;

contract myNewArray{
    uint[] data;
    function addValue(uint x) public returns (uint[] memory){
        data.push(x);
    }

    function wholeArray() public view returns(uint[] memory){
        return data;
    }

    function myarray_element(uint k) public view returns(uint){
        uint a = data[k];
        return a;
    }
}