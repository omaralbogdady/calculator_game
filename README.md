# Calculator Game

## Video URL: <[insert here](https://www.youtube.com/watch?v=Ag5s_m2Caa4)>

# Description

My calculator game project has 2 Main Sections:

1. A regular Calculator
2. A 007 Game

## Calculator

When you first run the project, you will be asked for an equation, the format should be in the format: **[Number] [Operator] [Number]** You don’t need to place the spaces. The numbers may also be negative or positive, and they can also be decimals. The program only supports basic arithmetic: **addition, subtraction, multiplication, and division.**

Once the equation is given, and is in the correct format, the program will return the result and exit. If the equation is in the wrong format the program will return with a print of **`Invalid Input`**

## Game

When prompted for an equation, if you input `007` , the game will enter the game mode, and the program will print `You've entered the Game mode`.

### Preamble

When you first enter the game mode, you will see a preamble explaining the game:

`Welcome to 007,`
`A game about strategy, planning, and feeling like James Bond.`
`You and a computer have 3 options every turn:`
`1. Reload`
`2. Block`
`3. Shoot`
`Your mission is to take out the computer by shooting when the computer is reloading.`
`You can't shoot if you don't have any bullets, and you and the computer can stor bullets. Good Luck!`
`Your Highscore is {highscore} waves.`

If it is your first time playing the game, your high score will be 0.

### Wave

The game is split into waves, each wave you will have the choice to reload, block, or shoot. If you don’t have any bullets, your only options will be reload or block.

Once you have made your selection, the computer will make it’s selection. The computer has some logic to not make it totally random:

1. If the user and the computer have no bullets, it will only choose reload
2. If the user has at least 1 bullet and the computer has none, the computer will choose between blocking or reloading, and has a 65% chance of blocking vs reloading.
3. If the user has no bullets while the computer has at least one, the computer will choose between reloading or shooting, with a 80% chance of shooting vs reloading.

This should make the game more challenging, but more predictable.

Once you and the computer have made your choices, the program will check the choices and compare to see if anyone has lost or won, who reloaded, and who blocked, and will set the variables accordingly.

### Winning

If you win the game, you will see a message congratulating you and stating how many waves you won in.

#### Saving the Highscore

Once you win, the program will take the number of waves you won in, and check a file called `highscore.txt` :

- If the file exists, it will compare the value inside of it, if the value inside the file is lower (in a previous game you won in less waves), the program will not change
- If the file exists and your wave number is less than the one inside the file, it will set the value inside the file to your new highscore and print `Highscore Updated!`
- If the file doesn’t exist (This is your first time playing the game), the program will create the file, and put your highscore inside of it.

NOTE: Due to the way the game works, the lowest amount of waves you can win in is 2.

### Losing

If you lose the game, the program will exit and print `The Computer won in {wave} waves` .

---

By Omar Albogdady

This was CS50P