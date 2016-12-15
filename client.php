<?php
require_once "nusoap.php";

$line = fgets(fopen("serviceIP.txt", 'r'));

//$stdev = $_GET["stdev"];
//$mean = $_GET["mean"];

$mean = rand(-5,5);
$stdev = rand(1,15)/10;

$servis1 = new nusoap_client("http://" . substr($line, 0, strlen($line)-1) . "/service.php?wsdl", true);

function microtime_float()
{
    list($usec, $sec) = explode(" ", microtime());
    return ((float)$usec + (float)$sec);
}


$error1 = $servis1->getError();
if ($error1) {
        echo "Constructor error: " . $error1 . "\n";
}


$time_start = microtime_float();
$result = $servis1->call("calcService", array("mean" => $mean, "stdev" => $stdev));
$time_end = microtime_float();
$time_all = $time_end - $time_start;

if ($servis1->fault) {
        echo "Fault: ";
        print_r($result);
} else {
        $error1 = $servis1->getError();
        if ($error1) {
                echo "Error: " . $error1 . "\n";
        } else {
                //echo $result . '<br>';
                //echo "<img src=http://10.30.2.65/" . $result ." /img>";
                //echo "\n";
        }
}

$temp = explode(";", $result);
//echo "Slika: " . $temp[0] . "<br>";
//echo "Servis3: " . $temp[1] . "<br>";
//echo "Servis2: " . ($temp[2]-$temp[1]) . "<br>";
//echo "Servis1: " . ($time_all-$temp[2]) . "<br>";
//echo "Total time: " .$time_all . ";";
echo $temp[1] . ";" . ($temp[2]-$temp[1]) . ";" . ($time_all-$temp[2]) . ";" . $time_all;
