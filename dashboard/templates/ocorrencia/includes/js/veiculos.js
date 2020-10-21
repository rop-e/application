{% include "ocorrencia/includes/js/get_veiculos.js" %}

getVeiculos("listarveiculos", "{{ acessoriosocorrencia }}", true);

$("#veiculo-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'acessoriosocorrencia:post_veiculo' %}",
        data: $(this).serialize(),
        success: () => {
            $("#veiculo-form").trigger('reset');
            $("#id_placa").focus();
            $("#id_chassi").focus();

            M.toast({html: "Veículo adicionado com sucesso.", classes: "green"});
            
            getVeiculos("listarveiculos", "{{ acessoriosocorrencia }}", true);
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

$("#id_placa").focusout(function(event){
    event.stopPropagation();
    $.ajax({
        type: "GET",
        url: "{% url 'acessoriosocorrencia:checar_veiculo_placa_existente' %}",
        data: {"placa": $(this).val(), "acessoriosocorrencia": "{{ acessoriosocorrencia }}"},
        success: function(response){
            if(!response["valid"]){
                M.toast({html: "Você já inseriu um veículo com essa placa!", classes: "red"});
                var Placa = $("#id_placa");
                Placa.val("");
                Placa.focus();
            }
        },
        error: (response) => {
            console.log(response);
        }
    });
    return false;
});

$("#id_chassi").focusout(function(event){
    event.stopPropagation();
    $.ajax({
        type: "GET",
        url: "{% url 'acessoriosocorrencia:checar_veiculo_chassi_existente' %}",
        data: {"chassi": $(this).val(), "acessoriosocorrencia": "{{ acessoriosocorrencia }}"},
        success: (response) => {
            if(!response["valid"]){
                M.toast({html: "Você já inseriu um veículo com esse chassi!", classes: "red"});
                var Chassi = $("#id_chassi");
                Chassi.val("");
                Chassi.focus();
            }
        },
        error: (response) => {
            console.log(response);
        }
    });
    return false;
});