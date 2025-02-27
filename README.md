# Organize Meeting Rooms

In this project, I have designed a function to help organize multiple meetings during a day. Each
meeting will have a start time and end time. Each meeting will need to reserve a private conference
room during that time. Your function will take all the meeting schedules and calculate the minimum
number of conference rooms you will need.

# Requirements:

1. The function will take the input as a sequence of lists, each list only contains two numbers, the
start time and the end time.
For simplicity, we assume the time is just a float number in the range of 0.0 to 24.0.

  For example, the function may be given the following input:

  findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0])

  Our code should return 3 as the result, since during this time window [3.1, 3.4], all three
  meetings will be going on in parallel.

  Another example:

  findMinRooms([1.2, 3.4], [2.3, 5.0], [4.1, 8.0])

  this will return 2. 

  Another example:

  findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0], [1.0, 10.0])

  this will return 4.

3. Our function should be able to handle any number of arguments.

4. The sequence of meetings can be input in any order.

5. Our function should handle all wrong inputs gracefully, by catching all errors and display
meaningful error messages. There should be no error/crash from the system.

6. Don’t do brutal force O(N^2) implementation, i.e., by checking each meeting against every other
meeting to count the time overlaps.
Hint: You will need to re-organize and sort the data in some way, after that, you only need to go through the data once to find the answer.

8. You should be able to implement using only what we learned in class so far.

9. You are encouraged to discuss with other students about the high-level ideas, but never share
anything at code level. You will have to write your own code independently. Plagiarism will be
detected and reported.
