<?php
require_once "nusoap.php";
require_once "phplot.php";

function checkService($polje) {
        return drawGraph($polje);
}

function drawGraph($polje) {
	$mean = $polje[0];
	$stdev = $polje[1];
	$rez = array_slice($polje, 2);
	$x=0;

	$data = array();
	for($i = -2+$mean; $i<=2+$mean;$i+=0.1){
        	$row = array('',$i);
	        $row[]=$rez[$x];
        	$data[]=$row;
        	$x++;
	}

	$img_file= "slike/test" . date("H-i-s") . "-" . rand(100,999) .".png";
	$p = new PHPlot(800, 600);

	$p->SetOutputfile($img_file);
	$p->SetFileFormat("png");
	$p->SetPrintImage(0);
	$p->SetIsInline("1");

	$p->SetTitle("Normal Distribution :: Mean= " . $mean . " && StDev=  " . $stdev);
	$p->SetDataType('data-data');
	$p->SetDataValues($data);
	$p->SetYTickIncrement(0.1);
	$p->SetDrawXGrid(True);
	$p->SetDrawYGrid(True);
	$p->SetPlotType('lines');
	$p->DrawGraph();
	$p->PrintImage();
	chmod($img_file, 777);
	return $img_file;
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
