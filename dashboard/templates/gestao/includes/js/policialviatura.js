{% include "gestao/includes/js/get_policialviatura.js" %}

getPoliciaisViaturas("listarpoliciais", "{{ guarnicao.id }}", true);

$("#policial-form").submit(function(event){
    event.stopPropagation();

    if($("#id_hidden").val() === ""){
        M.toast({html: "Informe um policial!", classes: "red"});
        $("#id_policial").val("");
        return false;
    }
    $.ajax({
        type: "POST",
        url: "{% url 'guarnicao:post_policial' %}",
        data: $(this).serialize(),
        success: () => {
            $("#policial-form").trigger("reset");
            $('select').formSelect();

            M.toast({html: "Policial adicionado na guarnição com sucesso.", classes: "green"});

            getPoliciaisViaturas("listarpoliciais", "{{ guarnicao.id }}", true);
        },
        error: (response) => {
            console.log(response.responseText);
            var erros = jQuery.parseJSON(response.responseText);
            for(let value of Object.values(erros)){
                M.toast({html: value, classes: "red"});
                $("#id_kmsaida").val("");
            }
            $('select').formSelect();
        }
    });
    return false;
});