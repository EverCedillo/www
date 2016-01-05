<?php

require 'vendor/autoload.php';
 
use Parse\ParseClient;
 
ParseClient::initialize('Gjy7cLCCl7HcIsLS6myQDIxUvYSdz2ZCVNGHpd8G', 'dtMnemfa8ZLomhY6ngmcEC3MQeFwao0z3HBlbKor', 'ONl2Nnb4QAfcFIZNOXrzgMeyzBnuhio63TIjqMWV');

$holi=$_GET["string"];
	$data = '[{  
      "title":"León",
      "data":"El león (Panthera leo) es un mamífero carnívoro ...",
      "foot":"-leon-"
   },
   {  
      "title":"Elefante",
      "data":"Los elefantes o elefu00e1ntidos (Elephantidae) son ...",
      "foot":"elefante"
   },
   {  
      "title":"Cocodrilo",
      "data":"Los crocodu00edlidos (Crocodylidae) son una familia de sauru00f3psidos ...",
      "foot":"cocodrilo"
   },
   {  
      "title":"Cocodrilo",
      "data":"Los crocodu00edlidos (Crocodylidae) son una familia de sauru00f3psidos ...",
      "foot":"cocodrilo"
   }
]';

header('Content-Type: application/json');
echo $data;
echo $holi;

use Parse\ParseObject;
 
$testObject = ParseObject::create("TestScale");
$testObject->set("test", $holi);
$testObject->save();

echo $testObject;
?>
