<?php
require_once "nusoap.php";
$servis1 = new nusoap_client("http://10.30.2.26/service.php?wsdl", true);
$servis2 = new nusoap_client("http://10.30.2.28/mysql.php?wsdl", true);

$error1 = $servis1->getError();
if ($error1) {
	echo "Constructor error: " . $error1 . "\n";
}

$result = $servis1->call("checkService", array("mean" => rand(0,10)/10, "stdev" => rand(1,4)));

if ($servis1->fault) {
	echo "Fault: ";
	print_r($result);
} else {
	$error1 = $servis1->getError();
	if ($error1) {
		echo "Error: " . $error1 . "\n";
	} else {
		echo implode("\n",$result);
		echo "\n";
	}
}

$error2 = $servis2->getError();
if ($error2) {
	echo "Constructor error: " . $error2 . "\n";
}


$result2 = $servis2->call("checkService", array("para" => $result));

if ($servis2->fault) {
	echo "Fault: ";
	print_r($result2);
} else {
	$error1 = $servis2->getError();
	if ($error1) {
	echo "Error: " . $error1 . "\n";
	} else {
		echo "Status zapisa: " .  $result2 . ". \n";
	}
}



