<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Natural Language Interface for DBpedia</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootswatch/3.1.1/cerulean/bootstrap.min.css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container">
    	<h1>Natural Language Interface for DBpedia</h1>
            <div class="row">
                <div class="col-md-4">
                    <div class="panel panel-info" style="min-height: 300px;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Domains covered</h3>
                        </div>
                        <div class="panel-body">
                            <ul>
                                <li>Species</li>
                                <li>Hotel</li>
                                <li>University</li>
                                <li>Language</li>
                                <li>Actor</li>
                                <li>Restaurant</li>
                                <li>Company</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-info" style="min-height: 300px;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Hints</h3>
                        </div>
                        <div class="panel-body">
                            When asking question be aware of the following:
                            <ul>
                                <li>Things your asking about are retrieved by their label in DBpedia, so you need to take capitalization into account</li><br/>
                                Example:
                                <ul>
                                    <li>University of Toronto - will be retrieved</li>
                                    <li>university of toronto - won't be retrieved</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-info" style="min-height: 300px;">
                      <div class="panel-heading">
                          <h3 class="panel-title">Example questions:</h3>
                      </div>
                        <div class="panel-body">
                            <ul>
                                <li>Which companies are owned by Google?</li>
                                <li>List all restaurants in London</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
    <div class="jumbotron">
        	<div class="row">
        		<div class="col-md-6">
        			<form role="form" action="/result" method="POST">
        				<div class="form-group">
        					<label for="input">What would you like to know?</label>
        					<input type="text" class="form-control" id="input" name="input" placeholder="Enter a question">
        				</div>
        				<button type="submit" class="btn btn-info">Get answer</button>
        			</form>
        		</div>
        	</div>
    </div>
    	<div class="row">
    		<div class="col-md-6">
    			
    		</div>
    	</div>
    </div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
  </body>
</html>