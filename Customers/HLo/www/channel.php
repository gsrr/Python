<?php
    $ret = array('status' => 0, 'msg' => '');
    $filename = "paras";
    $file = fopen( $filename, "w" );
    foreach ($_POST as $key => &$val) 
    {
        fwrite( $file,  $key . "=" . $_POST[$key] . "\n");
    }
    fclose( $file );
    
    $cmd = 'C:\\Python27\\python.exe python\\' . $_POST['prog'] . '.py';
    $hd = popen($cmd , "r");
    $data = fread($hd, 10240);
    pclose($hd);
    $ret['cmd'] = $cmd;
    $ret['data'] = $data;
    echo json_encode($ret);
?>