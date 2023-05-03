pragma solidity ^0.8.0;

contract DayOfWeek {
    function getDayOfWeek(uint256 dayNumber) public pure returns (string memory) {
        uint256 dayOfWeek = (dayNumber + 3) % 7;
        if (dayOfWeek == 0) {
            return "Sunday";
        } else if (dayOfWeek == 1) {
            return "Monday";
        } else if (dayOfWeek == 2) {
            return "Tuesday";
        } else if (dayOfWeek == 3) {
            return "Wednesday";
        } else if (dayOfWeek == 4) {
            return "Thursday";
        } else if (dayOfWeek == 5) {
            return "Friday";
        } else {
            return "Saturday";
        }
    }
}