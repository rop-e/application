{% include "ocorrencia/includes/js/get_aditamentos.js" %}

getAditamentos("listaraditamentos", "{{ ocorrencia.id }}");

$("#aditamento-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'ocorrencia:post_aditamento' %}",
        data: $(this).serialize(),
        success: () => {
            $("#aditamento-form").trigger("reset");

            M.toast({html: "Aditamento adicionado com sucesso.", classes: "green"});

            getAditamentos("listaraditamentos", "{{ ocorrencia.id }}");
        }
    });
    return false;
});