<?php
$key = "h%0Apwd #";

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" payload.txt");
    }
}
?>