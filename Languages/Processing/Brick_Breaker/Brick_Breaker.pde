/** Brick Breaker
Description:
Implement a breakout/brick breaker game
using the object oriented paradigm 

Requirements:
1. Every "object" must be a class
2. Collisions between the sides and top of screen
   must be implemented.
3. Game ends when ball hits the bottom of the screen
   or when the player clears all bricks from screen.
*/

// Global Variables
Paddle player = new Paddle(10,900, 200,50, 40);
Ball gameBall = new Ball(100, 200, 50, 5,-5);
Brick[][] bricks = new Brick[3][5];


void setup(){
size(1000,1000);

 int rowRed = int(random(235)) + 20; // color of bricks in a given row
 int rowGreen = int(random(235)) + 20; // color of bricks in a given row
 int rowBlue = int(random(235)) + 20; // color of bricks in a given row
 
 int row_health = 3; // How much health bricks in a given row have
 int currentBrickX = 0;
 int currentRowY = -50;
 
 // setup bricks
 for (int row = 0; row <=2; row ++){
   currentRowY += 75;
   currentBrickX = 25;
   for (int brick = 0; brick <= 4; brick ++){
     bricks[row][brick] = new Brick(row_health, rowRed, rowGreen, rowBlue, currentBrickX, currentRowY);
     currentBrickX += 200;
   }
   currentBrickX = 0;
   rowRed += random(235) + 20;
   rowGreen += random(235) + 20;
   rowBlue += random(235) + 20;
 }


}

void draw(){
  background(0);
  fill(255);
  player.checkCollisions();
  gameBall.moveBall();
  gameBall.checkCollisions(player.x_position, player.y_position, player.pad_length);
  rect(player.x_position, player.y_position, player.pad_length, player.pad_height); // Draw paddle
  ellipse(gameBall.x_position, gameBall.y_position, gameBall.radius, gameBall.radius); // Draw ball
  
  // Draw bricks
  for (int row = 0; row <=2; row ++){
     for (int brick = 0; brick <= 4; brick ++){
       fill(bricks[row][brick].brickRed, bricks[row][brick].brickGreen, bricks[row][brick].brickBlue);
       if (bricks[row][brick].health == 0){
       continue;
       }
       else{
         
         rect(bricks[row][brick].x_position, bricks[row][brick].y_position, bricks[row][brick].brickLength, bricks[row][brick].brickHeight);
       }
       
     }
   }
  
  
}



void keyPressed(){
  if (keyCode == RIGHT){
    player.x_position+= player.step;
  }
  
  if (keyCode == LEFT){
    player.x_position -= player.step;
  }
}


class Paddle{
  // instance variables
  int x_position;
  int y_position;
  int pad_length;
  int pad_height;
  int step; // value to move paddle by; equivolent to speed
  
  /** Paddle contructor; Paramaters:
   x_position; int
   y_position; int
   pad_length; int
   pad_height; int
   step; int
   */
  Paddle(int x_pos, int y_pos, int len, int hei, int stp){
    x_position = x_pos;
    y_position = y_pos;
    pad_length = len;
    pad_height = hei;
    step = stp; // Amount player moves by on each arrow key press
  }
  /** Checks if paddle has collided with wall, if it has this
  function will move player back where they should be */
  void checkCollisions(){
  // right wall collision
  if(x_position > (width - pad_length)){
    x_position -= step;
  }
  // Left wall collision
  if(x_position < 0){
    x_position += step;
  } 
 }// end of checkCollisions 
} // end of Paddle 

class Ball{
  int radius;
  int x_speed;
  int y_speed;
  int x_position;
  int y_position;
  
  Ball(int x_pos, int y_pos, int rad, int xSpeed, int ySpeed){
     radius = rad; 
     x_speed = xSpeed;
     y_speed = ySpeed;
     x_position = x_pos;
     y_position = y_pos;
  }
  
  /** change the x and y position based on speed values*/
  void moveBall(){
    x_position += x_speed;
    y_position += y_speed;
  }// end of moveBall
  
  void checkCollisions(int paddleX, int paddleY, int paddle_length){
    // Wall Collisions
    
    // Top collision
    if(y_position <= 0){
    y_speed *= -1;
    }
    // Bottom collision
    if(y_position >= (height + radius)){
    exit();
    }
    // Left wall collision
    if(x_position <= 0){
    x_speed *= -1;
    }
    // right wall collision
    if(x_position >= (width - radius)){
    x_speed *= -1;
    }
    
    // Paddle Collision
    if( 
    (((x_position + radius) >= paddleX  ) 
    && 
    ((x_position + radius) <= (paddleX + paddle_length)))
    && 
    ((y_position) == paddleY)){
    y_speed *= -1;
    }
  }// end of checkCollisions
} // end of ball


class Brick{
  int health;
  int brickRed;
  int brickGreen;
  int brickBlue;
  int x_position;
  int y_position;
  
  int brickLength = 150;
  int brickHeight = 50;
  int brickPadding = 50; // Space between each brick
  
  Brick(int hp, int brickR, int brickG, int brickB, int xpos, int ypos){
    health = hp;
    brickRed = brickR;
    brickGreen = brickG;
    brickBlue = brickB;
    x_position = xpos;
    y_position = ypos;
  }
  
  boolean checkCollision(int ballX, int ballY, int ballRadius){
    
    // Check left edge
    if ((ballX == x_position)
    &&
    ((y_position <= (ballY+ballRadius))
    && 
    ((y_position+ brickHeight) >= ballRadius))){
    health -= 1;
    return true;
    }
    else{
    return false;
    }
    
    // Check right edge
    
    // check top
    
    // check bottom
    
    
  }
}
