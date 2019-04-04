Obstacle[] obstacles = new Obstacle[5]; // list of game obstacles


class Obstacle{

  int size = 40;
  int x_pos;
  int y_pos;


  Obstacle(int x, int y){
    x_pos = x;
    y_pos = y;
  }
  
  void move_x(int amount, int direction){
  
  
  if (direction > 0){
  x_pos += amount;
    }
    
  else{
  x_pos -= amount;
    }
  }
  
  /**Validates if obstacle has hit rigt wall*/
  void check_walls(){
  if (x_pos >= width){
    x_pos = 0;
    y_pos = int(random(height));
  
    } // end if statement
  } // end check_walls
} // end of obstacle class


Obstacle obstacle_1 = new Obstacle(10,15);

void setup(){
  // TODO Make list 
size (500,500);

}

void draw(){
  background(0);
  
  
  rect(obstacle_1.x_pos, obstacle_1.y_pos, obstacle_1.size, obstacle_1.size);
  obstacle_1.move_x(5, 1);
  obstacle_1.check_walls();
  
}



//
