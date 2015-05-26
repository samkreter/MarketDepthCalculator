$( function() {


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

    	//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaCLP-RMB-value').html(china['BTCChina']['moneyExchanged'].toFixed(2));
    	$('#OKCoinCLP-RMB-value').html(china['OKCoin']['moneyExchanged'].toFixed(2));
    	$('#ChileBitCLP-RMB-value').html(chile['ChileBit']['coinsExchanged'].toFixed(8));
    	//create the best path green borders 
    	$('#'+china['Best']+'CLP-RMB-value').css("border-color","green");
    	$('#'+chile['Best']+'CLP-RMB-value').css("border-color","green");

    	$('#CLP-RMB-Result').html(china[china['Best']]['moneyExchanged'].toFixed(2))

  //   	//added the actual exchnage rate box to the page 
  //   	$('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
		
		// //add the percent differnce box to the page 
		// $('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+china['PercentDifference'].toFixed(3)+'</div>')
	}

	function RmbBrl(data){
		china = data['China']
    	brazil = data['Brazil']
    	//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaRMB-BRL-value').html(china['BTCChina']['coinsExchanged'].toFixed(8));
    	$('#OKCoinRMB-BRL-value').html(china['OKCoin']['coinsExchanged'].toFixed(8));
    	$('#FoxBitRMB-BRL-value').html(brazil['FoxBit']['moneyExchanged'].toFixed(2));
    	
    	$('#'+china['Best']+'RMB-BRL-value').css("border-color","green");
    	$('#'+brazil['Best']+'RMB-BRL-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#RMB-BRL-Result').html(brazil[brazil['Best']]['moneyExchanged'].toFixed(2))
    	// $('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
		
		//add the percent differnce box to the page 
		$('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+china['PercentDifference'].toFixed(3)+'</div>')

	}

	function BrlRmb(data){
		//make working with the data easier to understand 
		brazil = data['Brazil']
		china = data['China']

		//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaBRL-RMB-value').html(china['BTCChina']['moneyExchanged'].toFixed(2));
    	$('#OKCoinBRL-RMB-value').html(china['OKCoin']['moneyExchanged'].toFixed(2));
    	$('#FoxBitBRL-RMB-value').html(brazil['FoxBit']['coinsExchanged'].toFixed(8));
    	//create the best path green borders 
    	$('#'+china['Best']+'BRL-RMB-value').css("border-color","green");
    	$('#'+brazil['Best']+'BRL-RMB-value').css("border-color","green");

    	$('#BRL-RMB-Result').html(china[china['Best']]['moneyExchanged'].toFixed(2))
	}


	function RmbVef(data){
		china = data['China']
    	venezuela = data['Venezuela']
    	//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaRMB-VEF-value').html(china['BTCChina']['coinsExchanged'].toFixed(8));
    	$('#OKCoinRMB-VEF-value').html(china['OKCoin']['coinsExchanged'].toFixed(8));
    	$('#SurBitCoinRMB-VEF-value').html(venezuela['SurBitCoin']['moneyExchanged'].toFixed(2));
    	
    	$('#'+china['Best']+'RMB-VEF-value').css("border-color","green");
    	$('#'+venezuela['Best']+'RMB-VEF-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#RMB-VEF-Result').html(venezuela[venezuela['Best']]['moneyExchanged'].toFixed(2))
    	// $('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    
		
		//add the percent differnce box to the page 
		$('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+china['PercentDifference'].toFixed(3)+'</div>')

	}



	function VefRmb(data){
		//make working with the data easier to understand 
		venezuela = data['Venezuela']
		china = data['China']

		//add the bitcoin amounts to the appropriote boxes 
    	$('#BTCChinaVEF-RMB-value').html(china['BTCChina']['moneyExchanged'].toFixed(2));
    	$('#OKCoinVEF-RMB-value').html(china['OKCoin']['moneyExchanged'].toFixed(2));
    	$('#SurBitCoinVEF-RMB-value').html(venezuela['SurBitCoin']['coinsExchanged'].toFixed(8));
    	//create the best path green borders 
    	$('#'+china['Best']+'VEF-RMB-value').css("border-color","green");
    	$('#'+venezuela['Best']+'VEF-RMB-value').css("border-color","green");

    	$('#VEF-RMB-Result').html(china[china['Best']]['moneyExchanged'].toFixed(2))
	}


	$(document).on("submit", "form", function(event){
	    event.preventDefault();
	    $('#loading-modal').modal('show');
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
	        		case 'RMB-BRL':
	        			RmbBrl(data);
	        			break;
	        		case 'BRL-RMB':
	        			BrlRmb(data);
	        			break;
	        		case 'RMB-VEF':
	        			RmbVef(data);
	        			break;
	        		case 'VEF-RMB':
	        			VefRmb(data);
	        			break;
	        	}

	        	$('#loading-modal').modal('hide');
	        	
	        }
	    });
	});

})