<?php


$con = mysql_connect("localhost","web","ohana_psw");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
 
mysql_select_db("web", $con);

$sql = "INSERT INTO `moh_scales`.`test` (`id`, `data`, `hora`) VALUES (NULL, '$_GET[data]', CURRENT_TIMESTAMP);";
 
if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
	echo "1 record added";
  
 
mysql_close($con)

echo $_GET[data];
?>
