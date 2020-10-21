{% include "ocorrencia/includes/js/get_drogas.js" %}

getDrogas("listardrogas", "{{ acessoriosocorrencia }}", true);
    
$("#droga-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'acessoriosocorrencia:post_droga' %}",
        data: $(this).serialize(),
        success: function(){
            $("#droga-form").trigger("reset");

            M.toast({html: "Droga adicionada com sucesso.", classes: "green"});

            getDrogas("listardrogas", "{{ acessoriosocorrencia }}", true);
        },
        error: function(response){
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