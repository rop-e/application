{% include "opo/includes/js/get_comandantescia.js" %}

getComandantesCIA("listarcomandantes", "{{ opo.id }}", true);

$("#comandantecia-form").submit(function(event){
    event.stopPropagation();

    $.ajax({
        type: "POST",
        url: "{% url 'opo:post_comandantecia' %}",
        data: $(this).serialize(),
        success: () => {
            $("#comandantecia-form").trigger("reset");

            M.toast({html: "Comandante de CIA adicionado com sucesso.", classes: "green"});

            getComandantesCIA("listarcomandantes", "{{ opo.id }}", true);
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