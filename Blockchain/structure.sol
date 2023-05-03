/*attritubes like title author id price
1 assigning the book2 
2 displaying book1
3 returning cost of book2
4 displaying author of book1*/


pragma solidity ^0.8.19;

contract BookContract {
    struct Book {
        string title;
        string author;
        uint id;
        uint price;
    }

    Book b1; 
    Book b2;
    Book b3;

    function setBook() public{
        b1 = Book("Learn Java","TP",102,650);
        b2 = Book("Learn Python","KG",203,795);
        b3 = Book("Learn C++","NJ",301,600);
    }

    function getBook() public view returns(string memory, string memory, uint, uint){
        return b1;
    }
}