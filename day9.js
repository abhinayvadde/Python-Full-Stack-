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