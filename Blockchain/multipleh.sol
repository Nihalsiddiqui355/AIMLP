pragma solidity ^0.8.19;

contract Contract_A
{
    uint256 value;

    constructor (uint256 n) public
    {
        value=n;
    }
    function incrementValue(uint256 x) public
    {
        value+=x;
    }
    

    
}

contract Contract_B
{
    uint256 value1;
    constructor (uint256 n) public
    {
        value1=n;
    }
    function decrementValue(uint256 x) public
    {
        value1-=x;
    }
}

contract Contract_C is Contract_A(25),Contract_B(22)
{
    function getValue() public view returns(uint256,uint256)
    {
        return (value,value1);
        }
}