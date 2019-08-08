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
