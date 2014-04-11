<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Final project CSE 6339, 2014</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootswatch/3.1.1/slate/bootstrap.min.css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container">
    	<h1>Natural Language Interface for Internet Search Engines</h1>
    	<div class="row">
    		<div class="col-md-12">
    			<p><strong>Example questions:</strong></p>
    			<ul>
    				<li>Which companies are owned by Google?</li>
    			</ul>
    		</div>
    	</div>
    	<div class="row">
    		<div class="col-md-6">
    			<form role="form" action="/result" method="POST">
    				<div class="form-group">
    					<label for="input">What would you like to know?</label>
    					<input type="text" class="form-control" id="input" name="input" placeholder="Enter a question">
    				</div>
    				<button type="submit" class="btn btn-default">Get answer</button>
    			</form>
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