<DOCTYPE html>
<html>
<body>

<script>
  function startProcess()
  {
        $( "#file_submit" ).trigger( "click" );
        alert("aaa");
  }
    
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
            "Delete": function() {},
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
    $("#myform").submit(function(){
        alert("submit");
        var data = {
            "action": "uploadFile",
            "user" : $("#user").val(),
            "password" : $("#passwd").val(),
            "db" : $("#db").val(),
            "tableName" : $("#tableName").val(),
        };
        data = $(this).serialize() + "&" + $.param(data);
        console.log(data);
        alert(data);
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "write.php", //Relative or absolute path to response.php file
            data: data,
            success: function(data) {
                console.log(data);
                alert("Form submitted successfully.\nReturned json: " + data["json"]);
            },
            error: function(xhr) {
                            alert('Ajax request error');
            },
        });
        return true;
    });
    $( "#selectTable" ).click(tableDiag);
  });
</script>

<table>
        <tr>
            <td >User name:</td>
            <td><input id="user" type="text" size="20" value="root"></td>
        </tr>
        <tr>
            <td >Password:</td>
            <td><input id="passwd" type="text" size="20" value="root0119"></td>
        </tr>
        <tr>
            <td >DB:</td>
            <td><input id="db" type="text" size="20" disabled="disabled" value="subjects"></td>
        </tr>
        <tr>
            <td><button id="selectTable" >Select a table</button></td>
            <td><input type="text" size="20" disabled="disabled" id="tableName"></td>
        </tr>
</table>

<br/>
<form id="myform" action="upload.php" method="post" enctype="multipart/form-data">
    Select file to upload:
    <input type="file" name="fileToUpload[]" id="fileToUpload" multiple></br></br>
    Save Location<input name="dir_path" value="D:\My Documents\Desktop\code_test\uploads\" type="text" size="35"></br>
    <input id="file_submit" type="submit" name="submit" value="Submit form" style="display:none"/></br>  
    </br>    
    
</form>


</body>
</html>