<?php
    $ret = array('status' => 0, 'msg' => '');
    $servername = "localhost";
    $username = $_POST['user'];
    $password = $_POST['passwd'];
    $db = $_POST['db'];
    $conn = new mysqli($servername, $username, $password, $db);

    $sql = "SHOW TABLES";
    $tableList = array();
    $res = $conn->query($sql);        
    while($row = mysqli_fetch_row($res))
    {
        $tableList[] = $row[0];
    }
   $ret['data'] = $tableList;
    

    $conn->close();
    echo json_encode($ret);  // ajax return value
?>