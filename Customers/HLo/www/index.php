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
    <script src="./js/callPython.js"></script>
    <script src="./js/dialog.js"></script>

    <script>
        
        function importDialog() {
            var $dia;
            function startProcess() 
            {
                var data = {
                    "prog": "docxApi",
                    "op": "insertID",
                    "user": $("#user").val(),
                    "password": $("#passwd").val(),
                    "db": $("#db_menu option:selected").val(),
                    "table": $("#table_menu option:selected").val(),
                    "prefix": $("#id_prefix").val(),
                };
                callPython(data, function(ret) {
                    alert(ret['data']);
                });
                $dia.dialog("close");
            }
            var paras = [];
            paras['url'] = "./import.php";
            paras['button'] = {
                'Go': startProcess,
            };
            $dia = createDialog(paras);
            $dia.dialog("open");
        }

        function test() {
            var url = "./test.php";
            var dia = $("<div></div>").dialog({
                autoOpen: false,
                height: 'auto',
                width: 'auto',
                buttons: {
                    "Go": function() {
                        startProcess();
                    },
                },

            });
            dia.load(url);
            dia.dialog("open");
        }
        function callIframe(url, callback) {
            $(document.body).append('<IFRAME id="myId" ...>');
            $('iframe#myId').attr('src', url);

            $('iframe#myId').load(function() {
                callback(this);
            });
        }
        $(function() {
            function listData()
            {
                 var paras = [];
                paras['url'] = "./list/table.php";
                paras['button'] = {};
                $dia = createDialog(paras);
                $dia.dialog("open");
                //$("#mydiv").empty().load("./list/table.php");
            }
            $("button").button();
            $("#test").click(function() {
                test();
            });
            $("#import").click(function() {
                importDialog();
            });
            $("#list").click(function() {
                listData();
            });
            $("#generate").click(function() {
               window.location.href = "./generate/generate.html";
            });
            $("#labelop").click(function() {
               window.location.href = "./fileManager/index.html";
            });
        });
    </script>
</head>

<body>

    <button id="import">Import</button>
    <button id="list">List</button>
    <button id="generate">Generate</button>
    <button id="labelop">Add Label</button>
</body>

</html>