<?php
function uploadFile($target_dir, $name, $tmp_name, $size)
{
    $target_file = $target_dir . basename($name);
    $uploadOk = 1;
    $imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);

    // Check if file already exists
    if (file_exists($target_file)) 
    {
        echo "Sorry, file already exists.";
        $uploadOk = 0;
    }
    // Check file size
    if ($size > 500000) 
    {
        echo "Sorry, your file is too large.";
        $uploadOk = 0;
    }

    if ($uploadOk == 0) 
    {
        echo "Sorry, your file was not uploaded.";
    } 
    else 
    {
        if (move_uploaded_file($tmp_name, $target_file)) 
        {
            echo "The file ". basename( $name). " has been uploaded.<br>" ;
        } 
        else 
        {
            $uploadOk = 0;
            echo "Sorry, there was an error uploading your file.<br>";
        }
    }
    
    if ($uploadOk == 1) 
    {
        //Generate fileID
            //1. read all data from data table
            
        //write information to db
        
        //insert id into docx
            // 1.write fileName fileID into tmp file
        
        $cmd = 'C:\\Python27\\python.exe docApi.py ' . $file_id;
        $hd = popen($cmd , "r");
        $data = fread($hd,1024);
        pclose($hd);
        echo $data;
    }
}
#$target_dir = "C:\\AppServ\\www\\uploads\\";
foreach ($_FILES as $key => &$val) 
{
    echo $key . "<br>";
    for($i=0; $i<count($_FILES[$key]['name']); $i++) 
    {
        echo $_FILES[$key]['name'][$i] . "<br>";
        echo $_FILES[$key]['tmp_name'][$i]. "<br>";
    }
}
$target_dir = $dir_path;

for($i=0; $i<count($_FILES[$key]['name']); $i++) 
{
    $name = $_FILES[$key]['name'][$i];
    $tmp_name = $_FILES[$key]['tmp_name'][$i];
    $size = $_FILES["fileToUpload"]["size"][$i];
    uploadFile($target_dir, $name, $tmp_name, $size);
}

?>