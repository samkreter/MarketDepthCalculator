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

				

		  		<div role="tabpanel">
				  <!-- Nav tabs -->
				  <ul class="nav nav-tabs" role="tablist">
				    <li role="presentation" class="active"><a href="#RMB-CLP" aria-controls="RMB-CLP" role="tab" data-toggle="tab">RMB - CLP</a></li>
				    <li role="presentation"><a href="#RMB-BRL" aria-controls="RMB-BRL" role="tab" data-toggle="tab">RMB - BRL</a></li>
				    <li role="presentation"><a href="#RMB-VEF" aria-controls="RMB-VEF" role="tab" data-toggle="tab">RMB - VEF</a></li>
				    <li role="presentation"><a href="#CLP-VEF" aria-controls="CLP-VEF" role="tab" data-toggle="tab">CLP - VEF</a></li>
				    <li role="presentation"><a href="#CLP-BRL" aria-controls="CLP-BRL" role="tab" data-toggle="tab">CLP - BRL</a></li>
				    <li role="presentation"><a href="#BRL-VEF" aria-controls="BRL-VEF" role="tab" data-toggle="tab">BRL - VEF</a></li>
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
								  <div id="first-exchange-blockRMB-CLP" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaRMB-CLP-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinRMB-CLP-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div id="second-exchange-blockRMB-CLP"class="form-group col-md-3">
								    <label>Chilebit</label>
								    <div id="ChileBitRMB-CLP-value"class="form-control boldedNumbers"></div>
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

								  <div id="first-exchange-blockCLP-RMB"class="form-group col-md-3">
								    <label>Chilebit</label>
								    <div id="ChileBitCLP-RMB-value"class="form-control boldedNumbers"></div>
								    <label>SurBTC</label>
								    <div id="BTC-value"class="form-control boldedNumbers" ></div>
								  </div>

								  <div id="second-exchange-blockCLP-RMB" class="form-group col-md-3">
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
								  <div id="first-exchange-blockRMB-BRL" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaRMB-BRL-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinRMB-BRL-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div id="second-exchange-blockRMB-BRL"class="form-group col-md-3">
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

								  <div id="first-exchange-blockBRL-RMB" class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitBRL-RMB-value"class="form-control boldedNumbers"></div>
								  </div>

								  <div id="second-exchange-blockBRL-RMB" class="form-group col-md-3">
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

					<!-- ########################################################## -->


				    <!-- RMB to VEF -->
				    <div role="tabpanel" class="tab-pane" id="RMB-VEF">
				    	<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>RMB</label>
								    <input type="number" name="amount-RMB-VEF" class="form-control">
								    <button class="btn btn-default btn-margin-fix">RMB Exchange</button>
								  </div>
								  <div id="first-exchange-blockRMB-VEF" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaRMB-VEF-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinRMB-VEF-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div id="second-exchange-blockRMB-VEF" class="form-group col-md-3">
								    <label>SurBitCoin</label>
								    <div id="SurBitCoinRMB-VEF-value"class="form-control boldedNumbers"></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>VEF</label>
								    <div id="RMB-VEF-Result" type="number" class="form-control boldedNumbers" ></div>
								  </div>
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="RMB-VEF">
						</form>


						<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>VEF</label>
								    <input type="number" name="amount-VEF-RMB" class="form-control" class="btn btn-default btn-margin-fix">
								    <button class="btn btn-default btn-margin-fix">VEF Exchange</button>
								  </div>

								  <div id="first-exchange-blockVEF-RMB" class="form-group col-md-3">
								    <label>SurBitCoin</label>
								    <div id="SurBitCoinVEF-RMB-value"class="form-control boldedNumbers"></div>
								  </div>

								  <div id="second-exchange-blockVEF-RMB" class="form-group col-md-3">
								    <label>BTCChina</label>
								    <div id="BTCChinaVEF-RMB-value"class="form-control boldedNumbers has-success" ></div>
									<label>OKCoin</label>
								    <div id="OKCoinVEF-RMB-value"class="form-control boldedNumbers" ></div>
								  </div>

								  <div class="form-group col-md-3">
								    <label>RMB</label>
								    <div id="VEF-RMB-Result" type="number" class="form-control boldedNumbers"></div>
								  </div>
								  
								  
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="VEF-RMB">
						</form>
					</div>

			<!-- ########################################################## -->


				    <!-- CLP VEF -->
				    <div role="tabpanel" class="tab-pane" id="CLP-VEF">
				    	<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>CLP</label>
								    <input type="number" name="amount-CLP-VEF" class="form-control">
								    <button class="btn btn-default btn-margin-fix">CLP Exchange</button>
								  </div>
								  <div id="first-exchange-blockCLP-VEF" class="form-group col-md-3">
								    <label>ChileBit</label>
								    <div id="ChileBitCLP-VEF-value"class="form-control boldedNumbers has-success" ></div>
									<label>SurBit</label>
								    <div id="SurBitCLP-VEF-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div id="second-exchange-blockCLP-VEF" class="form-group col-md-3">
								    <label>SurBitCoin</label>
								    <div id="SurBitCoinCLP-VEF-value"class="form-control boldedNumbers"></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>VEF</label>
								    <div id="CLP-VEF-Result" type="number" class="form-control boldedNumbers" ></div>
								  </div>
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="CLP-VEF">
						</form>


						<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>VEF</label>
								    <input type="number" name="amount-VEF-CLP" class="form-control" class="btn btn-default btn-margin-fix">
								    <button class="btn btn-default btn-margin-fix">VEF Exchange</button>
								  </div>

								  <div id="first-exchange-blockVEF-CLP"class="form-group col-md-3">
								    <label>SurBitCoin</label>
								    <div id="SurBitCoinVEF-CLP-value"class="form-control boldedNumbers"></div>
								  </div>

								  <div id="second-exchange-blockVEF-CLP" class="form-group col-md-3">
								    <label>ChileBit</label>
								    <div id="ChileBitVEF-CLP-value"class="form-control boldedNumbers has-success" ></div>
									<label>SurBit</label>
								    <div id="SurBitVEF-CLP-value"class="form-control boldedNumbers" ></div>
								  </div>

								  <div class="form-group col-md-3">
								    <label>CLP</label>
								    <div id="VEF-CLP-Result" type="number" class="form-control boldedNumbers"></div>
								  </div>
								  
								  
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="VEF-CLP">
						</form>
					</div>

			<!-- ########################################################## -->


				    <!-- CLP to BRL -->
				    <div role="tabpanel" class="tab-pane" id="CLP-BRL">
				    	<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>CLP</label>
								    <input type="number" name="amount-CLP-BRL" class="form-control">
								    <button class="btn btn-default btn-margin-fix">CLP Exchange</button>
								  </div>
								  <div id="first-exchange-blockCLP-BRL" class="form-group col-md-3">
								    <label>ChileBit</label>
								    <div id="ChileBitCLP-BRL-value"class="form-control boldedNumbers has-success" ></div>
									<label>SurBit</label>
								    <div id="SurBitCLP-BRL-value"class="form-control boldedNumbers" ></div>
								  </div>
								  <div id="second-exchange-blockCLP-BRL" class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitCLP-BRL-value"class="form-control boldedNumbers"></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>BRL</label>
								    <div id="CLP-BRL-Result" type="number" class="form-control boldedNumbers" ></div>
								  </div>
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="CLP-BRL">
						</form>


						<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>BRL</label>
								    <input type="number" name="amount-BRL-CLP" class="form-control" class="btn btn-default btn-margin-fix">
								    <button class="btn btn-default btn-margin-fix">BRL Exchange</button>
								  </div>

								  <div id="first-exchange-blockBRL-CLP"class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitBRL-CLP-value"class="form-control boldedNumbers"></div>
								  </div>

								  <div id="second-exchange-blockBRL-CLP"class="form-group col-md-3">
								    <label>ChileBit</label>
								    <div id="ChileBitBRL-CLP-value"class="form-control boldedNumbers has-success" ></div>
									<label>SurBit</label>
								    <div id="SurBitBRL-CLP-value"class="form-control boldedNumbers" ></div>
								  </div>

								  <div class="form-group col-md-3">
								    <label>CLP</label>
								    <div id="BRL-CLP-Result" type="number" class="form-control boldedNumbers"></div>
								  </div>
								  
								  
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="BRL-CLP">
						</form>
					</div>



							<!-- ########################################################## -->


				    <!-- BRL to VEF -->
				    <div role="tabpanel" class="tab-pane" id="BRL-VEF">
				    	<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>BRL</label>
								    <input type="number" name="amount-BRL-VEF" class="form-control">
								    <button class="btn btn-default btn-margin-fix">BRL Exchange</button>
								  </div>
								  <div id="first-exchange-blockBRL-VEF"class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitBRL-VEF-value"class="form-control boldedNumbers has-success" ></div>
								  </div>
								  <div id="second-exchange-blockBRL-VEF"class="form-group col-md-3">
								    <label>SurBitCoin</label>
								    <div id="SurBitCoinBRL-VEF-value"class="form-control boldedNumbers"></div>
								  </div>
								  <div class="form-group col-md-3">
								    <label>VEF</label>
								    <div id="BRL-VEF-Result" type="number" class="form-control boldedNumbers" ></div>
								  </div>
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="BRL-VEF">
						</form>


						<form role="form">
							  <div class="row">
								  <div class="form-group col-md-3">
								    <label>VEF</label>
								    <input type="number" name="amount-VEF-BRL" class="form-control" class="btn btn-default btn-margin-fix">
								    <button class="btn btn-default btn-margin-fix">VEF Exchange</button>
								  </div>

								  <div id="first-exchange-blockVEF-BRL"class="form-group col-md-3">
								    <label>SurBitCoin</label>
								    <div id="SurBitCoinVEF-BRL-value"class="form-control boldedNumbers"></div>
								  </div>

								  <div id="second-exchange-blockVEF-BRL"class="form-group col-md-3">
								    <label>FoxBit</label>
								    <div id="FoxBitVEF-BRL-value"class="form-control boldedNumbers has-success" ></div>
								  </div>

								  <div class="form-group col-md-3">
								    <label>BRL</label>
								    <div id="VEF-BRL-Result" type="number" class="form-control boldedNumbers"></div>
								  </div>
								  
								  
								</div>
								<input id="currency-input-hidden" type="hidden" name="currency" value="VEF-BRL">
						</form>
					</div>


			</div> <!-- last tabs div -->


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="jquery-2.1.3.min.js"type="text/javascript"></script>
    <!-- // <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script> -->
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="bootstrap/js/bootstrap.min.js"></script>

    <script src="main.js"type="text/javascript"></script>
  </body>
</html>