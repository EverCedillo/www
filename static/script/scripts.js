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
	$('.slide-link').on('click',function(event) {
	    var target = $( $(this).attr('href') );
	    console.log($(window).scrollTop())
	    if( target.length ) {
	        event.preventDefault();
	        $('html, body').animate({
	            scrollTop: target.offset().top
	        }, 1300);
	    }
	});

}
$(window).scroll(function(event) {
	if($(window).scrollTop()==0){
		$('.logo-container').removeClass('visible');
		$('.Nav').removeClass('onScroll');
		$('.Reg-button').removeClass('RegBar-btn')
	}else{
		if(!($('.Nav').hasClass('onScroll'))){
			$('.logo-container').toggleClass('visible');
			$('.Nav').toggleClass('onScroll');
			$('.Reg-button').toggleClass('RegBar-btn');
		}
	}
})

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
