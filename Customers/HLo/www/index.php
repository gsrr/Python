<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>jQuery UI Button - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
  <link rel="stylesheet" href="https://cdn.datatables.net/1.10.8/css/dataTables.jqueryui.min.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
  <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
  <script src="https://cdn.datatables.net/1.10.8/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.datatables.net/1.10.8/js/dataTables.jqueryui.min.js"></script>
  
  <script>
  
  
  function importDialog()
  {     
        var url = "./import.php";
        var dia = $( "<div></div>" ).dialog({ 
            autoOpen: false,
            height: 'auto',
            width: 'auto',
            buttons: { 
                "Go": function() { startProcess(); },
            },
            close: function(event, ui) 
            { 
                $(this).dialog('close');
                $(this).dialog('destroy').remove()
            },
        });
        dia.load(url);
        dia.dialog("open");
  }
  
  function test()
  {
    var url = "./test.php";
    var dia = $( "<div></div>" ).dialog({ 
        autoOpen: false,
        height: 'auto',
        width: 'auto',
        buttons: { 
            "Go": function() { startProcess(); },
        },
        
    });
    dia.load(url);
    dia.dialog("open");
  }
  $(function() {
    $( "button" ).button();
    $("#test").click(function(){
        test();
    });
    $("#import").click(function(){
        importDialog();
    });
  });
  
 
  </script>
</head>
<body>
 
<button id="import">Import</button>
<button id="list">List</button>
<button id="generate">Generate</button>
<button id="test">Test</button>
</body>
</html>