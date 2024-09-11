/*
Created by a student
ISTE 422: Exercise 2: Improvised ETL
Date: 2/5/2016
Software used: Nodejs (No extra dependencies)
Why?: The reason I used nodejs is because we are dealing
with a json data format and nodejs is built to handle
that natively without any external plugins
*/

//Node JS dependencies for reading and writing files to the file system.
var fs = require('fs');

//Read the file from args
var filename = process.argv[2];

if (!filename) {
  console.log("Sorry, you need to add the json file as an argument to the program!");
  process.exit(0);
}


if(!fs.existsSync(filename)) {
  console.log("File not found!");
  process.exit(0);
}

var obj = JSON.parse(fs.readFileSync(filename,'utf8'));
//get the current date
var date = new Date();
//format the date to the YYYYMMDD.csv required for the submission.
var datef = date.getFullYear() + pad2(date.getMonth()+1) + pad2(date.getDate());
//to return string object
var csv = ""
//for loop to parse all items
for(var i = 0; i < obj.length; i++){
  //item is a single person
  var item = obj[i];
  //check if item has a creditcard then save the :name and :creditcard to the cvs object in the cvs format
  if(item.creditcard != null && item.email != null){
    csv += item.name + "," + item.email + "," + item.creditcard + "\n";
  }
}

//store the compiled cvs in a file formated YYYYMMDD.csv
fs.writeFile("./" + datef + ".csv", csv, function(err) {
    if(err) {
        console.log(err);
        process.exit(0);
    }
    console.log("The file was saved!");
});

//formating functino for manking numbebers 2 digits ex "2" -> "02"
function pad2(number) {
     return (number < 10 ? '0' : '') + number;
}
