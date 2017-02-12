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
  	debug_to_console(mysql_error())
  die('Error: ' . mysql_error());
  }
	debug_to_console("added");
  
 
mysql_close($con)

debug_to_console($_GET[data])
echo $_GET[data];

function debug_to_console( $data ) {

    if ( is_array( $data ) )
        $output = "<script>console.log( 'Debug Objects: " . implode( ',', $data) . "' );</script>";
    else
        $output = "<script>console.log( 'Debug Objects: " . $data . "' );</script>";

    echo $output;
}
?>
