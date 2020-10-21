{% include "gestao/includes/js/get_rrds.js" %}

getRrds("listarrrds", "{{ guarnicao.id }}", true);

$("#rrd-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'guarnicao:post_rrd' %}",
        data: $(this).serialize(),
        success: () => {
            $("#rrd-form").trigger("reset");

            M.toast({html: "RRD adicionada com sucesso.", classes: "green"});
            
            getRrds("listarrrds", "{{ guarnicao.id }}", true);
        },
        error: (response) => {
            var erros = jQuery.parseJSON(response.responseText);
            for(let value of Object.values(erros)){
                M.toast({html: value, classes: "red"});
            }
        }
    });
    return false;
});