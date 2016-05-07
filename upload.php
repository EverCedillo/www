<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$path = $_POST["file"];
$pic = $_POST["pic"];

echo base64_to_jpeg($pic,$path);

echo $path;


function base64_to_jpeg( $base64_string, $output_file ) {
    $ifp = fopen( "profile/pictures/fil.jpg", "wb" );
    if($ifp==false) {
    	echo "Fallé";
    }else{
	    fwrite( $ifp, base64_decode( $base64_string) ); 
	    fclose( $ifp ); 
	    echo  $base64_string;
	}
    return( $output_file ); 
}

?>