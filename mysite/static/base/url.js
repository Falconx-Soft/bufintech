function hov(x){
	x.innerHTML = "Subscribe";
	x.classList.remove("blurLinks");
	x.classList.add("unblurLinks");
	
}

function hovOut(x){
	x.innerHTML = "https://www.itsatesingurl/test1/com/";
	x.classList.add("blurLinks");
	x.classList.remove("unblurLinks");
}