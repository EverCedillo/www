<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	
	
</head>
<body>

	<?php


$con = mysql_connect("localhost","web","ohana_psw");
if (!$con)
  {
  echo mysql_error();
  exit;
  }

if(!mysql_select_db("moh_scales", $con)){
	echo "failed to find database";
	exit;
}


date_default_timezone_set('America/Mexico_City');
$timestamp = date('Y-m-d G:i:s');




$sql = "INSERT INTO `moh_scales`.`test` (`id`, `data`, `hora`) VALUES (NULL, '$_GET[data]', '$timestamp');";

//$sql = 'select * from moh_scales.test';
 
 


if (!mysql_query($sql,$con))
  {
  	echo "failed to execute";
  	exit;
  }
  
  
 
 


echo $_GET[data]." | ".$timestamp;


?>

</body>
</html>

