$(document).ready(function(){
    {% include "rat/includes/js/get_envolvidos.js" %}

    getEnvolvidos("listarenvolvidos", "{{ rat.id }}", true);

    {% include "rat/includes/js/get_veiculos.js" %}

    getRATVeiculos("listarveiculos", "{{ rat.id }}", true);

    {% include "rat/includes/js/get_objetos.js" %}

    getObjetos("listarobjetos", "{{ rat.id }}", true);

    $("#apagaRAT").on("click", function(event){
        event.stopPropagation();
        if(confirm("Deseja apagar essa ocorrência?")){
            $.ajax({
                url: "{% url 'rat:post_delete_rat' %}",
                type: "POST",
                data: {"rat": "{{ rat.id }}"},
                success: (response) => {
                    M.toast({html: "Ocorrência deletada com sucesso!", classes: "green", completeCallback: function(){ window.location.href = response.redirect }});
                }
            });
        } else {
            return false;
        }
    });

    $("#finalizarRAT").on("click", function(event){
        event.stopPropagation();
        if(confirm("Deseja finalizar a ocorrência?")){
            M.toast({html: "Ocorrência finalizada com sucesso!", classes: "green", completeCallback: function(){ window.location.href = "{% url 'index' %}"; }});
        } else {
            return false;
        }
    });
});