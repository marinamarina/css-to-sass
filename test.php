<?php

include 'convert.php';
include 'test_data.php';
include 'expect.php';


	$converter = new CssToSassConverter();
    $converter->convert($testData);
?>
