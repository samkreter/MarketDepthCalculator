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
	        	$('#BTCChina-value').html(data['BTCChina']['coinsExchanged'].toFixed(8));
	        	$('#OKCoin-value').html(data['OKCoin']['coinsExchanged'].toFixed(8));
	        	if(data['GreaterBuyCoins'] === 'OKCoin'){
	        		$('#OKCoin-value').css("border-color","green");
	        		$('#BTCChina-value').css("border-color",'');
	        	}
	        	else{
	        		$('#BTCChina-value').css("border-color","green");
	        		$('#OKCoin-value').css("border-color",'');
	        	}
	        	
	    		$('#China-Exchange-Group').append('<label>Percent Differece</label><div id="percentDifference-value"class="form-control boldedNumbers shortBox">%'+data['PercentDifference'].toFixed(3)+'</div>')
	        }
	    });
	});

})