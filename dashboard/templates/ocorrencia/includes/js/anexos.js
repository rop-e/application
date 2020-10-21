{% include "ocorrencia/includes/js/get_anexos.js" %}

getAnexos("listaranexos", "{{ ocorrencia }}", true);

$("#anexo-form").submit(function(event){
    event.stopPropagation();

    var data = new FormData(this);

    $.ajax({
        type: "POST",
        url: "{% url 'ocorrencia:post_anexo' %}",
        data: data,
        processData: false,
        contentType: false,
        success: () => {
            $("#anexo-form").trigger('reset');

            M.toast({html: "Anexo inserido com sucesso.", classes: "green"});

            $('select').formSelect();
            
            getAnexos("listaranexos", "{{ ocorrencia }}", true);
        },
        error: (response) => {
            M.toast({html: "Não foi possível adicionar esse anexo.", classes: "red"});
            // var erros = jQuery.parseJSON(response.responseText);
            // for(i in erros){
            //     for(j in erros[i]){
            //         M.toast({html: erros[i][j], classes: "red"});
            //     }
            // }
        }
    });
    return false;
});