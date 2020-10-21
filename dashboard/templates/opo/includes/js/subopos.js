{% include "opo/includes/js/get_subopos.js" %}

getSubOPOS("listarsubopos", "{{ opo.id }}", true);

$("#oporelatorio-form").submit(function(event){
    event.stopPropagation();

    $.ajax({
        type: "POST",
        url: "{% url 'opo:post_subopo' %}",
        data: $(this).serialize(),
        success: () => {
            $("#oporelatorio-form").trigger("reset");
            M.updateTextFields();

            M.toast({html: "SubOPO criada com sucesso.", classes: "green"});

            getSubOPOS("listarsubopos", "{{ opo.id }}", true);
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