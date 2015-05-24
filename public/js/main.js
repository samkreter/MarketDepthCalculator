$( function() {

	//creating the tab funtionallity with bootstrap 
	$('#myTab a').click(function (e) {
	  e.preventDefault()
	  $(this).tab('show')
	})


	//set the correct data for which button the user clicked 
	$('#CLP-RMB-submit').click(function(){
		$(this).submit();
	})
	$('#RMB-CLP-submit').click(function(){
		$(this).submit();
	})
	
	function RmbClp(data){
		china = data['China']
    	chile = data['Chile']
    	//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaRMB-CLP-value').html(china['BTCChina']['coinsExchanged'].toFixed(8));
    	$('#OKCoinRMB-CLP-value').html(china['OKCoin']['coinsExchanged'].toFixed(8));
    	$('#ChileBitRMB-CLP-value').html(chile['ChileBit']['moneyExchanged'].toFixed(2));
    	
    	$('#'+china['Best']+'RMB-CLP-value').css("border-color","green");
    	$('#'+chile['Best']+'RMB-CLP-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#RMB-CLP-Result').html(chile[chile['Best']]['moneyExchanged'].toFixed(2))
    	// $('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
		
		//add the percent differnce box to the page 
		$('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+china['PercentDifference'].toFixed(3)+'</div>')
	}

	function ClpRmb(data){
		china = data['China']
    	chile = data['Chile']
    	console.log(china)
    	console.log(chile)

    	//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaCLP-RMB-value').html(china['BTCChina']['moneyExchanged'].toFixed(2));
    	$('#OKCoinCLP-RMB-value').html(china['OKCoin']['moneyExchanged'].toFixed(2));
    	$('#ChileBitCLP-RMB-value').html(chile['ChileBit']['coinsExchanged'].toFixed(8));
    	console.log(china['BTCChina']['coinsExchanged'])
    	//create the best path green borders 
    	$('#'+china['Best']+'CLP-RMB-value').css("border-color","green");
    	$('#'+chile['Best']+'CLP-RMB-value').css("border-color","green");

    	$('#CLP-RMB-Result').html(china[china['Best']]['moneyExchanged'].toFixed(2))

  //   	//added the actual exchnage rate box to the page 
  //   	$('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
		
		// //add the percent differnce box to the page 
		// $('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+china['PercentDifference'].toFixed(3)+'</div>')
	}


	$(document).on("submit", "form", function(event){
	    event.preventDefault();
	    $.ajax({
	        url: '/amount_form_ajax',
	        type: 'POST',            
	        data: new FormData(this),
	        processData: false,
	        contentType: false,
	        success: function (data, status){
	        	switch(data['currency']){
	        		case 'RMB-CLP':
	        			RmbClp(data);
	        			break;
	        		case 'CLP-RMB':
	        			ClpRmb(data);
	        			break;
	        	}
	        	
	        }
	    });
	});

})