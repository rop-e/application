function getSubOPOS(element, opo, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'opo:get_subopos' %}",
        type: "GET",
        data: {"opo": opo},
        success: (data) => {
            if(!data["subopos"]){
                elemento.append(`<p>Nenhuma SubOPO inserida.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.subopos.forEach((subopo, index) => {
                    index+=1;

                    let rowDataFinalizacao = subopo["datafinalizacao"];
                    
                    rowDataFinalizacao = (rowDataFinalizacao !== null) ? `${rowDataFinalizacao||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">person</i>${index||""} - ${subopo["local"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-subopo" style="position: absolute; right: 40px;" class="waves-effect" data-id="${subopo["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-subopo" style="position: absolute; right: 0;" class="red-text" data-id="${subopo["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong>Local:</strong> ${subopo["local"]||""}
                            </p>
                            <p>
                                <strong>Data de execução:</strong> ${subopo["dataexecucao"]||""}
                            </p>
                            <p>
                                <strong>Data de finalização:</strong> ${rowDataFinalizacao||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-subopo", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'opo:edit_subopo' id=0 %}`.replace('0', $(this).data("id")), 'SubOPO '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-subopo", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'opo:delete_subopo' %}", `<p>Nenhuma SubOPO inserida.</p>`);
                });
            }
        }
    });
}