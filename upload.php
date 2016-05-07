<?php

$path = $_GET["file"];
$pic = $_GET["pic"];

echo base64_to_jpeg($pic,$path);

echo $path;


function base64_to_jpeg( $base64_string, $output_file ) {
    $ifp = fopen( $output_file, "wb" ); 
    fwrite( $ifp, base64_decode( $base64_string) ); 
    fclose( $ifp ); 
    echo  $base64_string;
    return( $output_file ); 
}

?>