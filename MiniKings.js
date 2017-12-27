//miniKings v0.0.1

//starting cell assignment and initialization
var startingNum = Math.floor(Math.random() * 10);
console.info(startingNum + " is the starting number");
var startingCell = document.querySelector(".a1");
switch(startingNum) {
  default:
    startingCell = document.querySelector(".a1");
    break;
  case 2:
    startingCell = document.querySelector(".a2");
    break;
  case 3:
    startingCell = document.querySelector(".a3");
    break;
  case 4:
    startingCell = document.querySelector(".b1");
    break;
  case 5:
    startingCell = document.querySelector(".b2");
    break;
  case 6:
    startingCell = document.querySelector(".b3");
    break;
  case 7:
    startingCell = document.querySelector(".c1");
    break;
  case 8:
    startingCell = document.querySelector(".c2");
    break;
  case 9:
    startingCell = document.querySelector(".c3");
    break;
}

startingCell.innerHTML = '<i class="material-icons">memory</i>'

var startingNumB = Math.floor(Math.random() * 10);
console.info(startingNumB + " is the starting number for blue");
var startingCellB = document.querySelector(".a1");
switch(startingNumB) {
  default:
    startingCellB = document.querySelector(".a1");
    break;
  case 2:
    startingCellB = document.querySelector(".a2");
    break;
  case 3:
    startingCellB = document.querySelector(".a3");
    break;
  case 4:
    startingCellB = document.querySelector(".b1");
    break;
  case 5:
    startingCellB = document.querySelector(".b2");
    break;
  case 6:
    startingCellB = document.querySelector(".b3");
    break;
  case 7:
    startingCellB = document.querySelector(".c1");
    break;
  case 8:
    startingCellB = document.querySelector(".c2");
    break;
  case 9:
    startingCellB = document.querySelector(".c3");
    break;
}
//end starting cell assignment


var spaceToChange = document.querySelector(".a1");
startingCell.style.backgroundColor = "orange";
startingCellB.style.backgroundColor = "blue";
var gold = 0;
var goldMeter = document.querySelector(".goldCount");

function clickOptions(spaceClicked) {
  var action = prompt("What would you like to do in this area? Type 1 for attacking, 2 for scouting, 3 for rebuilding, 4 for taxing.", "1, 2, 3 or 4");
  if(action !== null) {
   console.log(spaceClicked + " is what you clicked on.");
    switch(action) {
      default:
        alert("I DON't UNDERSTAND YOUR REQUEST");
        break;
      case "1":
        battle();
        break;
      case "2":
        spaceToChange = document.querySelector(spaceClicked);
        if(spaceToChange.style.backgroundColor == "blue") {
          alert("There is a empire here! Its stats are...");
        } else {
          alert("WHY ARE YOU SCOUTING DA TREES THAT U CONQERED/ WILL CONQUER?");
        }
        break;
      case "3":
        spaceToChange = document.querySelector(spaceClicked);
    }
  }
}


function battle() {
        spaceToChange = document.querySelector(spaceClicked);
        spaceToChange.style.backgroundColor = "orange";
        gold++;
        goldMeter.innerHTML = gold;
}
