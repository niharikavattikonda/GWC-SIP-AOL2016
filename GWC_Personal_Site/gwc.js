function introAlert(){
	alert("Welcome to my Girls Who Code Project Portfolio!");
}

function forwardPhotos(){
	if(document.getElementById("pic").src.match("gallery/obamicon_results.png")){
		document.getElementById("pic").src = "gallery/password_hashing.png";
	}
	else if(document.getElementById("pic").src.match("gallery/password_hashing.png")){
		document.getElementById("pic").src = "gallery/runner_game.png";
	}
	else if(document.getElementById("pic").src.match("gallery/runner_game.png")){
		document.getElementById("pic").src = "gallery/snow_scene.png";
	}
	else{
		document.getElementById("pic").src = "gallery/obamicon_results.png"
	}
}

function backwardPhotos(){
	if(document.getElementById("pic").src.match("gallery/obamicon_results.png")){
		document.getElementById("pic").src = "gallery/snow_scene.png";
	}
	else if(document.getElementById("pic").src.match("gallery/snow_scene.png")){
		document.getElementById("pic").src = "gallery/runner_game.png";
	}
	else if(document.getElementById("pic").src.match("gallery/runner_game.png")){
		document.getElementById("pic").src = "gallery/password_hashing.png";
	}
	else{
		document.getElementById("pic").src = "gallery/obamicon_results.png";
	}
}