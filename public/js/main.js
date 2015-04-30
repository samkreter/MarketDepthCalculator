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
	        	alert(data);
	        }
	    });
	});

})