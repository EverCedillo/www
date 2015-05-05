$( document ).ready(init);

function init(){
	
	fadeinShow();
}

function fadeinShow(){
	cont=0;
	banElements= document.getElementsByClassName('fadeInShow');
	$(banElements[cont]).toggleClass('visible');
	window.setInterval(function(){
		$(banElements[cont]).toggleClass('visible');
		cont=cont==banElements.length-1?0:cont+1;
		$(banElements[cont]).toggleClass('visible');
	}
	,3000);
}

