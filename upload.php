<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$path = $_GET["file"];
$pic = $_GET["pic"];

echo base64_to_jpeg($pic,$path);

echo $path;


function base64_to_jpeg( $base64_string, $output_file ) {
    $ifp = fopen( "profile/pictures/fil.png", "wb" );
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

iVBORw0KGgoAAAANSUhEUgAAABwAAAASCAMAAAB/2U7WAAAABlBMVEUAAAD///+l2Z/dAAAASUlEQVR4XqWQUQoAIAxC2/0vXZDrEX4IJTRkb7lobNUStXsB0jIXIAMSsQnWlsV+wULF4Avk9fLq2r8a5HSE35Q3eO2XP1A1wQkZSgETvDtKdQAAAABJRU5ErkJggg==