<?php
require_once "nusoap.php";
require_once "phplot.php";
$servis1 = new nusoap_client("http://10.30.2.26/service.php?wsdl", true);
$servis2 = new nusoap_client("http://10.30.2.30/mysql.php?wsdl", true);
$servis3 = new nusoap_client("http://10.30.2.31/graph.php?wsdl", true);

$error1 = $servis1->getError();
if ($error1) {
	echo "Constructor error: " . $error1 . "\n";
}

$result = $servis1->call("checkService", array("mean" => rand(0,4), "stdev" => rand(1,15)/10));

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

$error2 = $servis2->getError();
if ($error2) {
	echo "Constructor error: " . $error2 . "\n";
}


$result2 = $servis2->call("checkService", array("para" => $result));

if ($servis2->fault) {
	echo "Fault: ";
	print_r($result2);
} else {
	$error2 = $servis2->getError();
	if ($error2) {
	echo "Error: " . $error2 . "\n";
	} else {
		//echo "Status zapisa: " .  $result2 . ". \n";
	}
}

$result3 = $servis3->call("checkService", array("polje" => $result));

if ($servis3->fault) {
        echo "Fault: ";
        print_r($result3);
} else {
        $error3 = $servis3->getError();
        if ($error3) {
        echo "Error: " . $error3 . "\n";
        } else {
                //echo $result3 ;
        }
}

$mean = $result[0];
$stdev = $result[1];
$rez = array_slice($result, 2);
$x=0;

$data = array();
for($i = -2+$mean; $i<=2+$mean;$i+=0.1){
	$row = array('',$i);
	$row[]=$rez[$x];
	$data[]=$row;
	$x++;
}

$p = new PHPlot(800, 600);
$p->SetTitle("Normal Distribution :: Mean= " . $mean . " && StDev=  " . $stdev);
$p->SetDataType('data-data');
$p->SetDataValues($data);
$p->SetYTickIncrement(0.1);
$p->SetDrawXGrid(True);
$p->SetDrawYGrid(True);
$p->SetPlotType('lines');
$p->DrawGraph();
