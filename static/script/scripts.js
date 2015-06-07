$( document ).ready(init);

function init(){

	subm();
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

function subm () {
	$('#mailsubmit').click(function(event) {
		var email = $('#emailI').val();
		formEmail(email);
	});
	$('#mailsubmitA').click(function(event) {
		var email = $('#emailIA').val();
		formEmail(email);
	})
}

function formEmail (email) {
		var dataString = 'email_ohana='+ email;
		//alert(email);
		  //alert (dataString);return false;
		  $.ajax({
		    type: "GET",
		    url: "mail.php",
		    data: dataString,
		    success: function() {
		     console.log("success");
		     $('.success').toggleClass('visible');
		     window.setTimeout(function(event) {
		     	$('success').removeClass('visible');
		     },2000)
		    },
		    error: function() {
		    	console.log("Error");
		    }
		  });
		  return false;
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
