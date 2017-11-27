Made in pygame module of python.
Images and sound clips source: Internet.
Colors defined in RGB values.
Highscore.txt file to keep track of high score.
Bird, pipe and background images are randomized.
Main game loop consists definitions of all the functions- bird, game over, high score(just defined), obstacle, score, play_again.
Bird
Mid-flap and fall-image of the bird as per requirement.
Game over
Displays ‘Game Over’, your score, high score and calls the play_again function.
Has the procedure to keep track of high score.
‘r’ key resets the high score.
Obstacle
Upper and lower pipes rendered as per requirement.
Score
Updates score and displays on the screen.
Play_again
Displays play again and quit commands in a window.
Enter key restarts the game.
Escape key quits the game.
Game variable values hard-coded – coordinates of bird, coordinates of upper and lower pipes, height and width of pipes, space between pipes, speed of pipes, downward and upward speed of bird, score.
Up_arrow key makes the bird go up, releasing the key makes it go down.
Crash tests:
For ground:
The bird can’t go below the screen. 
For upper pipe:
The bird shouldn’t touch the upper-pipe.
For lower pipe:
The bird shouldn’t touch the lower-pipe.
Any failure of crash test will result in game over.
Score increases by 1 point each time the bird crosses one unit of pipes.
Appropriate sound clips are added for respective functions.
>>> python flappy_bird2.py 
This command will run the game.



Developers:
Advait Lonkar – IMT2017002
Amogh Johri – IMT2017003
Sriram Gandikota - IMT2017018

				

