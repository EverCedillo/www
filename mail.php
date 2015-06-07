<html>
<body>
 
 
<?php
$con = mysql_connect("localhost","web","ohana_psw");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
 
mysql_select_db("web", $con);
$sql = "INSERT INTO ohana_mailing.TOH001_MAIL_LIST ('NB_MAIL') VALUES ('$_POST[email]')";

 
if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
echo "1 record added";
 
mysql_close($con)
?>
</body>
</html>
