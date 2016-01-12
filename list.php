<list></list>
<?php
require 'vendor/autoload.php';

header("refresh: 10;");
 
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
  	
  	echo $object->getObjectId() . ' - ' . $object->get('data') . ' - ';
  	echo "<br>";
  	
  }
  
}


?>

<script src="//www.parsecdn.com/js/parse-1.6.14.min.js"></script>
<script type="text/javascript" charset="utf-8" async defer>
	
	Parse.initialize("Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G", "5z9QFpnWx09U1aznCU5z38KRa53tFufHiGAXZwVO");
	var TestScale = Parse.Object.extend("TestScale");
	var query = new Parse.Query(TestScale);
	query.exists("data");
	query.find({
  		success: function(results) {
    	var content="//<br>";
    	// Do something with the returned Parse.Object values
    	for (var i = 0; i < results.length; i++) {
      		var object = results[i];
      		var date=object.createdAt;
      		console.log(date.toString());
      		content=content+object.id + ' - ' + object.get('data') + ' - ' + '<br>';
      		console.log(date);

    	}
    	document.getElementsByTagName('list')[0].innerHTML=content;
  },
  error: function(error) {
    
  }
});
</script>

