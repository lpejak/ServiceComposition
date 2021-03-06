<?php
require_once "nusoap.php";

function databaseService($para){
        $line = fgets(fopen("serviceIP.txt", 'r'));
        zapisArray($para);
        $servis3 = new nusoap_client("http://" . substr($line, 0, strlen($line)-1) . "/graph.php?wsdl", true);
        $time_start = microtime_float();
        $result3 = $servis3->call("graphService", array("polje" => $para));
        $time_end = microtime_float();
        $time_3 = $time_end - $time_start;
        return $result3 . ";". $time_3;
}

function microtime_float()
{
    list($usec, $sec) = explode(" ", microtime());
    return ((float)$usec + (float)$sec);
}

function zapisArray($para){

        $conn = new mysqli("localhost", "root", "grad");
        $sql = "CREATE DATABASE IF NOT EXISTS baza";
        $conn->query($sql);
        $conn = new mysqli("localhost", "root", "grad", "baza");
        $sql = "CREATE TABLE IF NOT EXISTS test(id INT AUTO_INCREMENT PRIMARY KEY,mean FLOAT, stdev FLOAT, broj FLOAT, date TIMESTAMP)";
        $conn->query($sql);
//      foreach(array_slice($para, 2) as $p){
//              $sql = "INSERT INTO test (mean, stdev, broj) VALUES (". $para[0] .", " . $para[1] . ", " . $p  . ")";
//              $conn->query($sql);
//      }

        $sql = "INSERT INTO test (mean, stdev, broj) VALUES (". $para[0] .", " . $para[1] . ", " . $para[22] . ")";
        $conn->query($sql);
        $conn->close();
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

$server->register("databaseService",
    array("para" => "tns:randArray"),
    array("return" => "xsd:string"),
    "urn:status",
    "urn:status#databaseService",
    "rpc",
    "encoded",
    "Check if service is working by passing your name");

$server->service($HTTP_RAW_POST_DATA);

