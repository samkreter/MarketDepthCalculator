$( function() {


	
	function differenceHighlight(data){
		if(data['percentDifference'] < 0){
    		$('.percentDifference-value').css("border-color","red");
    	}
    	else{
    		$('.percentDifference-value').css("border-color","green");
    	}
	}

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
		$('#first-exchange-blockRMB-CLP').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#RMB-CLP-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')

		differenceHighlight(data)
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

    	$('#first-exchange-blockCLP-RMB').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#CLP-RMB-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
		differenceHighlight(data)
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
		$('#first-exchange-blockRMB-BRL').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')

		$('#RMB-BRL-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
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

    	$('#first-exchange-blockBRL-RMB').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#BRL-RMB-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
		
		differenceHighlight(data)
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
		$('#first-exchange-blockRMB-VEF').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')

		$('#RMB-VEF-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
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

    	$('#first-exchange-blockVEF-RMB').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
	
		$('#VEF-RMB-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
	}

	function ClpBrl(data){
		brazil = data['Brazil']
		chile = data['Chile']
		console.log(brazil)
		//add the bitcoin amounts to the appropriote boxes 
    	$('#FoxBitCLP-BRL-value').html(brazil['FoxBit']['moneyExchanged'].toFixed(2));
    	$('#ChileBitCLP-BRL-value').html(chile['ChileBit']['coinsExchanged'].toFixed(8));
    	
    	$('#'+brazil['Best']+'CLP-BRL-value').css("border-color","green");
    	$('#'+chile['Best']+'CLP-BRL-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#CLP-BRL-Result').html(brazil[brazil['Best']]['moneyExchanged'].toFixed(2))

    	$('#first-exchange-blockCLP-BRL').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')

    	$('#CLP-BRL-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
    	differenceHighlight(data)
	}

	function BrlClp(data){
		brazil = data['Brazil']
		chile = data['Chile']
    	//add the bitcoin amounts to the appropriote boxes 
    	$('#FoxBitBRL-CLP-value').html(brazil['FoxBit']['coinsExchanged'].toFixed(8));
    	$('#ChileBitBRL-CLP-value').html(chile['ChileBit']['moneyExchanged'].toFixed(2));
    	//create the best path green borders 
    	$('#'+brazil['Best']+'BRL-CLP-value').css("border-color","green");
    	$('#'+chile['Best']+'BRL-CLP-value').css("border-color","green");

    	$('#BRL-CLP-Result').html(chile[chile['Best']]['moneyExchanged'].toFixed(2))

    	$('#first-exchange-blockBRL-CLP').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#BRL-CLP-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
	}

	function ClpVef(data){
		venezuela = data['Venezuela']
		chile = data['Chile']
		//add the bitcoin amounts to the appropriote boxes 
    	$('#SurBitCoinCLP-VEF-value').html(venezuela['SurBitCoin']['moneyExchanged'].toFixed(2));
    	$('#ChileBitCLP-VEF-value').html(chile['ChileBit']['coinsExchanged'].toFixed(8));
    	
    	$('#'+venezuela['Best']+'CLP-VEF-value').css("border-color","green");
    	$('#'+chile['Best']+'CLP-VEF-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#CLP-VEF-Result').html(venezuela[venezuela['Best']]['moneyExchanged'].toFixed(2))

    	$('#first-exchange-blockCLP-VEF').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#CLP-VEF-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
		
		differenceHighlight(data)
	}

	function  VefClp(data){
		venezuela = data['Venezuela']
		chile = data['Chile']
    	//add the bitcoin amounts to the appropriote boxes 
    	$('#SurBitCoinVEF-CLP-value').html(venezuela['SurBitCoin']['coinsExchanged'].toFixed(8));
    	$('#ChileBitVEF-CLP-value').html(chile['ChileBit']['moneyExchanged'].toFixed(2));
    	//create the best path green borders 
    	$('#'+venezuela['Best']+'VEF-CLP-value').css("border-color","green");
    	$('#'+chile['Best']+'VEF-CLP-value').css("border-color","green");

    	$('#VEF-CLP-Result').html(chile[chile['Best']]['moneyExchanged'].toFixed(2))

    	$('#first-exchange-blockVEF-CLP').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#VEF-CLP-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
	}

	function BrlVef(data){
		venezuela = data['Venezuela']
		brazil = data['Brazil']
		//add the bitcoin amounts to the appropriote boxes 
    	$('#SurBitCoinBRL-VEF-value').html(venezuela['SurBitCoin']['moneyExchanged'].toFixed(2));
    	$('#FoxBitBRL-VEF-value').html(brazil['FoxBit']['coinsExchanged'].toFixed(8));
    	
    	$('#'+venezuela['Best']+'BRL-VEF-value').css("border-color","green");
    	$('#'+brazil['Best']+'BRL-VEF-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#BRL-VEF-Result').html(venezuela[venezuela['Best']]['moneyExchanged'].toFixed(2))

    	$('#first-exchange-blockBRL-VEF').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
	
		$('#BRL-VEF-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
	}

	function VefBrl(data){
		venezuela = data['Venezuela']
		brazil = data['Brazil']
		//add the bitcoin amounts to the appropriote boxes 
    	$('#SurBitCoinVEF-BRL-value').html(venezuela['SurBitCoin']['coinsExchanged'].toFixed(8));
    	$('#FoxBitVEF-BRL-value').html(brazil['FoxBit']['moneyExchanged'].toFixed(2));
    	//create the best path green borders 
    	$('#'+venezuela['Best']+'VEF-BRL-value').css("border-color","green");
    	$('#'+brazil['Best']+'VEF-BRL-value').css("border-color","green");

    	$('#VEF-BRL-Result').html(brazil[brazil['Best']]['moneyExchanged'].toFixed(2))

    	$('#first-exchange-blockVEF-BRL').append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#VEF-BRL-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')
	
		differenceHighlight(data)
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

	        		case 'CLP-BRL':
	        			ClpBrl(data);
	        			break;
	        		case 'BRL-CLP':
	        			BrlClp(data);
	        			break;

	        		case 'CLP-VEF':
	        			ClpVef(data);
	        			break;
	        		case 'VEF-CLP':
	        			VefClp(data);
	        			break;

	        		case 'BRL-VEF':
	        			BrlVef(data);
	        			break;
	        		case 'VEF-BRL':
	        			VefBrl(data);
	        			break;
	        	}
	        	$('#second-exchange-block'+data['currency']).append('<label>Open 1 CNY to CLP Rate </label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">'+data['exhangeRate'].toFixed(2)+'</div>')
	        	$('#loading-modal').modal('hide');
	        	
	        }
	    });
	});

})