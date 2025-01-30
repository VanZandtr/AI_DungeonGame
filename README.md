# ChatGPT_DungeonGame
Developing a python text based Dungeon Game using only ChatGPT free version. Game is rebase off my original Zork inspired Dungeon Game that is in another repository that anyone can access. 

## Goals
* To emulate my other game using only AI (ChatGPT for now)
* To better my abilities at AI syntax writing
* To see if I can make a fun game without (or with very minimal) coding

## Chat GPT free edition restriction
* free tier has 10-16 messages of GPT-4o every 3 hours

## TODO
* 1/30/2025
  - Fix maze/battle logic under bugs
  - Add better intro and lore to text printouts
  - Add feature descriptions to be added to github
    
## Chat log history
* Day1_ChatGPT_Transcript.txt - 1/30/2025
  - Only manual coding a did was change "Skill" to "Skills" because chatgpt had deleted half the script from one iteration to the next
  - A query was wasted in getting chatgpt the current code because it had deleted the maze logic lol

## Bugs found to be fixed in following Day
* Day 1 - 1/30/2025
  - Maze is not connected correctly. Can't reach all rooms and can get stuck next to stairs room
  - Moving over a maze block does not clear out the block --> should become empty
  - Battle does not intiate when moving into a battle room
