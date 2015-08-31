<?php
    // if (is_ajax()) {
        // if (isset($_POST["action"]) && !empty($_POST["action"])) { 
        // $action = $_POST["action"];
        // switch($action) { 
        // case "test": test_function(); break;
        // }
        // }
        // }

        // function is_ajax() {
        // return isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest';
        // }
        // function test_function(){
        // $return = $_POST;
        // $handle = popen('python hello.py', 'r');
        // $read = fread($handle, 2096);
        // pclose($handle);
        // $return["data"] = $read;
        // $return["json"] = json_encode($return);
        // echo json_encode($return);
    // }
    $command = 'C:\\Python27\\python.exe convert.py';
    $hd = popen($command,"r");
    print fread($hd,1024);
    pclose($hd);
?>