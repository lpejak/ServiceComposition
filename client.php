<?php
require_once "nusoap.php";

//$serviceIP = array();
//$lines = file("serviceIP.txt");
//foreach ($lines as $line_num => $line) {
//        array_push($serviceIP, substr($line,0, strlen($line)-1));
//}

//$stdev = $_GET["stdev"];
//$mean = $_GET["mean"];

$mean = rand(-5,5);
$stdev = rand(1,15)/10;

$servis1 = new nusoap_client("http://10.30.2.67/service.php?wsdl", true);

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

if ($servis1->fault) {
	echo "Fault: ";
	print_r($result);
} else {
	$error1 = $servis1->getError();
	if ($error1) {
		echo "Error: " . $error1 . "\n";
	} else {
		echo $result;
		//echo "<img src=http://10.30.2.65/" . $result ." /img>";
		//echo "\n";
	}
}
$time_end = microtime_float();
$time_all = $time_end - $time_start;

echo "\n Total time: " .$time_all . ";";
