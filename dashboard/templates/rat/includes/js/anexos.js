{% include "rat/includes/js/get_anexos.js" %}

getAnexos("listaranexos", "{{ rat.id }}", true);

$("#anexo-form").submit(function(event){
    event.stopPropagation();

    var data = new FormData(this);

    $.ajax({
        type: "POST",
        url: "{% url 'rat:post_anexo' %}",
        data: data,
        processData: false,
        contentType: false,
        success: () => {
            $("#anexo-form").trigger('reset');

            M.toast({html: "Anexo inserido com sucesso.", classes: "green"});

            $('select').formSelect();
            
            getAnexos("listaranexos", "{{ rat.id }}", true);
        },
        error: (response) => {
            var erros = jQuery.parseJSON(response.responseText);
            for(i in erros){
                for(j in erros[i]){
                    M.toast({html: erros[i][j], classes: "red"});
                }
            }
        }
    });
    return false;
});