<?php
require 'vendor/autoload.php';
 
use Parse\ParseClient;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');


$query = new ParseQuery("TestScale");

$query->exists("data");

foreach ($query as $key) {
	# code...
	echo $key;
	echo "\n";
}


?>