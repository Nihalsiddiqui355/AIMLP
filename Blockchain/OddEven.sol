pragma solidity ^0.8.19;

contract EvenOdd {
    int num;
    string num_type;

    function set(int n) public{
        if (n % 2 == 0){
            num_type = "Even";
        } else{
            num_type = "Odd";
        }
        num = n;
    }

    function get() public view returns (string memory){
        return num_type;
    }
}
