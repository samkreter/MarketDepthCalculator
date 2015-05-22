$( function() {

	//creating the tab funtionallity with bootstrap 
	$('#myTab a').click(function (e) {
	  e.preventDefault()
	  $(this).tab('show')
	})


	//set the correct data for which button the user clicked 
	$('#CLP-RMB-submit').click(function(){
		$('#currency-input-hidden').val("CLP-RMB");
		$(this).submit();
	})
	$('#RMB-CLP-submit').click(function(){
		$('#currency-input-hidden').val("RMB-CLP");
		$(this).submit();
	})
	

	$(document).on("submit", "form", function(event){
	    event.preventDefault();
	    $.ajax({
	        url: '/amount_form_ajax',
	        type: 'POST',            
	        data: new FormData(this),
	        processData: false,
	        contentType: false,
	        success: function (data, status){

	        	china = data['China']
	        	chile = data['Chile']
	        	//add the bitcoin amounts to the appropriote boxes 
	        	$('#BTCChina-value').html(china['BTCChina']['coinsExchanged'].toFixed(8));
	        	$('#OKCoin-value').html(china['OKCoin']['coinsExchanged'].toFixed(8));
	        	$('#ChileBit-value').html(chile['ChileBit']['moneyExchanged'].toFixed(8));
	        	
	        	$('#'+china['Best']+'-value').css("border-color","green");
	        	$('#'+chile['Best']+'-value').css("border-color","green");
	        	//added the actual exchnage rate box to the page 
	        	$('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
	    		
	    		//add the percent differnce box to the page 
	    		$('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+china['PercentDifference'].toFixed(3)+'</div>')
	        }
	    });
	});

})