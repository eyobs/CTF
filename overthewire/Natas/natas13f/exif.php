<?php
    // phpinfo();

    // if (function_exists('exif_imagetype')) {
    //     echo "This function is installed";
    // } else {
    //     echo "It is not";
    // }

    $d=exif_imagetype('img.jpg');
    echo $d;
?>
