$( function() {

	//set the correct data for which button the user clicked 
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
	        	//add the bitcoin amounts to the appropriote boxes 
	        	$('#BTCChina-value').html(data['BTCChina']['coinsExchanged'].toFixed(8));
	        	$('#OKCoin-value').html(data['OKCoin']['coinsExchanged'].toFixed(8));
	        	
	        	//find the bigger value and change the border color of that box
	        	if(data['GreaterBuyCoins'] === 'OKCoin'){
	        		$('#OKCoin-value').css("border-color","green");
	        		$('#BTCChina-value').css("border-color",'');
	        	}
	        	else{
	        		$('#BTCChina-value').css("border-color","green");
	        		$('#OKCoin-value').css("border-color",'');
	        	}
	        	//added the actual exchnage rate box to the page 
	        	$('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
	    		
	    		//add the percent differnce box to the page 
	    		$('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+data['PercentDifference'].toFixed(3)+'</div>')
	        }
	    });
	});

})