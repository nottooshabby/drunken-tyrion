//This will be the first thing that I create in Java/coding. It will be a game of rock paper scissors
//and will let you select which on you want. I hope to have 2 player mode, along with a Vs. AI mode.
//I will try to make it as perfect as possible, but I am also just starting out.
//- Jonathon Fuller

var computerChoice = Math.random();
var player1Choice = prompt("Do you want to be rock, paper, or scissors?");

var game = function (rock,paper,scissors){
	if(computerChoice === player1Choice){
		console.log("It is a tie!");
	}
	
}