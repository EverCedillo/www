<?php
require 'vendor/autoload.php';

header("refresh: 10;");
 
use Parse\ParseObject;
use Parse\ParseQuery;
use Parse\ParseACL;
use Parse\ParsePush;
use Parse\ParseUser;
use Parse\ParseInstallation;
use Parse\ParseException;
use Parse\ParseAnalytics;
use Parse\ParseFile;
use Parse\ParseCloud;
use Parse\ParseClient;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');


$query = new ParseQuery("TestScale");


$query->exists("data");
$query->descending("updatedAt");

$results = $query->find();

for ($i = 0; $i < count($results); $i++) {
  $object = $results[$i];
  if ($object->get("data")!=null) {
  	# code...
  	
  	echo $object->getObjectId() . ' - ' . $object->get('data') . ' - ' . $obj->getCreatedAt()->format('Y-m-d H:i:s');
  	echo "<br>";
  	
  }
  
}


?>


