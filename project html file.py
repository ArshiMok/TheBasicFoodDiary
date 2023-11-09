# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:27:10 2021

@author: arsha
"""

<html>
<html lang="en-us">
<style>
body {
  background-image: url('https://cdn.pixabay.com/photo/2021/04/30/19/37/orange-6219723__480.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;  
  background-size: cover;
  background-position: left;
  background-blend-mode: normal;
}

h1 {text-align: center;}
body { margin: 50px 105px 100px 105px ;}}

body {background-color: PapayaWhip;}
style="font-family:sans-serif;"

body {
  font-family: Arial, Helvetica, sans-serif;
}

</style>

<body>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta charset="UTF-8">


<title> Food Diary </title>


<form action = "http://students.hi.gmu.edu/cgi-bin/amoktade/project.cgi">


<h1 style="background-color:rgba(255, 99, 71, 0.2); border:50px salmon; border-radius:8px; width: auto ; padding: 35px ; font-family:helvetica;">Welcome to Your Daily Food Diary! </h1>

</head>

<br>
<br>
<br>

	<label for = <"date"> Today's Date (MM/DD/YYYY): <br> </label>
	<input type = "text" id="date" name = "date"? style= border-radius:4px;> <br>

<p>How do you feel today? </p>


	<input type="radio" id="poor" name="mood" value="poor">
	<label for="poor">&#128553 Poor</label><br>
	
	<input type="radio" id="ok" name="mood" value="Ok">
	<label for="mood">&#128528 Ok</label><br>
 
	<input type="radio" id="good" name="mood" value="good">
	<label for="good">&#128578 Good</label><br>

	<input type="radio" id="great" name="mood" value="great">
	<label for="great">&#128512 Great</label><br>
 
	<input type="radio" id="awesome" name="mood" value="awesome">
	<label for="awesome">&#128513 Awesome</label><br>  
 
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
#more {display: none;}
</style>
</head>
<body>

<p>Did you sleep well last night?</p>

	<input type="radio" id="zero to four" name="sleep" value="zero to four">
	<label for="zero">0 - 4 hours</label><br>

	<input type="radio" id="five to seven" name="sleep" value="five to seven">
	<label for="no">5 - 7 hours</label><br> 
 
	<input type="radio" id="eight plus" name="sleep" value="eight plus">
	<label for="no">8+ hours</label><br>  


<br>
	<span id="elipses"></span><span id="more"> A good night's rest will always be beneficial. Reflect on your lifestyle, what times do you wake up and go to sleep? Do you nap often? (You can include this in the "Anything else you would like to add?" text box!) Think about what may need to change to accommodate for adequate sleep. Change takes time! so take it step by step. Check out  
	<a href="https://www.cdc.gov/sleep/about_sleep/how_much_sleep.html"> CDC's tips and recommendation on sleep. </a> </span> </p> <br> 
	<button type = "button" onclick="Tip1()"; id="sleepBtn"; style= border-radius:4px >Click for Tips and Recommendations</button> <br>
		
<script>
function Tip1() {
  var elipses = document.getElementById("elipses");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("sleepBtn");

  if (elipses.style.display === "none") {
    elipses.style.display = "inline";
    btnText.innerHTML = "Cick for Tips and Recommendations"; 
    moreText.style.display = "none";
  } else {
    elipses.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}
</script>
<br>
</body>

<p>Take a moment to think about all that you ate today or plan to eat, from sunrise to bedtime! <br> 
 Don't leave anything out! If you skipped any meals, snacks, or beverages, please put N/A.</p> <br>


	<label for = "breakfast"> Breakfast :</label> <br>
	<textarea id="breakfast" name="breakfast" style="font-family:sans-serif; border-radius:4px;font-size:1 em;">
	</textarea> <br>

	<label for = "lunch"> Lunch :</label> <br>
	<textarea id="lunch" name="lunch" style="font-family:sans-serif; border-radius:4px; font-size:1 em;">
	</textarea><br>

	<label for = "dinner"> Dinner :</label> <br>
	<textarea id="dinner" name="dinner" style="font-family:sans-serif; border-radius:4px; font-size:1 em;">
	</textarea><br>

	<label for = "snacks"> Snacks :</label> <br>
	<textarea id="snacks" name="snacks" style="font-family:sans-serif; border-radius:4px ;font-size:1 em;">
	</textarea><br>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
#extra {display: none;}
</style>
</head>
<body>

<p>How much was your liquid intake today?<br><br>
	<label for = "gwater"> Glasses of Water :</label>
	<input type="text" id="gwater" name = "gwater" style= border-radius:4px> <br>

	<label for = "otherbeverage"> Other Beverages :</label>
	<input type="text" id="otherbeverage" name = "otherbeverage" style= border-radius:4px> <br><br>

	<span id="elipses">...</span> <span id="extra"> Water intake is essential! To remain hydrated and well, aim to drink at least 5 glasses of water a day. While other beverages can add nutrients or be more enjoyable, keep in mind that water is the best source of hydration! Not all beverages are as nutritious as they are tasty,
	<a href="https://www.cdc.gov/healthyweight/healthy_eating/drinks.html">  learn more here. </a> </span> </p> <br> 
	<button type = "button" onclick="Rec()"; id="waterBtn" style= border-radius:4px;>Click for Tips and Recommendations</button> <br>
	
		
<script>
function Rec() {
  var elip = document.getElementById("elipses");
  var XText = document.getElementById("extra");
  var btnTxt = document.getElementById("waterBtn");

  if (elip.style.display === "none") {
    elip.style.display = "inline";
    btnTxt.innerHTML = "Click for Tips and Recommendations"; 
    XText.style.display = "none";
  } else {
    elip.style.display = "none";
    btnTxt.innerHTML = "Read less"; 
    XText.style.display = "inline";
  }
}
</script>
</body>
<br>
	

<p>Anything else you would like to add? </p>
	<label for = "comments"> </label>
	<textarea id="comments" name="comments" style="font-family:sans-serif;font-size:1 em; border-radius:4px;">
	</textarea><br>

<br>
<br>

<p>Your information will be stored on a server. To identify your specific data, please enter the following:</p>
	<label for = "fname"> First Name : <br></label>
	<input type="text" id="fname" name = "fname" style= border-radius:4px> <br>

	<label for = "lname"> Last Name : <br></label>
	<input type="text" id="lname" name = "lname" style= border-radius:4px> <br>

	<label for = "emaila"> Email Address : <br></label>
	<input type="text" id="emaila" name = "emaila" style= border-radius:4px> <br>



<br>
<br>


<button onclick = 'alert("Good submission! See you tomorrow!")'> Submit </button>
<input type="reset">
<br>
<br>

</form>
</body>

</html>
