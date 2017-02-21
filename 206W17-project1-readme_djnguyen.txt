206 Project 1 - Code for playing cards
README

Your name: David Nguyen (djnguyen)
Anyone you worked with: N/A

--README FILE--

Overall Description:

This code contains three classes that can be very useful when playing card games such as War. The card game War can be seen in the function play_war_game. The three classes that are defined are Card, Deck, and Hand. The three classes are reliant on each other to work properly and to play a card game. The Card class creates the cards, the Deck class uses the Card class to create an entire 52 card deck, and the Hand class uses the Card and Deck class to create a hand for a player, with a specific number of cards that can be limited by the programmer.

The play_war_game function simulates the card game of War in which it uses the Card and Deck classes. With the simulation of the game, two players are given a deck of 52 cards that are of random assortment. There is a method in the Deck class called pop_card which is used to remove a card from the deck and is compared to see which player gets the point. That card is then removed and the process repeats itself. When all 52 cards are gone, the player with the highest number of points is declared the winner.

The Hand class is not referenced in the play_war_game function but it can be applicable to card games that require a smaller number of cards to be played with, or maybe even a war game with less than 52 cards. 

With this code and the very simple classes that have been created, there can definitely be an extension to the Card Game of War and create code to play other card games due to the simple nature of these Classes and their basic functionality.


Card CLASS:
	The Card Class has suit_names, rank_levels, and faces defined to show the three characteristics of a single card enclosed either in a list or a dictionary. It is essentially an object that contains a suit and a ranking level like a traditional playing card. Possible suits include “Diamonds”, “Clubs”, “Hearts”, and “Spades”. Possible ranks range from 1-13 with special cards of Aces, Jack, Queen, and King respectively at ranks 1,11,12, and 13. One instance of this class would be a single playing card with the attributes that were just described.

• __init__ METHOD:
	The __init__ method is also known as the constructor of the class. This method includes three instance variables: self.suit, self.rank, and self.rank_num. The constructor also contains two optional inputs/arguments: suit and rank. With optional inputs, the constructor automatically defaults to a suit of 0 and a rank of 2, also known as a “2 of Diamonds”. But, if Card(3,4) is called, an instance of a card object is made with the attributes of “Spade” (since it is the 3rd index in the suit_names list) and the rank of 4, as it is the second argument passed in the constructor. It would be commonly known as a “4 of Spades”. These attributes are saved in self.suit, self.rank, and self.rank_num (which is used in the events of ties).
		
• __str__ METHOD:
	The __str__ method, also known as the string method is used for printing out the attributes of a card instance. It uses the values of self.rank and self.suit from the class constructor to return the string. With the default arguments, the string method will return “2 of Diamonds”. However, if the instance is Card(0,13), the string method will return “King of Diamonds”.


Deck CLASS:
	The Deck class overall represents the deck of 52 cards, which is the typical number of cards in a traditional playing card deck. There are no inputs needed to create the deck of cards as it depends on the Card class mentioned above. Creating an instance of Deck will create a list that represents every card in a traditional playing card deck sorted by suits and ranks. 

• __init__ METHOD:
	The __init__ method does not require any input to create the deck of cards as it depends on the Card class that was previously created. The method creates a list, known as self.cards, that represents a single deck of cards and sorted by suits and ranks. It does this through a nested for loop that loops through a single suit and every card in that suit and appends them to the self.cards list and runs through all four of the suits. The __init__ method should create the list self.cards with 52 unique card objects that represent each card in a traditional playing card deck.

• __str__ METHOD:
	The __str__ method does not take any inputs. This method returns a multi-line string that contains the ordering of the cards in the self.cards list that was created in the __init__ method of the Deck class. 
	
	An example output would be: 

	“Ace of Diamonds”
	“2 of Diamonds”
	“3 of Diamonds”
	. . . and so on . . . 

• pop_card METHOD:
	The pop_card method takes the Deck object and also the optional input of “i” and takes the card at the index “i” and removes it from the “self.cards” list. This method essentially removes a specific card from the deck of cards that is contained in the list. The optional input (“i”) has a default value of “-1” which represents the last card object out of the deck.

• shuffle METHOD:
	The shuffle method does not have any inputs and used the random module which has been imported and puts the list of cards in a random order, similar to the cards being “shuffled”.

• replace_card METHOD:
	The replace_card method takes in the input of a card. For every card in the Deck, that card will be appended to the list “card_strs”. In addition, if the card is not already in the deck, as it may have been removed via the pop_card method, that card is also added to the “card_strs” list.

• sort_cards METHOD:
	The sort_cards method is very similar to the __init__/constructor method as it remakes the deck in a sorted way. However, there is the assumption that one cannot have more than 52 cards in a deck. There are also no inputs associated with this method. The difference with this method and the __init__ method is the method in which they are called. The __init__ method is automatically called with “Deck()”, but to call the sort_cards method, an instance would already have to be created. For example if x = Deck(), the __init__ method is automatically called, but to call the sort_card method, it would have to be “x.sort_cards()”.
	

Hand CLASS:
	The Hand Class and a single instance of it represents the hand of cards for a game, with basic functionality that is the number of card attributes. There is a default to the number of cards that a player can have per game which is set at 5, but it can be altered if necessary. 

• __init__ METHOD:
	The __init__/Constructor method takes in two inputs: deck_to_use and num_cards. The constructor uses these two inputs to create a hand, with the max number of cards set at the value of num_cards. The hand is created by the “deck_to_use” which references the Deck and Card classes mentioned earlier. 

• place_card METHOD:
	The place_card method has an optional input “i” that is defaulted at i = 0 which represents the first card in the hand. It is very similar to the pop_card method from the Deck class. However, the place_card method only acts on the cards in the hand and not the entire deck. By default, it removes the first card in the hand unless the input “i” is altered to remove an alternative card at that specific index. The card from the hand that is removed is returned.   	

• get_suits_available METHOD:
	The get_suits_available method has no inputs. It returns a list of all the suits that are in the current hand.

• get_ranks_available METHOD:
	The get_ranks_available method has no inputs. It returns a list of all the ranks that are in the current hand.

• specific_card METHOD:
	The specific_card method takes in two inputs: suit and rank. With the input, the method checks if any card in the hand matches the input and if so, calls the place_card method and removes that card from the hand and returns it. If there is no card in the hand that matches the input, the method returns “None”.
 
• add_card METHOD:
	The add_card method has an input of a card, which will be added to the hand. There is the assumption that we are working with one deck so there should not be any identical cards. This method adds the cards in the hand to a list and if the card input is not already in that list, it will add that card to the hand. 

• __str__ METHOD
	The __str__ method has no inputs. This method returns a multi-line string listing each card in the hand.	

Test Cases:
	Checking Code using UnitTesting!

• ProblemSet2Tests:
	Test Cases from Problem Set #2 that test the Card + Deck Classes

• HandClassTests:
	New Test Cases that test the Hand Class

** More description can be seen in the code file**


