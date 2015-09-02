<DOCTYPE html>
<html>
<body>

<script src="./js/callPython.js"></script>
<script>
  function tableDiag()
  {
    alert("select buttion");
    var url = "./table.php";
    var dia = $( "<div></div>" ).dialog({ 
        autoOpen: false,
        height: 'auto',
        width: 'auto',
        buttons: { 
            "OK": function() {tableOK($(this));},
            "Create": function() {createDB();},
            "Delete": function() {deleteTable();},
        },
        close: function(event, ui) 
        { 
            $(this).dialog('close');
            $(this).dialog('destroy').remove()
        } 
        
    });
    dia.load(url);
    dia.dialog("open");
    return false;  // avoid aubmit action
  }
  
  $("document").ready(function(){
    $( "#selectTable" ).click(tableDiag);
    $('#myform').prop("target", 'my_iframe');
    //document.getElementById('my_form').target = 'my_iframe';
  });
</script>

<table>
        <tr>
            <td >User name:</td>
            <td><input id="user" type="text" size="20" value="root"></td>
        </tr>
        <tr>
            <td >Password:</td>
            <td><input id="passwd" type="password" size="20" value="root0119"></td>
        </tr>
        <tr>
            <td >DB:</td>
            <td><input id="db" type="text" size="20" disabled="disabled" value="subjects"></td>
        </tr>
        <tr>
            <td><button id="selectTable" >Select a table</button></td>
            <td><input type="text" size="20" disabled="disabled" id="tableName" value="q111"></td>
        </tr>
</table>

<br/>
<form id="myform" action="upload.php" method="post" enctype="multipart/form-data">
    Select file to upload:
    <input type="file" name="fileToUpload[]" id="fileToUpload" multiple></br></br>
    Save Location<input name="dir_path" value="D:\My Documents\Desktop\code_test\uploads\" type="text" size="35"></br>
    </br>  
    <input id="file_submit" type="submit" name="submit" value="Upload"/></br>  
    </br>
    <iframe id='my_iframe' name='my_iframe' src="">    
    
</form>


</body>
</html>