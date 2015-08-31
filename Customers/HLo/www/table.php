<html>
    <head>
        <script>
         function tableOK(dialog)
         {
            var table_name = $('.selected td:nth-child(3)').html();
            $("#tableName").val(table_name);
            /*
            $('.selected td:nth-child(3)').each(function()
            {
              console.log($(this).html());
            });
            */
           closeDialog(dialog);
         }
         
         function closeDialog(dialog)
         {
            dialog.dialog('close'); 
            dialog.dialog('destroy').remove();
         }
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
         function Delete()
         {
            
         }
         
         function showTable()
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
            $('#showTable').click(showTable);
         });
        </script>
    </head>
    <body>
        <br/>
        <button id="showTable"> Show Tables </button>
        <br/>
        <br/>
        <table id="classTable"  class="display" cellspacing="0" width="100%">
            <thead>
            <tr>
                <th>Index</th>
                <th>Database</th>
                <th>table Name</th>
            </tr>
            <tbody>
            </tbody>
            <tfoot>
            <tr>
                <th>Index</th>
                <th>Database</th>
                <th>table Name</th>
            </tr>
        </tfoot>
        </thead>
        </table>
    </doby>
</html>