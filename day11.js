/*Element.addEventListener(event,function(){
    // block of code
});


let btn = document.getElementById("btn");
btn.addEventListener("click",function(){
    console.log("clicked")
})

let input = document.getElementById("searchInput");


input.addEventListener("keydown", function(e){
    console.log(e.target.value)
});


let url = "https://apis.ccbp.in/wiki-search?search=" + "abhi";
let options = {
    method : "GET"
};
fetch(url,options)
.then(function(response){
    return response.json();
})
.then(function(jsonData){
    console.log(jsonData);
})
    */


let randomNo = Math.ceil(Math.random()*100);
let input = document.getElementById("searchInput");
let btn = document.getElementById("btn");
let p = document.getElementById("result");


let userInput;

input.addEventListener("change", function(e){
    userInput =(e.target.value);
    console.log(userInput);
});
btn.addEventListener("click", function(){
    if (parseInt(userInput)===randomNo){
        p.textContent = "You won";
    }else if(userInput< randomNo){
        p.textContent = "You gussed too low";
    }else{
        p.textContent = "you gussed too high";
    }
});

