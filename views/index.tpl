<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Bitnexo Calculator</title>

    <!-- Bootstrap -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
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

			    <form role="form">
				  <div class="row">
					  <div class="form-group col-md-3">
					    <label>RMB</label>
					    <input type="number" name="amount-RMB" class="form-control"  placeholder="Enter Amount">
					    <div id="RMB-submit" class="btn btn-default btn-margin-fix">RMB Exchange</div>
					  </div>
					  <div id="China-Exchange-Group" class="form-group col-md-3">
					    <label>BTCChina</label>
					    <div id="BTCChina-value"class="form-control boldedNumbers has-success" ></div>
						<label>OKCoin</label>
					    <div id="OKCoin-value"class="form-control boldedNumbers" ></div>
					  </div>
					  <div class="form-group col-md-3">
					    <label>Chilebit</label>
					    <div id="ChileBit-value"class="form-control boldedNumbers" placeholder="Password"></div>
					    <label>SurBTC</label>
					    <div id="BTC-value"class="form-control boldedNumbers" placeholder="Password"></div>
					  </div>
					  <div class="form-group col-md-3">
					    <label>CLP</label>
					    <input type="number" name="amount-CLP" class="form-control" name="CLP-Ammout" placeholder="Enter Amount">
					    <div id="CLP-submit" class="btn btn-default btn-margin-fix">CLP Exchange</div>
					  </div>
					</div>
					<input id="currency-input-hidden" type="hidden" name="currency" value="none">
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