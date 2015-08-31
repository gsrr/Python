<?php
        $hd = popen("python ./hello.py","r");
        print fread($hd,1024);
        pclose($hd);
?>