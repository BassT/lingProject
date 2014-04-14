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
      <div class="col-md-12">
        %if error is not None:
          <div class="panel panel-danger">
            <div class="panel-heading">
              <h3 class="panel-title">Error:</h3>
            </div>
            <div class="panel-body">
              {{ error }}
            </div>
          </div>
        %end
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">SPARQL query</h3>
          </div>
          <div class="panel-body">
            %if query is not None:
              {{ query }}
            %else:
              No query
            %end
          </div>
        </div> 
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">Results</h3>
          </div>
          <div class="panel-body">
            %try:
            <table class="table">
              %for result in results["results"]["bindings"]:
                <tr class="active"><td>{{ result[target]["value"] }}</td></tr>
              %end
            </table>
            %except:
              No results
            %end
          </div>
        </div> 
      </div>
    </div>
  </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
</body>
</html>