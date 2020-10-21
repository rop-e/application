{% include "ocorrencia/includes/js/get_diversos.js" %}

getDiversos("listardiversos", "{{ acessoriosocorrencia }}", true);

$("#diverso-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'acessoriosocorrencia:post_diverso' %}",
        data: $(this).serialize(),
        success: function(){
            $("#diverso-form").trigger("reset");

            M.toast({html: "Objeto adicionado com sucesso.", classes: "green"});

            getDiversos("listardiversos", "{{ acessoriosocorrencia }}", true);
        },
        error: function(response){
            var erros = jQuery.parseJSON(response.responseText);
            for(let value of Object.values(erros)){
                M.toast({html: value, classes: "red"});
            }
        }
    });
    return false;
});