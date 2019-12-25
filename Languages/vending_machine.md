# Vending machine

A vending machine is a great project to implement in each language for learning. I've outlined various 'stages' that are useful milestones to work towards. The stages are intended to force you to learn more advanced techniques and language features, but as you go through some of the stages will force you to refactor and redesign your code (just like a real software project).

I've split each stage up into a prompt (which would be what you would get from a client), an overview of the concepts that each stage reinforces, and a set of formal requirements that would be gathered based on the prompt. Also keep in mind I haven't (and wont) include any front end development, but feel free to add it as your own challenge if that's your thing.

## Stages

### Stage 1 (MVP)

You have been hired by a vending machine manufacturer to write the backend for their next set of vending machines. They have asked you to start working on an mvp with the requirements outlined below.

*Concepts:*

State management and somewhat complicated processing/data structures

***Requirements:***

- Be able to add credit.
- Remove credit based on purchases and determine the amount of change to give back.

### Stage 2; improved readability

The team has asked you to make the MVP more readable, so they can show it off. They want you to be able to give an in-terminal display of what actual change (coins and or bills) users will be given back after a purchase (localize as you see fit).

*Concepts:*

State conversion to real world recognizable types.

***Requirements:***

- Be able to tell you how many of each coin/bill type should be given back to you i.e. For CAD$3.35 in change you would get: 1 Toonie($2), 1 Loonie($1), 1 Quarter($0.25) and 1 dime($0.10).
- You only need to do this for your own regions currency.

### Stage 3; Inventory and Error checking

Now that the basics are in place it's time to start making the project suited for the real world. If you don't have any of a certain product left then you should print a message and leave the credit untouched to allow the user to choose a product that is in stock. Additionally you should allow the user to refund their credit and return what they have put in.

*Concepts*
Error checking on standard cases, handling of mutable state and multi-option flows that modify state.

**requirements**
- Print a message on selection of a product that's out of stock; "This product is out of stock please select another". The credit should be left **untouched**
- Have an option to refund the amount currently inside the machine this should zero out the balance and return the proper amount of change.

### Stage 4; Scope shift

You may have realized if you have ever seen a vending machine that if you select a different column that contains the same product then it just goes to one that has it in stock. For example if all the top rows have cola then if you select a row column pair with none left then the machine will pick another from the same row.

I have included some test cases, this is a common technique project planners use to make sure functionality is made to spec. 

*Concepts*
Code refactoring, scope shift, and functionality with many ways to implement.

**Requirements**
- If a **product** is out of stock a message saying the product is out of stock should appear; "\<product name\> is out of stock".
- This change **should not** break existing functionality
- When you run the tests the expected outcome should happen.

**Testing steps**
1. Pick a product and add it to multiple row/column pairs. 
2. Add enough funds to empty the stock.
3. Continuously buy from one of the row/column pairs until it runs out of stock.
4. Try to purchase from the row again
5. **Purchase should take stock from another row/column pair of the same product**
6. Buy from remaining row/column pairs until they are all out.
7. Try to buy from one of the row/column pairs.
8. **Out of stock message should display and nothing should be taken from the balance**
