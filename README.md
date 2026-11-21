# my_first_python_game
I'm currently learning python and this is my first "console game"


My requirements for this exam were :
Project Exam: “Survive 5 Days on the Island”
Create a game in which the player tries to survive on an island for five days. At the beginning of each expedition, the player enters their name.
Main Menu
The program displays this menu and returns to it after each action:
1. Start a new expedition
2. View expedition history
3. View statistics
4. Quit
If the player enters an option that does not exist, the program displays a message and asks them to choose again.
Starting an Expedition
At the beginning of each expedition, the player has:
- 100 health points;
- 3 portions of food;
- 3 portions of water;
- 0 exploration points.
The goal is to stay alive for five days. The player loses if their health reaches 0.
Each Day
At the beginning of each day, the player consumes one portion of food and one portion of water.
- If the player has the required resource, that resource decreases by one portion.
- If the player does not have food or water, their health decreases by 15 points for each missing resource.
- Resources cannot drop below 0, and health cannot drop below 0 or rise above 100.
- If health reaches 0, the expedition ends in a loss.
If the player is still alive, they choose one action for that day:
1. Search for food: Receive a random amount of 1 to 3 portions of food, but lose 5 health points.
2. Search for water: Receive a random amount of 1 to 3 portions of water, but lose 5 health points.
3. Rest: Recover 20 health points, up to a maximum of 100.
4. Explore the island: One of these events happens at random, with equal chances:
   - Find 2 portions of food and gain 10 exploration points.
   - Find 2 portions of water and gain 10 exploration points.
   - Get injured and lose 15 health points.
An invalid choice does not use up the day; the player is asked to choose again. After the action, the program displays the player’s remaining health and resources. If the player is still alive, they move on to the next day.

The player wins if they survive until the end of the fifth day.
Expedition Score
At the end of each expedition, whether won or lost, calculate the score as follows:
- 10 points for each day survived;
- plus the remaining health points;
- plus 5 points for each remaining portion of food or water;
- plus the exploration points earned.
The program displays whether the player won or lost, how many days they survived, and their final score.
History and Statistics
The history keeps track of expeditions played since the program started. For each expedition, display:
- the player’s name;
- the result: won or lost;
- the number of days survived;
- the final score.
The statistics display the number of expeditions, how many were won and lost, the highest and lowest scores, the total points, and the average score.

If the player requests the history or statistics before completing an expedition, the program displays a suitable message. The history must remain available while the program is running.
