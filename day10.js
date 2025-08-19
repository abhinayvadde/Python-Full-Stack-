/*
let h1 = document.createElement("h1");
console.log(h1)
let div = document.getElementById("root");
let h2 = document.createElement("h1");
h1.textContent = "Hello World!"
console.log(div);


let div = document.getElementById("root");
let h1 = document.createElement("h1");
h1.textContent = "Hello World !"
div.appendChild(h1)
console.log(div);

// Dice logic 
console.log(Math.ceil(Math.random()*6))
// here using floor we can go to before nearest value which is opp. of ceil
console.log(Math.floor(Math.random()*6))




let myArray = [5,"six",2,8.2];
console.log(myArray);
console.log(myArray[0]);




let n = document.getElementById("n")
function n(){
    n.textContent = "234G5A0201"
    n.style.backgroundColor("red")
}



let counter = 0;
let id = setInterval(function(){
    console.log(counter);
    counter = counter + 1;
},1000) 

clearInterval(id);
*/


greenlyt = document.getElementById("green");
orangelyt = document.getElementById("orange");
redlyt = document.getElementById("red");

function green(){
    greenlyt.classList.add("green");
    redlyt.classList.remove("red");
    orangelyt.classList.remove("orange");
}

function orange(){
    orangelyt.classList.add("orange");
    redlyt.classList.remove("red");
    greenlyt.classList.remove("green");
}
function red(){
    redlyt.classList.add("red");
    greenlyt.classList.remove("green");
    orangelyt.classList.remove("orange");
}



greenlyt = document.getElementById("green");
orangelyt = document.getElementById("orange");
redlyt = document.getElementById("red");

function green(){
    greenlyt.classList.add("green");
    redlyt.classList.remove("red");
    orangelyt.classList.remove("orange");
}

function orange(){
    orangelyt.classList.add("orange");
    redlyt.classList.remove("red");
    greenlyt.classList.remove("green");
}
function red(){
    redlyt.classList.add("red");
    greenlyt.classList.remove("green");
    orangelyt.classList.remove("orange");
}

let current = 0;
const colors = [green, orange, red];

function changeColor() {
    colors[current]();
    current = (current + 1) % colors.length;
    setTimeout(changeColor, 3000);
}

changeColor();


setTimeout(function(){
    setTimeout(red, 1000);
    setTimeout(orange, 61000);
    setTimeout(green, 64000);
},0);

setInterval(function(){
     setTimeout(red, 1000);
    setTimeout(orange, 61000);
    setTimeout(green, 64000);
},93000);




let options = {
    method: 'GET',
};
fetch("https://gorest.co.in/public-api/users", options)
.then(function(response) {
    return response.json();
})
.then(function(jsonData){
   for(let i = 0; i < jsonData.data.length; i++){
        let {name,gender} = jsonData.data[i];
        let div1 = document.createElement("div");
        div1.classList.add("container");
        let h1 = document.createElement("h1");
        h1.textContent = name;
        let p1 = document.createElement("p");
        p1.textContent = gender;
        let root = document.getElementById("root");
        root.appendChild(div1);
        div1.appendChild(h1);
        div1.appendChild(p1);
       
    }
})



