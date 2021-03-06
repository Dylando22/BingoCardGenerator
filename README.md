# CS 1440 Assignment 3: Bingo! Design and Implementation

* [Instructions](./instructions/README.md)
* [Rubric](./instructions/Rubric.md)
* [Hints](./instructions/Hints.md)

Clone this repository and use it as a basis for your work.  Run each of these
commands one-at-a-time, without the '$' (that represents your shell's prompt).
Be sure to replace the words `LAST`, `FIRST`, and `USERNAME` with your own
names.

```
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3 cs1440-LAST-FIRST-assn3
$ cd cs1440-LAST-FIRST-assn3
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn3.git
$ git push -u origin --all
```

## Important!
**I have _specifically_  instructed the tutors in the Tutor Lab to  _not_  help you with the second portion of the assignment until you have completed the first draft of a UML class diagram.  Don't even think about writing code until you have thought through the design. Many software projects have gone awry because the design step had been neglected. Don't become another statistic - think first, code after.**


## Overview

For your next project at DuckieCorp you are tasked with writing an interactive
Bingo card generator.  This project had been started by our C++ team, but
partway through the customer and the project manager decided that Python would
be a better platform for this system.  The partially-completed C++ program was
translated into Python before the project was assigned to you.

You will create a complete programming product consisting of

*   A program which is extensible (can be easily modified)
*   Documentation (both technical and user-oriented)
*   Unit test cases

As you well know, creating a *programming product* can take up to 3x as much
time as just making a simple program.  Plan for this and carefully manage your
time so that you can meet the deadline.

## Objectives

*   Learn to design before you code
*   Study existing resources to identify requirements
    *   Read source code to identify which parts are already implemented
    *   Extract the customer's requirements from the specification
    *   Generate UML Class diagrams from source code
*   Extend a software system with new classes and features
    *   Design classes in UML first, then in code later
    *   Implement code to achieve the design
    *   Validate that your program is "doing the right thing"
*   Support your implementation work with unit tests
    *   Design code to meet the test's specifications
    *   Create or modify tests as your design evolves
    *   Verify that your program is "doing the thing right"
*   Write a users' manual at the appropriate level of detail


## This assignment consists of two deliveries with two due dates

* There is a delivery milestone in the middle of this assignment.
* You will use a single git repository for both submission.
* You will use a git tag to mark the boundary between the two deliveries and push your code to gitlab.cs.usu.edu to turn in your work.
* The grading gift can only be used for the 2nd delivery milestone.


### Design phase due Friday, October 22nd

This milestone includes the following components:

0.  1st draft of your UML diagram and peer reviews of the UML diagrams of **two** classmates.
1.  1st draft of your User's Manual.
2.  1st draft of your Software Development Plan
3.  1st draft of your Sprint Signature
4.  Tag the commit that concludes your design phase with the tag `designed`.
    *   The tag `designed` identifies to the graders when your 1st draft documents were completed.
    *   Push this tag to GitLab so that it is visible to the graders.
        `$ git push origin designed`
    *   The tag `designed` must be pushed _one week_ before the final due date.
    *   If the tag `designed` is missing or applied to a later commit the rubric points allocated to the 1st draft documents will be penalized according to the late submission policy outlined in the Course Rules.

I recommend [Diagrams.net](https://app.diagrams.net/) for drawing your UML diagrams. I don't really mind which drawing program you use so long as your diagrams

-   Are legible
-   Represent correct UML, at least as far as was discussed in class


### Implementation phase due Friday, October 29th

This submission includes the following components:

0.  The completed program
1.  A suite of meaningful, non-trivial unit tests
2.  The final draft of the UML class diagram
3.  The final draft of your User's Manual
4.  The final draft of your Software Development Plan
5.  The final draft of your Sprint Signature
