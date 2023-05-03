pragma solidity ^0.8.19;

contract BookContract {
    struct Book {
        string title;
        string author;
        uint id;
        uint price;
    }

    function setBook(string memory _title, string memory _author, uint _id, uint _price) public {
        myBook = Book(_title, _author, _id, _price);
    }

    function getBook() public view returns (string memory, string memory, uint, uint) {
        return (myBook.title, myBook.author, myBook.id, myBook.price);
    }
}