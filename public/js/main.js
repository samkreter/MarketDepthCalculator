$( function() {


	
	function differenceHighlight(data){
		if(data['percentDifference'] < 0){
    		$('.percentDifference-value').css("border-color","red");
    	}
    	else{
    		$('.percentDifference-value').css("border-color","green");
    	}
	}

	function handleExchangeData(data){
		curr1 = data['currency'].substring(0,3);
    	curr2 = data['currency'].substring(4,7);

    	country1 = data[curr1];
    	country2 = data[curr2];

    	$.each(country1['exchanges'],function(index,element){
    		$('#'+index+data['currency']+'-value').html(country1['exchanges'][index]['coinsExchanged'].toFixed(8));
    	})

    	$.each(country2['exchanges'],function(index,element){
    		$('#'+index+data['currency']+'-value').html(country2['exchanges'][index]['moneyExchanged'].toFixed(2));
    	})
    	
    	$('#'+country1['Best']+data['currency']+'-value').css("border-color","green");
    	$('#'+country2['Best']+data['currency']+'-value').css("border-color","green");
    	//added the actual exchnage rate box to the page 

    	$('#'+data['currency']+'-Result').html(country2['exchanges'][country2['Best']]['moneyExchanged'].toFixed(2))
    	// $('.inner-container').prepend('<div id="real-exchange-rate" class="row"><div class="col-md-2 center-bootstrap text-center"><label>Actual Exchange Rate</label><div id="BTCChina-value"class="form-control boldedNumbers" ></div></div></div>')	    

		//add the percent differnce box to the page 
		$('#first-exchange-block'+data['currency']).append('<label>Bitnexo Exchange Rate</label><div class="form-control boldedNumbers shortBox">'+data['bitnexoExchangeRate'].toFixed(2)+'</div>')
		
		$('#'+data['currency']+'-Result').after('<label>Percent Differece</label><div class="form-control boldedNumbers shortBox percentDifference-value">%'+Math.abs(data['percentDifference']).toFixed(3)+'</div>')

		differenceHighlight(data)
	}


	function errorHandling(errors){
		$(".tab-content").prepend('<div class="errors-formating">'+errors+'</div>');
		$('#loading-modal').modal('hide');

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
	        	if(data["errors"]){
	        		errorHandling(data.errors);
	        		return;
	        	}
	        	
	        	handleExchangeData(data);

	        	$('#second-exchange-block'+data['currency']).append('<label>Open 1 CNY to CLP Rate </label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">'+data['exhangeRate'].toFixed(2)+'</div>')
	        	$('#loading-modal').modal('hide');
	        	
	        }
	    });
	});

})