<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title></title>
  <link rel="stylesheet" href="">
</head>
<body>
Hola
<?php


$con = mysql_connect("localhost","web","ohana_psw");
if (!$con)
  {
  echo "conn failed";
  exit;
  }
 

$sql = 'SELECT * from moh_scales.test';

$result = mysql_query($sql, $con);
/*
if (!$result) {
    echo "error"
    exit;
}

while ($fila = mysql_fetch_assoc($result)) {
    echo $fila['data'];
}


/*
$conn->close();
 
 /*
if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
  
  
 
mysql_close($con)



require 'vendor/autoload.php';

header("refresh: 60;");
 
use Parse\ParseClient;
use Parse\ParseObject;
use Parse\ParseQuery;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');


$query = new ParseQuery("TestScale");


$query->exists("data");
$query->descending("updatedAt");

$results = $query->find();

for ($i = 0; $i < count($results); $i++) {
  $object = $results[$i];
  if ($object->get("data")!=null) {
    # code...
    
    #echo $object->getObjectId() . ' - ' . $object->get('data') . ' - ';
    #echo "<br>";
    
  }
  
}




<script src="//www.parsecdn.com/js/parse-1.6.14.min.js"></script>
<script type="text/javascript" charset="utf-8" async defer>
  
  Parse.initialize("Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G", "5z9QFpnWx09U1aznCU5z38KRa53tFufHiGAXZwVO");
  var TestScale = Parse.Object.extend("TestScale");
  var query = new Parse.Query(TestScale);
  query.exists("data");
  query.descending("createdAt");
  query.find({
      success: function(results) {
      var content="//<br>";
      // Do something with the returned Parse.Object values
      for (var i = 0; i < results.length; i++) {
          var object = results[i];
          var date=object.createdAt;
          console.log(date.toString());
          var d=date.toString();
          content=content+object.id + ' - ' + object.get('data') + ' - '+ d + '<br>';
          console.log(date);

      }
      document.getElementsByTagName('list')[0].innerHTML=content;
  },
  error: function(error) {
    
  }
});
</script>
*/
?>
</body>
</html>
