<?php
require_once "nusoap.php";

function checkService($mean, $stdev) {
	return normalDistribution($mean, $stdev);
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

$server->register("checkService",
    array("mean" => "xsd:float", "stdev" => "xsd:float"),
    array("return" => "tns:floatArray"),
    "urn:status",
    "urn:status#checkService",
    "rpc",
    "encoded",
    "Check if service is working by passing your name");

$server->service($HTTP_RAW_POST_DATA);
