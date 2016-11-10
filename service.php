<?php
require_once "nusoap.php";
//$mysql_client = new nusoap_client("http://10.30.2.28/mysql.php?wsdl", true);
//$rez = 123;
//$mysql_client->call("checkService", array("para" => $rez));


function checkService($mean, $stdev) {
	return normalDistribution($mean, $stdev);
}

function normalDistribution($mean, $stdev) {
	$max = $stdev*4;
	$pre = 1/($stdev*sqrt(2*pi()));
	$ukupno = array();
	$ukupno[] = $mean;
	$ukupno[] = $stdev;
	for ($i = -$max; $i <= $max; $i++) {
		$ukupno[] = $pre * exp(-pow($i-$mean,2)/(2*pow($stdev,2)));
	}
	return $ukupno;
}

//$rez = normalDistribution($mean, $stdev);
//$mysql_client->call("checkService", array("para" => $rez));

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
?>
