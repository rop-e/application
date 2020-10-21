{% include "rat/includes/js/get_objetos.js" %}

getObjetos("listarobjetos", "{{ rat.id }}", true);

$("#objeto-form").submit(function(event){
    event.stopPropagation();

    $.ajax({
        type: "POST",
        url: "{% url 'rat:post_objeto' %}",
        data: $(this).serialize(),
        success: () => {
            $("#objeto-form").trigger("reset");

            M.toast({html: "Objeto adicionado com sucesso.", classes: "green"});

            getObjetos("listarobjetos", "{{ rat.id }}", true);
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