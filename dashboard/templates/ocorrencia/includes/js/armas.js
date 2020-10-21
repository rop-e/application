{% include "ocorrencia/includes/js/get_armas.js" %}

getArmas("listararmas", "{{ acessoriosocorrencia }}", true);

$("#arma-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'acessoriosocorrencia:post_arma' %}",
        data: $(this).serialize(),
        success: () => {
            $("#arma-form").trigger("reset");
            $("#id_numeroserie").focus();

            M.toast({html: "Arma adicionada com sucesso.", classes: "green"});

            getArmas("listararmas", "{{ acessoriosocorrencia }}", true);
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

$("#id_numeroserie").focusout(function(event){
    event.stopPropagation();
    $.ajax({
        type: "GET",
        url: "{% url 'acessoriosocorrencia:checar_numero_serie_existente' %}",
        data: {"numeroserie": $(this).val(), "acessoriosocorrencia": "{{ acessoriosocorrencia }}"},
        success: (response) => {
            if(!response["valid"]){
                M.toast({html: "Você já inseriu essa arma!", classes: "red"});
                var Numeroserie = $("#id_numeroserie");
                Numeroserie.val("");
                Numeroserie.focus();
            }
        },
        error: (response) => {
            console.log(response);
        }
    });
    return false;
});