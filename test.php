<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	
	
</head>
<body>
HOla
	<?php


$con = mysql_connect("localhost","web","ohana_psw");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

if(!mysql_select_db("moh_scales", $con)){
	echo "failed to find database";
}

/*

$sql = "INSERT INTO `moh_scales`.`test` (`id`, `data`, `hora`) VALUES (NULL, '$_GET[data]', CURRENT_TIMESTAMP);";
 
if (!mysql_query($sql,$con))
  {
  	debug_to_console(mysql_error())
  die('Error: ' . mysql_error());
  }
	debug_to_console("added");
  
 
mysql_close($con)

*/
echo $_GET[data];


?>

</body>
</html>

