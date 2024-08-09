// TODO: The update Cells or Update board functions are very broken rn

// Assumes p5.js is imported on the page
// Creates a conways game of life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

// Setup cell information
const CELLSPERROW = 20;
const CELLSPERCOLUMN = 30;
const CELLSIZE = 25; // in px

// Setup canvas info
const CANVASWIDTH = CELLSIZE * CELLSPERROW;
const CANVASHEIGHT = CELLSIZE * CELLSPERCOLUMN;

gameOfLife = null

function setup() {
    createCanvas(CANVASWIDTH, CANVASHEIGHT);
    background(255,255,255);
    if (gameOfLife == null){
      gameOfLife = generateRandomBoard(CELLSPERCOLUMN, CELLSPERROW)

    }
    // updateBoard(gameOfLife);
    drawBoard(gameOfLife); // Draw initial Board
}

function generateRandomBoard(columns, rows){

  let board = []

  for (let i = 0; i < columns; i++) {
    // Itterate Columns
    let currentRow = []
    for (let j = 0; j < rows; j++) {
      // Itterate Row within column
      currentRow.push(Math.round(Math.random() *.7))
    }
    board.push(currentRow)
  }
  return board
}

function updateCell(board, row, column) {
  let liveNeighbours = 0

  if (!row == 0) {
    if (!column == 0) {
      // NW 
      if (board[row-1][column-1] == 1){
        liveNeighbours += 1
      }
    }
    // N  
    if (board[row-1][column] == 1){
      liveNeighbours += 1
    }
    if (!column == CELLSPERCOLUMN - 1) {
      // NE 
      if (board[row-1][column+1] == 1){
        liveNeighbours += 1
      }
    }
  }
  if (!column == 0) {
    // W  
    if (board[row][column-1] == 1){
      liveNeighbours += 1
    }
  }
  if (!column == CELLSPERCOLUMN - 1) {
    // E  
    if (board[row][column+1] == 1){
      liveNeighbours += 1
    }
  }

  if (!row == CELLSPERROW - 1) {
    if (!column == 0) {
      // SW 
      if (board[row+1][column-1] == 1){
        liveNeighbours += 1
      }
    }
    // S  
    if (board[row+1][column] == 1){
      liveNeighbours += 1
    }
    if (!column == CELLSPERCOLUMN - 1) {
      // SE 
      if (board[row+1][column+1] == 1){
        liveNeighbours += 1
      }
    }
  }

  if (liveNeighbours==2 || liveNeighbours == 3 || liveNeighbours == undefined){
    console.log("Live neighbours: ", liveNeighbours)
  }

  if (board[row][column] == 1){
    // Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if ((liveNeighbours < 2)){
      return 0
    }
    // Any live cell with two or three live neighbours lives on to the next generation.
    else if ((liveNeighbours == 2) || (liveNeighbours == 3)){
      return 1
    }
    // Any live cell with more than three live neighbours dies, as if by overpopulation.
    else if (liveNeighbours > 3 ){
      return 0
    }
  }
  
  // Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
  else if ((liveNeighbours == 3) && board[row][column] == 0 ){
    return 1
  } 
  else {
    
    return board[column][row]
  }
}

function updateBoard(board){
  console.log(board)
  for (let index = 0; index < CELLSPERCOLUMN; index++) {
    for (let jindex = 0; jindex < CELLSPERROW; jindex++) {
      board[index][jindex] = updateCell(board, jindex, index)
      
    }
  }


}


function drawBoard(board){
  for (let i = 0; i < CELLSPERCOLUMN; i++) {
    // Itterate Columns
    ypos = i * CELLSIZE
    for (let j = 0; j < CELLSPERROW; j++) {
      // Itterate Row within column
      xpos = CELLSIZE * j
      if (board[i][j] == 1){
        fill(0)
      } else{
        noFill()
      }
      square(xpos,ypos,CELLSIZE)
    }
  }
}
  
function draw() {

  background(255,255,255);
  drawBoard(gameOfLife);

}