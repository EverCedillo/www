$( document ).ready(init);

function init(){
	/*$(window).on('beforeunload', function() {
		$('#Modal').toggleClass('visible');
    	return 'Your own message goes here...';
	});*
	fadeinShow();*/
	$('#RegContainer').click(function(event) {
		event.stopPropagation();
	})
	$('html').click(function() {
	//Hide the menus if visible
		$('#Modal-pane').removeClass('visible');
	});
	$('#ModalReg').on('click',function(event) {
		$('#Modal-pane').toggleClass('visible');
		event.stopPropagation();
	});
	$('.MainMenu-link').on('click',function(event) {
	    var target = $( $(this).attr('href') );
	    if( target.length ) {
	        event.preventDefault();
	        $('html, body').animate({
	            scrollTop: target.offset().top
	        }, 1300);
	    }
	});

}


function loadTimeLine(callback){
	jQuery.ajax({
		url:"nosotros.html",
		cache:false,
		dataType: "text",
		async:true,
		success: function (text) {
			callback(text);
		}

	});
}
function sendTimeLine(content) {
	$(coso).html(content);
}


/*
function bye(){
	alert("bye");
	console.log("bye")
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

*/
