<html>
    <head>
        <script>
         function contentTable()
         {
            var data = {
                    "user":$("#user").val(),
                    "passwd":$("#passwd").val(),
                    "db":$("#db").val(),
                };
            data = $(this).serialize() + "&" + $.param(data);
            $.ajax({
                type: "POST",
                dataType: "json",
                url: "getTables.php", //Relative or absolute path to response.php file
                data: data,
                success: function(ret) {
                   tables = ret['data'];
                   $("#classTable > tbody").empty();
                   for( i = 0 ; i < tables.length ; i++)
                   {
                        console.log(tables[i]);
                        $("#classTable > tbody").append("<tr><td>" + (i+1) + "</td><td>subjects</td><td>" + tables[i] + "</td></tr>");
                        
                   }
                   
                   
                },
                error: function(data) {
                   alert("bbbbbb, error");
                }
                
            });
         }
         
         $("document").ready(function(){
            //$("button").button();
            var table = $('#classTable').DataTable();
            $('#classTable tbody').on( 'click', 'tr', function () {
                if ( $(this).hasClass('selected') ) {
                    $(this).removeClass('selected');
                }
                else {
                    table.$('tr.selected').removeClass('selected');
                    $(this).addClass('selected');
                }
            } );
            $('#contentTable').click(contentTable);
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
                <td><button id="selectDB" style="width:100%">show db</button></td>
                <td>
                    <select name="menu" id="db_menu" style="min-width:200px;">
                    </select>
                </td>
            </tr>
            <tr>
                <td><button id="selectTable" style="width:100%">show table</button></td>
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
        <table id="classTable"  class="display" cellspacing="0" width="100%">
            <thead>
            <tr>
                <th>Index</th>
                <th>Id</th>
                <th>Label</th>
                <th>Location</th>
            </tr>
            <tbody>
            </tbody>
            <tfoot>
            <tr>
                <th>Index</th>
                <th>Id</th>
                <th>Label</th>
                <th>Location</th>
            </tr>
        </tfoot>
        </thead>
        </table>
    </doby>
</html>