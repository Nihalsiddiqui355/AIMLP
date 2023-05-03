pragma solidity ^0.8.0;

contract DaysOfWeek {
    function getDayName(uint256 dayNum) public pure returns (string memory) {
        require(dayNum >= 1 && dayNum <= 7, "Invalid day number");
        string[7] memory daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        return daysOfWeek[dayNum - 1];
    }
}