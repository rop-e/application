
{% include "rat/includes/js/get_envolvidos.js" %}

getEnvolvidos("listarenvolvidos", "{{ rat.id }}", true);

function validaAgenteRecebedor(Local, nomeAgente, cargo){
    if(Local.val() != ""){
        if(nomeAgente.val() == "" && cargo.val() == ""){
            M.toast({html: "Informe o agente recebedor!", classes: "red"});
            return false;
        } else if(nomeAgente.val() != "" && cargo.val() == ""){
            M.toast({html: "Informe o cargo do agente recebedor.", classes: "red"});
            return false;
        } else if(cargo.val() != "" && nomeAgente.val() == ""){
            M.toast({html: "Informe o nome do agente recebedor.", classes: "red"});
            return false;
        }
    }
    return true;
}

function TestaCPF(strCPF){
    strCPF = strCPF.replace(/[^\d]+/g, '');
    var Soma;
    var Resto;
    Soma = 0;
    if(strCPF == "00000000000"){
        return false;
    }
    for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);
        Resto = (Soma * 10) % 11;

        if ((Resto == 10) || (Resto == 11)) Resto = 0;
        if (Resto != parseInt(strCPF.substring(9, 10))) return false;

        Soma = 0;

        for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);

        Resto = (Soma * 10) % 11;
    if((Resto == 10) || (Resto == 11)) Resto = 0;
    if(Resto != parseInt(strCPF.substring(10, 11))) return false;
    return true;
}

$("#envolvido-form").submit(function(event){
    event.stopPropagation();
    
    let envLocal = $("#id_localrecebedor_envolvido"), envNomeAgente = $("#id_nome_agente_envolvido"), envCargo = $("#id_cargo_envolvido");

    if($("#id_cpf").val() != ""){
        if(!TestaCPF($("#id_cpf").val())){
            M.toast({html: "CPF inválido.", classes: "red"});
            return false;
        }
    }

    if(validaAgenteRecebedor(envLocal, envNomeAgente, envCargo)){
        $.ajax({
            type: "POST",
            url: "{% url 'envolvido:post_envolvidorat' %}",
            data: $(this).serialize(),
            success: () => {
                $("#envolvido-form").trigger("reset");
                $("#envolvido-form #id_nome").focus();

                M.toast({html: "Envolvido adicionado com sucesso.", classes: "green"});

                getEnvolvidos("listarenvolvidos", "{{ rat.id }}", true);
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

        M.updateTextFields();
        $('select').formSelect();
    }
    return false;
});

$("#envolvido-form #id_nome").focusout(function(event){
    event.stopPropagation();

    $.ajax({
        type: "GET",
        url: "{% url 'envolvido:checar_nome_existente' %}",
        data: {"nome": $("#envolvido-form #id_nome").val(), "rat": "{{ rat.id }}"},
        success: (response) => {
            if(response["invalid"]){
                M.toast({html: "Você já inseriu essa pessoa como envolvida!", classes: "red"});
                $("#envolvido-form").trigger("reset");
            }
        }
    });
    return false;
});