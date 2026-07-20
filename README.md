 Personal Expense Tracker.
The purpose of this program is to help users record their daily expenses, view all the expenses they have entered, calculate the total amount spent, and exit the program whenever they are finished.

The program is menu-driven, meaning the user selects an option from a menu."

The Four Menu Options
"At the beginning of the program, the user is shown four options:
Add Expense
View Expenses
View Total Expenses
Exit
The program keeps displaying these options until the user chooses Exit."

"This program uses a while loop.
A while loop repeats a block of code as long as a condition remains true.

In my program, the loop continues showing the menu so the user can perform multiple actions without restarting the program.

The loop only stops when the user selects option 4, which is Exit. At that point, the break statement ends the loop."


Start
   ↓
Display Menu
   ↓
User chooses an option
   ↓
Perform the action
   ↓
Back to Menu
   ↓
Exit?
No ───────────► Repeat
Yes
   ↓
Program Ends
Option 1 – Add Expense
"When the user selects option 1, the program asks for information about an expense.
For example:

Expense name
Amount spent
After entering the information, it is stored in a list.
A list is used because it can store many expenses instead of just one.

Every time the user adds another expense, it is appended to the list."

Example:

Food - 50
Transport - 20
Books - 100
Explain:
"The append() method adds each new expense to the end of the list."

Option 2 – View Expenses
"When the user selects option 2, the program displays every expense stored in the list.
To do this, I used a for loop.

A for loop goes through each item in the list one at a time and prints it."

Example output:

Food - GHC50
Transport - GHC20
Books - GHC100
Explain:
"If there are no expenses yet, the program informs the user that no expenses have been recorded."

Option 3 – View Total Expenses
"This option calculates the total amount spent.
The program adds together all the expense amounts.

For example:

Food = 50

Transport = 20

Books = 100

Total = 170

This allows the user to know how much money has been spent."

Option 4 – Exit
"When the user chooses option 4, the program displays a goodbye message.
Then it uses the break statement to stop the while loop.

This ends the program."

Example:

Thank you for using the Expense Tracker.
Goodbye!
Why I Used Lists
"I used a list because:
It stores multiple expenses.
It allows new expenses to be added easily.
It makes it easy to display all the expenses later."
Why I Used Variables
"I used variables to store information such as:
Expense name
Expense amount
User's menu choice
Variables help the program remember information while it is running."
Why I Used if, elif, and else
"The program needs to know which menu option the user selected.
I used:

if for option 1
elif for options 2, 3, and 4
else to handle invalid choices
If the user enters something like 7, the program tells them the choice is invalid instead of crashing."
Example Program Flow
===== Expense Tracker =====

1. Add Expense
2. View Expenses
3. View Total
4. Exit

Enter choice: 1

Expense Name: Food
Amount: 50

Expense Added Successfully!

Menu appears again.

Enter choice: 2

Food - GHC50

Menu appears again.

Enter choice: 3

Total Expenses = GHC50

Menu appears again.

Enter choice: 4

Goodbye!
Conclusion
"In conclusion, this project demonstrates the use of important Python concepts, including:
Variables
Lists
while loops
for loops
if, elif, and else statements
User input
The break statement
The program helps users keep track of their spending in a simple and organized way."
🌟
