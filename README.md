# AI Dungeon Game

### ---------- Begin AI Generated Text - **Last Updated 1/31/2025** ----------

### **Intro:**
Welcome to **AI Dungeon Game**, a text-based RPG where you explore a procedurally generated dungeon, fight dangerous creatures, and level up your hero!

### **Current Features:**
- **Procedural Dungeon Generation**: Explore a multi-layered dungeon with randomized rooms, battles, and treasures.
- **Playable Classes**: Choose from **Warrior, Mage, Rogue, and Cleric**, each with unique skills and abilities.
- **Turn-Based Combat**: Face off against **Goblins, Skeletons, Trolls, and even Dragons** with dynamic attack, defense, and skill mechanics.
- **Equipment System**: Find and equip weapons and armor to enhance your stats.
- **Item Drops**: Enemies have a chance to drop **healing and mana potions** to keep you going.
- **XP & Leveling System**: Gain experience, level up, and unlock powerful new abilities.
- **Boss Fights**: Conquer the dungeon and face a **mighty final boss**.

### **AI Suggested Upcoming Features:**
- More classes, skills, and enemy types
- Quests and story elements
- Expanded inventory and crafting system

### ---------- End AI Generated Text ----------

## Goals
* To emulate my other game using only free AI
* To better my abilities at AI syntax writing
* To see if I can make a fun game without (or with very minimal) coding

## Updates
* 1/30/2025
  - Fix maze/battle logic and classes under bugs
  - Add better intro and lore to text printouts
  - Add feature descriptions to be added to github

* 1/31/2025
   * Updates:
       * Moved to Claude, better code generation
       * Added Equipment, Potions, better fights, and fixed most bugs from 1/30/2025
       * Added better intro and lore to text printouts
       * Added feature descriptions to be added to github
    
  * Bugs:
       * Player is being healed between fights
       * Enemies are too strong on the first level
       * Probably should remove hiddeness of map

* 2/5/2025
   * Updates:
       * "Fixed" persistent health - the player healed to full on level up and I was mistaking this as a bug. For now I have it so a level up only restores 50% of lost health and mana
       * Dragon can only be found as last level boss
       * Made enemies easier on level 1
       * Modified maze to show full map instead of using ? for unexplored rooms - fixed issue where room wouldn't become an "empty" room
    
  * Bugs:
       * Troll is supposed to be non final level boss, but room isn't marked as 'X'

* 2/7/2025
  * Updates from Claude:
    * Today we made several key updates to the dungeon game:
      * Fixed boss monster system:
        * Ensured Troll only appears as marked boss ('X')
        * Removed Troll from regular battles
        * Added Dragon as final boss
        * Rebalanced monster difficulty scaling
      * Improved inventory system:
        * Moved inventory management from Maze to Character class
        * Added inventory access during movement phase
      * Enhanced map visibility:
        * Map now displays before each move prompt
        * Added cleaner map rendering
      * Added save/load system:
        * Saves character stats, inventory, and progress
        * Saves maze state and exploration
        * Allows loading previous game on startup
        * Uses JSON file format for save data
  * Updates from me:
    * Added equipping items before fights
    * TODO - add description when checking inventory to equipped items
    * TODO - combine inventory equip and use potion
    * TODO test save feature

* 2/14/2025
  * Updates from Claude
    * Added a pet system with two starter companions (Mystic Cat and Spirit Wolf), each providing unique passive bonuses to the player (mana or attack boost) and having their own combat abilities
    * Implemented pet combat mechanics where pets can attack enemies, take damage, and be knocked out (but not die permanently), with pets having a maximum of 8-10 HP depending on their type
    * Created a pet acquisition system with a 2% drop chance from regular monsters and 5% from bosses, limiting players to one pet at a time
    * Added pet healing through health potions (pets receive 50% of the potion's healing value) and implemented a system for managing pet passive bonuses when they're knocked out or revived
    * Fixed various bugs and added quality of life improvements, including better battle information display, clearer potion descriptions, proper save/load functionality for pets, and improved error handling
  * Updates from me:
    * Next day should be spent testing features and fixes - save seems to work pretty well!
    * TODO Add helment, gloves, boots, offhand, ring, and necklace to armor
    * TODO Lower xp gain rate and make monsters easier
    * TODO ignore case sensitive in inputs
    * TODO up pet drop rates
    * TODO see if I can reduce code lines - split into multiple files? Can claude handle that?

