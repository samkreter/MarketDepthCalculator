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

		  		<div id="loading-modal"class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="loading-modal" aria-hidden="true">
					<div class="modal-dialog modal-sm">
						<div class="modal-content">
							<span class="loading">LOADING...</span>
						</div>
	 				</div>
				</div>

		  		<div role="tabpanel">
				  <!-- Nav tabs -->
				  <ul class="nav nav-tabs" role="tablist">
				    <li role="presentation" class="active"><a href="#RMB-CLP" aria-controls="RMB-CLP" role="tab" data-toggle="tab">RMB - CLP</a></li>
				    <li role="presentation"><a href="#RMB-BRL" aria-controls="RMB-BRL" role="tab" data-toggle="tab">RMB - BRL</a></li>
				  </ul>


				  <!-- Tab panes -->
				  <div class="tab-content">
				    <div role="tabpanel" class="tab-pane active" id="RMB-CLP">
				    	<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>RMB</label>
								    <input type="number" name="amount-RMB-CLP" class="form-control"  placeholder="Enter Amount">
								    <button type="submit" class="btn btn-default btn-margin-fix">RMB Exchange</button>
								  </div>
								  <div id="China-Exchange-Group" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaRMB-CLP-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinRMB-CLP-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>Chilebit</label>
								    <div id="ChileBitRMB-CLP-value"class="form-control boldedNumbers" placeholder="Password"></div>
								    <label>SurBTC</label>
								    <div id="BTC-value"class="form-control boldedNumbers"></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>CLP</label>
								    <div id="RMB-CLP-Result"type="number"  class="form-control boldedNumbers" ></div>
								  </div>
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="RMB-CLP">
						</form>


						<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>CLP</label>
								    <input type="number"  class="form-control" name="amount-CLP-RMB" placeholder="Enter Amount">
								    <button id="CLP-RMB-submit" class="btn btn-default btn-margin-fix">CLP Exchange</button>
								  </div>

								  <div class="form-group col-md-3">
								    <label>Chilebit</label>
								    <div id="ChileBitCLP-RMB-value"class="form-control boldedNumbers" placeholder="Password"></div>
								    <label>SurBTC</label>
								    <div id="BTC-value"class="form-control boldedNumbers" placeholder="Password"></div>
								  </div>

								  <div id="China-Exchange-Group" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaCLP-RMB-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinCLP-RMB-value"class="form-control boldedNumbers" ></div>
								  </div>

								  <div class="form-group col-md-3">
								    <label>RMB</label>
								    <div id="CLP-RMB-Result" type="number" class="form-control boldedNumbers" ></div>
								  </div>
								  
								  
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="CLP-RMB">
						</form>
				    </div>

<!-- ########################################################## -->


				    <!-- RMB to BRL -->
				    <div role="tabpanel" class="tab-pane" id="RMB-BRL">
				    	<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>RMB</label>
								    <input type="number" name="amount-RMB-BRL" class="form-control">
								    <button class="btn btn-default btn-margin-fix">RMB Exchange</button>
								  </div>
								  <div id="China-Exchange-Group" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaRMB-BRL-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinRMB-BRL-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitRMB-BRL-value"class="form-control boldedNumbers"></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>BRL</label>
								    <div id="RMB-BRL-Result" type="number" class="form-control boldedNumbers" ></div>
								  </div>
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="RMB-BRL">
						</form>


						<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>BRL</label>
								    <input type="number" name="amount-BRL-RMB" class="form-control" class="btn btn-default btn-margin-fix">
								    <button class="btn btn-default btn-margin-fix">BRL Exchange</button>
								  </div>

								  <div class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitBRL-RMB-value"class="form-control boldedNumbers"></div>
								  </div>

								  <div id="China-Exchange-Group" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaBRL-RMB-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinBRL-RMB-value"class="form-control boldedNumbers" ></div>
								  </div>

								  <div class="form-group col-md-3">
								    <label>RMB</label>
								    <div id="BRL-RMB-Result" type="number" class="form-control boldedNumbers"></div>
								  </div>
								  
								  
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="BRL-RMB">
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