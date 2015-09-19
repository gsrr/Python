<html>
    <head>
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" />
        <link rel="stylesheet" href="../lib/google-code-prettify/prettify.css" />
        <link rel="stylesheet" href="../css/style.css" />
        
        <script>
        function initialTable(contents)
        {
            alert("initialTable");
            var res = contents.split("\n");
            var dataSet = [];
            for(var i = 0 ; i < res.length ; i++)
            {
                var str = res[i].slice(0,-1);
                console.log(str);
                var item = str.split(",");
                item[1] = item[1].replace(/;/g, ",");
                console.log(item);
                dataSet.push(item);
            }
            $('#tableInput_wrapper').remove();
            //$('#tableInput_wrapper').remove();
            $('#tableArea').append('<table id="tableIuput"  class="dataTable" cellspacing="0" style="width:100%"></table>');
            console.log(dataSet);
              
             $('#tableIuput').DataTable( {
                "scrollY":"200px",
                "scrollCollapse": true,
                "paging": false,
                data: dataSet,
                columns: [
                    { title: "Id" },
                    { title: "Label" },
                    { title: "Path" },
                ]
            });
        }
        function readSingleFile(evt) {
        //Retrieve the first (and only!) File from the FileList object
        var f = evt.target.files[0]; 

        if (f) {
          var r = new FileReader();
          r.onload = function(e) { 
              var contents = e.target.result;
            alert( "Got the file.n" 
                  +"name: " + f.name + "\n"
                  +"type: " + f.type + "\n"
                  +"size: " + f.size + " bytesn" + "\n"
                  + "starts with: " + contents.substr(1, contents.indexOf("n"))
            );  
            initialTable(contents.trim());
          }
          r.readAsText(f);
        } 
        else 
        { 
          alert("Failed to load file");
        }
      }
         $("document").ready(function(){
            function importCSV()
            {
                alert("Import csv");
                readSingleFile();
            }
            document.getElementById('csvfile').addEventListener('change', readSingleFile, false);
            //$("#import_csv").click(importCSV);
            $('#multiselect').multiselect();
         });
        </script>
    </head>
    <body>
        <div class="row">
            <div class="col-xs-5">
                <select name="from" id="multiselect" class="form-control" size="8" multiple="multiple">
                    <option value="1">Item 1</option>
                    <option value="2">Item 5</option>
                    <option value="2">Item 2</option>
                    <option value="2">Item 4</option>
                    <option value="3">Item 3</option>
                </select>
            </div>
            
            <div class="col-xs-2">
                <button type="button" id="multiselect_rightAll" class="btn btn-block"><i class="glyphicon glyphicon-forward"></i></button>
                <button type="button" id="multiselect_rightSelected" class="btn btn-block"><i class="glyphicon glyphicon-chevron-right"></i></button>
                <button type="button" id="multiselect_leftSelected" class="btn btn-block"><i class="glyphicon glyphicon-chevron-left"></i></button>
                <button type="button" id="multiselect_leftAll" class="btn btn-block"><i class="glyphicon glyphicon-backward"></i></button>
            </div>
            
            <div class="col-xs-5">
                <select name="to" id="multiselect_to" class="form-control" size="8" multiple="multiple"></select>
            </div>
        </div>
        <script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/prettify.min.js"></script>
	<script type="text/javascript" src="js/multiselect.min.js"></script>    
    </body>
    
    
   
   
</html>