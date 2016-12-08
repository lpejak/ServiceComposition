<?php
require_once "nusoap.php";

//$stdev = $_GET["stdev"];
//$mean = $_GET["mean"];

$mean = rand(-5,5);
$stdev = rand(1,15)/10;

$servis1 = new nusoap_client("http://10.30.2.26/service.php?wsdl", true);
$servis2 = new nusoap_client("http://10.30.2.30/mysql.php?wsdl", true);
$servis3 = new nusoap_client("http://10.30.2.31/graph.php?wsdl", true);


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
$result = $servis1->call("checkService1", array("mean" => $mean, "stdev" => $stdev));

if ($servis1->fault) {
	echo "Fault: ";
	print_r($result);
} else {
	$error1 = $servis1->getError();
	if ($error1) {
		echo "Error: " . $error1 . "\n";
	} else {
		//echo implode("\n",$result);
		//echo "\n";
	}
}
$time_end = microtime_float();
$time = $time_end - $time_start;

echo $time . ";";

$error2 = $servis2->getError();
if ($error2) {
	echo "Constructor error: " . $error2 . "\n";
}


$time_start = microtime_float();
$result2 = $servis2->call("checkService", array("para" => $result));

if ($servis2->fault) {
	echo "Fault: ";
	print_r($result2);
} else {
	$error2 = $servis2->getError();
	if ($error2) {
	echo "Error: " . $error2 . "\n";
	} else {
	//	echo "Status zapisa: " .  $result2 . ". \n<br />";
	}
}

$time_end = microtime_float();
$time = $time_end - $time_start;

echo $time . ";";


$time_start = microtime_float();
$result3 = $servis3->call("checkService", array("polje" => $result));

if ($servis3->fault) {
        echo "Fault: ";
        print_r($result3);
} else {
        $error3 = $servis3->getError();
        if ($error3) {
        echo "Error: " . $error3 . "\n";
        } else {
               // echo "<img src=http://10.30.2.31/" . $result3 ." /img>";
        }
}

$time_end = microtime_float();
$time = $time_end - $time_start;

echo $time . ";";

