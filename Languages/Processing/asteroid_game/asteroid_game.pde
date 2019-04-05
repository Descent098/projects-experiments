/**A game in which the player dodges asteroids
requirements:
1. Object Oriented
2. Limited Global Variables (ideally none)
3. Player movement via mouse movement
4. Obstacle-Player collision detection
5. Game ends on collision between player and obstacle
*/

int obstacle_amount = 5; // amount of obstacles to generate
Obstacle[] obstacles = new Obstacle[obstacle_amount]; // list of game obstacles

class Obstacle{
  // Instance Variables
  int x_pos;
  int y_pos;
  int step;
  
  // Class Variables
  int size = 40;

  /** Primary Constructor
  ============== Paramaters ==============
  int x; Value of initial x position
  int y; Value of initial y position
  int stp; Amount, in pixels to move by each frame*/
  Obstacle(int x, int y, int stp){
    x_pos = x;
    y_pos = y;
    step = stp;
  } // end of primary constructor
  
  
  /**Moves obstacles in x direction by instances' step value 
  ============== Paramaters ==============
  int direction; if positive it will increment x by the step value (move right), 
  if negative it will decrement x by the step value (move left)*/
  void move(int direction){
  if (direction > 0){
  x_pos += step;
    }// end if
  else{
  x_pos -= step;
    }// end else
  }// end move
  
  
  /**Validates if obstacle has hit a wall, if so */
  void check_walls(){
    
  // Right Wall
  if (x_pos > width){
    x_pos = 0;
    y_pos = int(random(height-size));
    } // end if statement
    
  
  // Left Wall
  if (x_pos < 0){
    x_pos = width;
    y_pos = int(random(height-size));
    } // end if statement
  } // end check_walls
} // end of obstacle class



void setup(){
  size (500,500);
  
  // Fill obstacles array with obstacle instances
  int current_y = 10; // The current iterations y value
  for(int obs = 0; obs <= obstacle_amount-1; obs ++){
    obstacles[obs] = new Obstacle(0, current_y, 10);
    current_y += 50; // increment next instances' y value to avoid overlap
  } // end of for loop
} // end of setup

void draw(){
  background(0);
  
  // Draw obstacles
  int direction = 1;
  for(int obs = 0; obs <= obstacle_amount-1; obs ++){
    rect(obstacles[obs].x_pos, obstacles[obs].y_pos, obstacles[obs].size, obstacles[obs].size);
    obstacles[obs].move(direction);
    obstacles[obs].check_walls();
    direction*= -1; // Make next instance move in oposite direction
  } // end of for loop
  
} // end of draw
