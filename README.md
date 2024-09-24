# HorribleCodeActivity

Explanation of Program:
A calculator programmed to calculate simple calculations of two integer values. The three operations implemented are addition, subtraction, and multiplication. The user inputs the desired values and chooses an operation to perform. 
 
KISS: 
Multiple class for simple task: In ViolatorSimpleCalculator I put each function into their own class, making for unnecessary instances in main. Instead, I can put these in one class.

DRY CODE: 
Repetition in operations: passing the same parameter values in each function when can condense it into one function using lambda.

Repetition In the def operation function: you will notice I used match-case statements, instead of if statement in the SimpleCalculator class. I did this to have a cleaner look and less repetition.

Document your code:  
Over-explanation: Unnecessary comments in self-explanation lines

Unhelpful: Most of these comments do not explain to the user what the line does
	
