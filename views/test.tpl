<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Bitnexo Calculator</title>

    <!-- Bootstrap -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome --> 
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet">

    <!-- <link rel="stylesheet" type="text/css" href="font-awesome/fonts/fontawesome-webfont.woff2"> -->
    <!-- custome css -->
    <link href="main.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
	  <div class="container">
	  		<header>
	  			<div class="heder-logo">Bitnexo</div> 
	  		</header>
		  	<div class="inner-container">

		  		<div id="loading-modal"class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="loading-modal" aria-hidden="true">
					<div class="modal-dialog modal-sm">
						<div class="modal-content">
							<div class="loading">
							LOADING
							</div>
						</div>
	 				</div>
				</div>


		    	<form role="form">
					  <div class="row">
					  	<div class="form-group col-md-2">
					  	<button></button>
					  	</div>
						  <div class="form-group col-md-2">
						    <label>RMB</label>
						    <input type="number" name="amount-RMB-CLP" class="form-control"  placeholder="Enter Amount">
						    <button type="submit" class="btn btn-default btn-margin-fix">RMB Exchange</button>
						  </div>
						  <div id="first-exchange-blockRMB-CLP" class="form-group col-md-2">
						    <label>BTCChina</label>
						    <div id="BTCChinaRMB-CLP-value"class="form-control boldedNumbers has-success" ></div>
							<label>OKCoin</label>
						    <div id="OKCoinRMB-CLP-value"class="form-control boldedNumbers" ></div>
						  </div>
						  <div id="second-exchange-blockRMB-CLP"class="form-group col-md-2">
						    <label>Chilebit</label>
						    <div id="ChileBitRMB-CLP-value"class="form-control boldedNumbers" placeholder="Password"></div>
						    <label>SurBTC</label>
						    <div id="BTC-value"class="form-control boldedNumbers"></div>
						  </div>
						  <div class="form-group col-md-2">
						    <label>CLP</label>
						    <div id="RMB-CLP-Result"type="number"  class="form-control boldedNumbers" ></div>
						  </div>
						</div>
						<input id="currency-input-hidden" type="hidden" name="currency" value="RMB-CLP">
						<div class="form-group col-md-2">
							<button></button>
						</div>
				</form>
			</div>
		</div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="jquery-2.1.3.min.js"type="text/javascript"></script>
    <!-- // <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script> -->
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="bootstrap/js/bootstrap.min.js"></script>

    <script src="main.js"type="text/javascript"></script>
  </body>
</html>