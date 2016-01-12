<?php
require 'vendor/autoload.php';

header("refresh: 10;");
 
use Parse\ParseClient;
use Parse\ParseObject;
use Parse\ParseQuery;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');


$query = new ParseQuery("TestScale");

try{
$query->exists("data");
$query->descending("updatedAt");

$results = $query->find();

for ($i = 0; $i < count($results); $i++) {
  $object = $results[$i];
  if ($object->get("data")!=null) {
  	# code...
  	
  	echo $object->getObjectId() . ' - ' . $object->get('data') . ' - '. $object->getUpdatedAt();
  	echo "<br>";
  	
  }
  
}}
catch(Exception $error) {
  // $error is an instance of ParseException with details about the error.
  echo $error->getCode();
  echo $error->getMessage();
}


?>