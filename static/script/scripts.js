$( document ).ready(init);

function init(){
	$('#mailsubmit').click(function() {
		alert($('.RegBar-inputMail').val());
		$.post("mail.php",{email: juan});
		console.log("holi");
	})
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
