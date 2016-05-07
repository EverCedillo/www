<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$path = $_POST["file"];
$pic = $_POST["pic"];

base64_to_jpeg($pic,$path);



function base64_to_jpeg( $base64_string, $output_file ) {
    $ifp = fopen( "profile/pictures/".$output_file.".png", "wb" );
    if($ifp==false) {
    	echo "Fail";
    }else{
	    fwrite( $ifp, base64_decode( $base64_string) ); 
	    fclose( $ifp ); 
	}
    return( $output_file ); 
}

?>