{% load ropd_extras %}

{% if request.user|has_group:"CPO" or ocorrencia.guarnicao.comandante == request.user.policial %}
    function verificaAutorAditamento(autor, request_id) {
        return (autor == request_id) ? true : false;
    }
{% endif %}

function getAditamentos(element, ocorrencia) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'ocorrencia:get_aditamentos' %}",
        type: "GET",
        data: {"ocorrencia": ocorrencia},
        success: (data) => {
            if(!data["aditamentos"]){
                elemento.append(`<p>Nenhum aditamento cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";
                
                data.aditamentos.forEach((aditamento, index) => {
                    index+=1;

                    let autor = aditamento["autor"]["postograduacao"]["postograduacao"] + " "+ aditamento["autor"]["nomeguerra"];
                    let ativo = (aditamento["ativo"]) ? false : " disabled";

                    rows += `<li>
                    <div class="collapsible-header" style="position: relative;">
                        <i class="material-icons">person</i>#${index||""} - ${autor||""}${(!aditamento["ativo"]) ? ' - CANCELADO' : ''}
                    </div>
                    <div class="collapsible-body" style="position: relative;">
                        {% if request.user|has_group:"CPO" or ocorrencia.guarnicao.comandante == request.user.policial %}
                        ${(verificaAutorAditamento(aditamento["autor"]["id"], "{{ request.user.policial.id }}")||"") ? `
                            <p style="float: right;">
                                <a id="cancel-aditamento" data-id="${aditamento["id"]||""}" class="btn waves-effect waves-light${ativo||""}">
                                    <i class="material-icons right">cancel</i>Cancelar 
                                </a>
                            </p>` : ``}
                        {% endif %}
                        <p>
                            Aditamento: ${aditamento["observacao"]["observacao"]||""}
                        </p>
                    </div>
                </li>`;
                });
                elemento.children("ul").append(rows);
                {% if request.user|has_group:"CPO" or ocorrencia.guarnicao.comandante == request.user.policial %}
                    elemento.children("ul").children("li").on("click", "#cancel-aditamento", function(event){
                        event.stopPropagation();
                        if(confirm("Deseja cancelar o aditamento?")){
                            $.ajax({
                                url: "{% url 'ocorrencia:cancel_aditamento' %}",
                                type: "POST",
                                data: {"id": $(this).data("id")},
                                success: (response) => {
                                    M.toast({html: response.message, classes: "green"});
                                    $(this).attr("disabled", "true");
                                },
                                error: (response) => {
                                    console.log(response.responseText);
                                }
                            });
                        } else {
                            return false;
                        }
                    });
                {% endif %}
            }
        }
    });
}