
<html>
    <head>
        <script type="text/javascript">
            function startProcess()
            {
               $( "#foo" ).trigger( "click" );
            }
            
            function printData(ret)
            {
                alert(ret['data']);
            }
            $("document").ready(function(){
                $( "#foo" ).hide();
                $(".js-ajax-php-json").submit(function(){
                    var data = {
                        "prog" : "docxApi",
                        "op" : "hello",
                    };
                    callPython(data, printData);
                    return false;  // don't reload page after submit.
                });
                
            });
            
        </script>
    </head>
    <body>
        <form class="js-ajax-php-json" accept-charset="utf-8" id="myform">
            <input type="text" name="favorite_beverage" value="" placeholder="Favorite restaurant" />
            <input type="text" name="favorite_restaurant" value="" placeholder="Favorite beverage" />
            <select name="gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
            </select>
            <input id="foo" type="submit" name="submit" value="Submit form"/>
        </form>
    </body>
</html>
