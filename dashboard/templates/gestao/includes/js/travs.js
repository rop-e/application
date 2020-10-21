{% include "gestao/includes/js/get_travs.js" %}

getTravs("listartravs", "{{ guarnicao.id }}", true);

$("#trav-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'guarnicao:post_trav' %}",
        data: $(this).serialize(),
        success: () => {
            $("#trav-form").trigger("reset");

            M.toast({html: "TRAV adicionada com sucesso.", classes: "green"});
            
            getTravs("listartravs", "{{ guarnicao.id }}", true);
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