<?php
    $filename = "tmp_info";
    $file = fopen( $filename, "w" );
    fwrite( $file,  "user=".$_POST['user'] . "\n");
    fwrite( $file,  "password=".$_POST['password'] . "\n");
    fwrite( $file,  "db=".$_POST['db'] . "\n");
    fwrite( $file,  "table=".$_POST['tableName'] . "\n");
    fclose( $file );
?>