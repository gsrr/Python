

function callPython(paras,func)
{
    alert("call Python");
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1/channel.php",
        data: paras,
        success: function(ret) {;
            func(ret);
        },
        error: function(xhr) {
            alert('Ajax request error');
        },
    });
}