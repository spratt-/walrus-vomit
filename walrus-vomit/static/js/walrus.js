function redirect_to_advice() {
	window.location.replace("/advice");
}

function make_walrus_bigger() {
	$('#the-walrus').animate(
		{width: "600px"},
		6000, 
		redirect_to_advice);
}

function setup() {
	$('#the-walrus').click(make_walrus_bigger);
}

$(document).ready(setup
	/* pass in a function full of 
	crap to do when the page loads*/)