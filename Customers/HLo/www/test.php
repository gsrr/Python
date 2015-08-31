
<html>
    <head>
        <script type="text/javascript">
            function startProcess()
            {
                alert("aaa");
               $( "#foo" ).trigger( "click" );
            }
        
            $("document").ready(function(){
                $( "#foo" ).hide();
                $(".js-ajax-php-json").submit(function(){
                    var data = {
                        "action": "test"
                    };
                    data = $(this).serialize() + "&" + $.param(data);
                    $.ajax({
                        type: "POST",
                        dataType: "json",
                        url: "response.php", //Relative or absolute path to response.php file
                        data: data,
                        success: function(data) {
                            console.log(data);
                            alert("Form submitted successfully.\nReturned json: " + data["json"]);
                        },
                        error: function(xhr) {
                            alert('Ajax request µo¥Í¿ù»~');
                        },
                    });
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
