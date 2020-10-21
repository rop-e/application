{% include "ocorrencia/includes/js/get_municoes.js" %}

getMunicoes("listarmunicoes", "{{ acessoriosocorrencia }}", true);

$("#municao-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'acessoriosocorrencia:post_municao' %}",
        data: $(this).serialize(),
        success: () => {
            $("#municao-form").trigger("reset");

            M.toast({html: "Munição adicionada com sucesso.", classes: "green"});
            
            getMunicoes("listarmunicoes", "{{ acessoriosocorrencia }}", true);
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