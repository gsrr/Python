<?php
    $ret = array('status' => 0, 'msg' => '');
    $servername = "localhost";
    $username = $_POST['user'];
    $password = $_POST['passwd'];
    $db = $_POST['db'];
    $table = $_POST['table'];
    $conn = new mysqli($servername, $username, $password);
   
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    $sql="SHOW DATABASES";
    $databases = mysqli_query($conn, $sql);
    
    $db_exist = 0;
    while($row = mysqli_fetch_row($databases))
    {
        //printf ("%s (%s)\n",$row[0],$row[1]);
        if(strtolower($db) == strtolower($row[0]))
        {
            $db_exist = 1; 
        }
    }
    
    if($db_exist == 0)
    {
        $sql = "CREATE DATABASE " . $db;
        if ($conn->query($sql) === TRUE) {
            $ret["msg"] = "Database created successfully";
        } else {
            $ret["status"] = 0;
            $ret["msg"] = "Error creating database: " . $conn->error;
        }
    }
    $conn->close();
    $conn = new mysqli($servername, $username, $password, $db);
    //create data table
    $sql = "CREATE TABLE " . $table . " (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
            label VARCHAR(30) NOT NULL,
            subject VARCHAR(255) NOT NULL,
            short_ans VARCHAR(255),
            detail VARCHAR(255)
    )";
            
    if ($conn->query($sql) === TRUE) 
    {
        $ret["msg"] =  "Table MyGuests created successfully";
    } 
    else 
    {
         $ret["status"] = -2;
    }
    

    $conn->close();
    echo json_encode($ret);  // ajax return value
?>