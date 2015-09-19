<?php
function uploadFile($target_dir, $name, $tmp_name, $size, $file)
{
    $ret = array('status' => 0, 'msg' => '');
    $target_file = $target_dir . "\\" . basename($name);
    $uploadOk = 1;
    // Check if file already exists
    if (file_exists($target_file)) 
    {
        $ret['msg'] = "Sorry, file already exists.";
        $uploadOk = 0;
    }
    // Check file size
    if ($size > 500000) 
    {
        $ret['msg'] = "Sorry, your file is too large.";
        $uploadOk = 0;
    }

    if ($uploadOk == 0) 
    {
        $ret['msg'] = "Sorry, your file was not uploaded.";
    } 
    else 
    {
        if (move_uploaded_file($tmp_name, $target_file)) 
        {
            $ret['msg'] = basename( $name). " has been uploaded.<br>" ;
        } 
        else 
        {
            $uploadOk = 0;
            $ret['msg'] = "Sorry, there was an error uploading your file.<br>";
        }
    }
    
    if ($uploadOk == 1) 
    {   
        fwrite( $file, $target_file . "\r\n");
    }
    echo json_encode($ret);
}

$key="fileToUpload";
$target_dir = $dir_path;
$filename = "files";
$file = fopen( $filename, "w" );
for($i=0; $i<count($_FILES[$key]['name']); $i++) 
{
    $name = $_FILES[$key]['name'][$i];
    $tmp_name = $_FILES[$key]['tmp_name'][$i];
    $size = $_FILES["fileToUpload"]["size"][$i];
    uploadFile($target_dir, $name, $tmp_name, $size, $file);
}
fclose( $file );

?>