<?php

require 'vendor/autoload.php';
 
use Parse\ParseClient;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');

$holi=$_GET["data"];

echo $data;
echo $holi;

use Parse\ParseObject;
 
$testObject = ParseObject::create("TestScale");
$testObject->set("data", $holi);
$testObject->save();

echo $testObject;
?>
