$( function() {


	$('#CLP-submit').click(function(){
		$('#currency-input-hidden').val("CLP");
		$(this).submit();
	})

	$('#RMB-submit').click(function(){
		$('#currency-input-hidden').val("RMB");
		$(this).submit();
	})
	
	$(document).on("submit", "form", function(event){
	    event.preventDefault();
	    $.ajax({
	        url: '/is_ajax',
	        type: 'POST',            
	        data: new FormData(this),
	        processData: false,
	        contentType: false,
	        success: function (data, status){
	        	$('#BTCChina-value').html(data['BTCChina']['coinsExchanged']);
	        	$('#OKCoin-value').html(data['OKCoin']['coinsExchanged']);
	        	if(data['OKCoin']['coinsExchanged'] >= data['BTCChina']['coinsExchanged']){
	        		$('#OKCoin-value').css("border-color","green");
	        	}
	        	else{
	        		$('#BTCChina-value').css("border-color","green");
	        	}
	        }
	    });
	});

})