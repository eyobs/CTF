<?php
session_start();

var_dump($_GET);



// header("Location: /");

if(array_key_exists("revelio", $_GET)) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas23\n";
    print "Password: <censored></pre>";
}
else
    print "booooo";
?>


