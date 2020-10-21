{% include "gestao/includes/js/get_aits.js" %}

getAits("listaraits", "{{ guarnicao.id }}", true);

$("#ait-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'guarnicao:post_ait' %}",
        data: $(this).serialize(),
        success: () => {
            $("#ait-form").trigger("reset");

            M.toast({html: "AIT adicionada com sucesso.", classes: "green"});
            
            getAits("listaraits", "{{ guarnicao.id }}", true);
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