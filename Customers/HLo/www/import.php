<DOCTYPE html>
<html>
<body>

<script src="./js/callPython.js"></script>
<script>
   function createDB()
 {
    var url = "./create.html";
    var dia = $( "<div></div>" ).dialog({ 
        autoOpen: false,
        height: 'auto',
        width: 'auto',
        buttons: { 
            "OK": function() {startCreateDB($(this));},
        },
        close: function(event, ui) 
        { 
            $(this).dialog('close'); 
            $(this).dialog('destroy').remove()
        } 
        
    });
    dia.load(url);
    dia.dialog("open");
    
 }
 function selectAppend(selector , data)
     {
        for (i in data)
        {
            selector.append($('<option>', {
                value: data[i],
                text: data[i],
            }));
        }
     }
  function showDb()
     {
        var data = {
            "prog": "mySql",
            "op": "showDB",
            "user": $("#user").val(),
            "password": $("#passwd").val(),
        };
        callPython(data, function(ret) {
            var data = eval(ret['data']);
            selectAppend($("#db_menu"), data);
            showTable();
        });
     }
     function showTable()
     {
        var data = {
            "prog": "mySql",
            "op": "showTable",
            "user": $("#user").val(),
            "password": $("#passwd").val(),
            "db" : $("#db_menu option:selected").val(),
        };
        callPython(data, function(ret) {
            var data = eval(ret['data']);
            $("#table_menu").empty();
            selectAppend($("#table_menu"), data);
        });
     }
     
     function fileManager()
     {
        var paras = [];
        paras['url'] = "./fileManager/fileManager.html";
        paras['button'] = {};
        $dia = createDialog(paras);
        $dia.dialog("open");
     }
  $("document").ready(function(){
    $('#myform').prop("target", 'my_iframe');
    $('#showDb').click(showDb);
    $('#showTable').click(showTable);
    $("#db_menu").change(showTable);
    $("#create").click(createDB);
    $("#fileManager").click(fileManager);
    //document.getElementById('my_form').target = 'my_iframe';
  });
</script>

<table>
        
        <tr>
            <td >User name:</td>
            <td><input id="user" type="text" size="20" value=""></td>
        </tr>
        <tr>
            <td >Password:</td>
            <td><input id="passwd" type="password" size="20" value=""></td>
        </tr>
        <tr>
            <td><button id="create" style="width:100%">Create DB and Table</button></td>
        </tr>
        <tr>
            <td><button id="showDb" style="width:100%">show db</button></td>
            <td>
                <select name="menu" id="db_menu" style="min-width:200px;">
                </select>
            </td>
        </tr>
        <tr>
            <td><button id="showTable" style="width:100%">show table</button></td>
             <td>
                <select name="menu" id="table_menu" style="min-width:200px;">
                </select>
            </td>
        </tr>
        <tr/>
        <tr>
            <td >Prefix of ID:</td>
            <td><input type="text" size="10" id="id_prefix" value=""></td>
        </tr>
</table>

<br/>
<form id="myform" action="upload.php" method="post" enctype="multipart/form-data">
    Select file to upload:
    <input type="file" name="fileToUpload[]" id="fileToUpload" multiple></br></br>
    Save Location
    <button id="fileManager">Browse</button>
    <input id="dir_path" name="dir_path" value="" type="text" size="50"></br>
    </br>  
    <input id="file_submit" type="submit" name="submit" value="Upload"/></br>  
    </br>
    <iframe id='my_iframe' name='my_iframe' src="" width="500">    
    
</form>


</body>
</html>