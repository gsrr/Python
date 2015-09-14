<html>
    <head>
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
        } else { 
          alert("Failed to load file");
        }
      }
         $("document").ready(function(){
            function importCSV()
            {
                readSingleFile();
            }
            document.getElementById('csvfile').addEventListener('change', readSingleFile, false);
            $("#import_csv").click(importCSV);
         });
        </script>
    </head>
    <body>
        
        <table>
            <tr>
                <td><button id="import_csv" style="width:100%">Import CSV</button></td>
                <td><input type="file" name="csvfile" id="csvfile"></td>
            </tr>
    </table>
        <br/>
        <br/>
        <button id="random" style="width:150px">Randomize</button>
        <button id="genSubject" style="width:150px">Generate</button>
        <br/>
        <div id="tableArea">
        <table id="classTable"  class="display" cellspacing="0" style="width:100%">
        </table>
        </div>
        
    </doby>
</html>