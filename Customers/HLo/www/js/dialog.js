function createDialog(paras)
{     
    var dia = $( "<div></div>" ).dialog({ 
        autoOpen: false,
        height: 'auto',
        width: 'auto',
        resizable: true,
        buttons: paras["button"],
        close: function(event, ui) 
        { 
            $(this).dialog('close');
            $(this).dialog('destroy').remove()
        },
        position: "center",
    });
    dia.load(paras['url']);
    return dia;
}