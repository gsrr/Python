<html>
    <head>
        <script>
         function outputToFile()
         {
            alert("output to file");
            var csvContent = "data:text/csv;charset=utf-8,";
            
            $(".addRow").each(function(){
                $(this).find('td').each (function() {
                  //var text = $(this).html().replace(/,/g, ";")
                  csvContent += $(this).html();
                  csvContent += ";";
                });
                csvContent += "\r\n";
            });
            var encodedUri = encodeURI(csvContent);
            window.open(encodedUri);
            //$("#download").attr("href", encodedUri);
         }
         function SearchTable()
         {
            var paras = {
                "prog": "mySql",
                "op": "showItems",
                "user":$("#user").val(),
                "password":$("#passwd").val(),
                "db" : $("#db_menu option:selected").val(),
                "table" : $("#table_menu option:selected").val(),
                "condition" : escape($("#condition").val()),
            };

            callPython(paras, function(ret) {
               var dataSet = jQuery.parseJSON(ret['data']);
               $('#classTable_wrapper').remove();
                $('#tableArea').append('<table id="classTable"  class="display" cellspacing="0" style="width:100%"></table>');
                console.log(dataSet);
                  
                 $('#classTable').DataTable( {
                    select: true,
                    "paging": false,
                    data: dataSet,
                    columns: [
                        { title: "Id" },
                        { title: "Label" },
                        { title: "Path" },
                    ]
                });
                $('#classTable tbody').on( 'click', 'tr', function () {
                    $(this).toggleClass('selected');
                } );
                $('#classTable tbody tr').addClass( "addRow" );
                $('#add').click( function () {
                    $(".selected").css('color', 'black');
                    $( ".selected" ).addClass( "addRow" );
                    
                } );
                 $('#remove').click( function () {
                    $(".selected").css('color', 'red');
                    $( ".selected" ).removeClass( "addRow" );
                } );
                $('#output').click( function () {
                    outputToFile();
                });

            });
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
         $("document").ready(function(){
            //$("button").button();
            
            $('#showDb').click(showDb);
            $("#db_menu").change(showTable);
            $('#showTable').click(showTable);
            $('#Search').click(SearchTable);
         });
        </script>
    </head>
    <body>
        
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
    </table>
        <br/>
        <span style="font-size: 20px;color: rgb(0,0,255);">Label input condition: </span><br/>
        <span/>
        <input id="condition" type="text" size="50">
        <button id="Search"> Search</button>
        <br/>
        <br/>
        <button id="add" style="width:100px">add</button>
        <button id="remove" style="width:100px">remove</button>
        <button id="output" style="width:100px">output</button>
        <!-- <a id="download" download='FileName' href='your_url'>download</a> -->
        <div id="tableArea">
        <table id="classTable"  class="display" cellspacing="0" style="width:100%">
        </table>
        </div>
        
    </doby>
</html>