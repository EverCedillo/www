<?php
require 'vendor/autoload.php';
 
use Parse\ParseClient;
use Parse\ParseObject;
use Parse\ParseQuery;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');


$query = new ParseQuery("TestScale");

$query->exists("data");

$results = $query->find();

for ($i = 0; $i < count($results); $i++) {
  $object = $results[$i];
  if ($object->get("data")!=null) {
  	# code...
  	echo $object->getObjectId() . ' - ' . $object->get('data');
  	echo "<br>";
  }
  
}


?>