$(document).ready(init);function init(){
	            if (document.createStyleSheet){
                document.createStyleSheet('css/normalize.css');
                document.createStyleSheet('css/Main.css');
            }
            else {
                $("head").append($("<link rel='stylesheet' href='css/normalize.css' type='text/css' media='screen' />"));
                $("head").append($("<link rel='stylesheet' href='css/Main.css' type='text/css' media='screen' />"));
            }populateDB1();populateDB2();$('#RegContainer').click(function(event){event.stopPropagation();})
$('html').click(function(){$('#Modal-pane').removeClass('visible');});$('#ModalReg').on('click',function(event){$('#Modal-pane').toggleClass('visible');$('#emailI').focus();event.stopPropagation();});$('.slide-link').on('click',function(event){var target=$($(this).attr('href'));console.log($(window).scrollTop())
if(target.length){event.preventDefault();$('html, body').animate({scrollTop:target.offset().top},1300);}});}function populateDB1(){$("#mailsubmit").click(function(){var email=$("#emailI").val();var dataString='email_ohana='+email;$.ajax({type:"POST",url:"mail.php",data:dataString,success:function(){console.log(":)")
console.log("success");$("#emailI").val("");$('.success').toggleClass('visible');window.setTimeout(function(event){$('.success').removeClass('visible');},2000);}});return false;});}function populateDB2(){$("#mailsubmitA").click(function(){var email=$("#emailIA").val();var dataString='email_ohana='+email;$.ajax({type:"POST",url:"mail.php",data:dataString,success:function(){console.log(":)")
console.log("success");$("#emailIA").val("");$('.success').toggleClass('visible');window.setTimeout(function(event){$('.success').removeClass('visible');},2000);}});return false;});}$(window).scroll(function(event){if($(window).scrollTop()==0){$('.logo-container').removeClass('visible');$('.Nav').removeClass('onScroll');$('.Reg-button').removeClass('RegBar-btn')}else{if(!($('.Nav').hasClass('onScroll'))){$('.logo-container').toggleClass('visible');$('.Nav').toggleClass('onScroll');$('.Reg-button').toggleClass('RegBar-btn');}}})