<?php
require_once "nusoap.php";

function checkService($polje) {
        return "Istina \n" . $polje[0] . " " . $polje[1] ;
}

function drawGraph($polje) {
	$graphTxt = "0";
}

$server = new soap_server();
$server->configureWSDL("status", "urn:status");

$server->wsdl->addComplexType(
        "randArray",
        "complexType",
        "array",
        "",
        "SOAP-ENC:Array",
        array(),
        array(array("ref"=>"SOAP-ENC:arrayType","wsdl:arrayType"=>"xsd:string[]")),
        "xsd:string");

$server->register("checkService",
    array("polje" => "tns:randArray"),
    array("return" => "xsd:string"),
    "urn:status",
    "urn:status#checkService",
    "rpc",
    "encoded",
    "Check if service is working by passing your name");

$server->service($HTTP_RAW_POST_DATA);

