{% include "ocorrencia/includes/js/get_documentos.js" %}

getDocumentos("listardocumentos", "{{ acessoriosocorrencia }}", true);

$("#doc-form").submit(function(event){
    event.stopPropagation();
    $.ajax({
        type: "POST",
        url: "{% url 'acessoriosocorrencia:post_doc' %}",
        data: $(this).serialize(),
        success: () => {
            $("#doc-form").trigger("reset");
            $("#id_numero").focus();

            M.toast({html: "Documento adicionado com sucesso.", classes: "green"});            

            getDocumentos("listardocumentos", "{{ acessoriosocorrencia }}", true);
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

$("#id_numero").focusout(function(event){
    event.stopPropagation();
    $.ajax({
        type: "GET",
        url: "{% url 'acessoriosocorrencia:checar_numero_existente' %}",
        data: {"numero": $(this).val(), "acessoriosocorrencia": "{{ acessoriosocorrencia }}"},
        success: (response) => {
            if(!response["valid"]){
                M.toast({html: "Você já inseriu esse documento!", classes: "red"});    
                var Numero = $("#id_numero");
                Numero.val("");
                Numero.focus();
            }
        },
        error: (response) => {
            console.log(response);
        }
    });
    return false;
});