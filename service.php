<?php
require_once "nusoap.php";

$line = fgets(fopen("serviceIP.txt", 'r'));

function calcService($mean, $stdev) {
	$time_start = microtime_float();
	$result = normalDistribution($mean, $stdev);
	$time_end = microtime_float();
	$time_1 = $time_end - $time_start;
	$servis2 = new nusoap_client("http://" . substr($line, 0, strlen($line)-1) .  "/mysql.php?wsdl", true);
	$result2 = $servis2->call("databaseService", array("para" => $result));
	return $result2 . ";" . $time_1;
}

function microtime_float()
{
    list($usec, $sec) = explode(" ", microtime());
    return ((float)$usec + (float)$sec);
}

function normalDistribution($mean, $stdev) {
	$pre = 1/($stdev*sqrt(2*pi()));
	$ukupno = array();
	$ukupno[] = $mean;
	$ukupno[] = $stdev;
	for ($i = -2+$mean; $i <= 2+$mean; $i+=0.1) {
		$ukupno[] = $pre * exp(-pow($i-$mean,2)/(2*pow($stdev,2)));
	}
	return $ukupno;
}

$server = new soap_server();
$server->configureWSDL("status", "urn:status");

$server->wsdl->addComplexType(
	"floatArray",
        "complexType",
        "array",
        "",
        "SOAP-ENC:Array",
        array(),
	array(array("ref"=>"SOAP-ENC:arrayType","wsdl:arrayType"=>"xsd:string[]")),
        "xsd:string");

$server->register("calcService",
    array("mean" => "xsd:float", "stdev" => "xsd:float"),
    array("return" => "xsd:string"),
    "urn:status",
    "urn:status#calcService",
    "rpc",
    "encoded",
    "Check if service is working by passing your name");

$server->service($HTTP_RAW_POST_DATA);
