function getTravs(element, guarnicao, editable=false){
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'guarnicao:get_travs_guarnicao' %}",
        type: "GET",
        data: {"guarnicao": guarnicao},
        success: (data) => {
            if(!data["travs"]){
                elemento.append(`<p>Nenhuma TRAV cadastrada.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.travs.forEach(trav => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${trav["codigo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-trav" style="position: absolute; right: 40px;" class="waves-effect" data-id="${trav["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-trav" style="position: absolute; right: 0;" class="red-text" data-id="${trav["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Código:</strong>
                                <strong class="short-text">Código:</strong> ${trav["codigo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Veículo:</strong>
                                <strong class="short-text">Veículo:</strong> ${trav["tipoveiculo"].toUpperCase()||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-trav", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'guarnicao:edit_trav' id=0 %}`.replace('0', $(this).data("id")), 'TRAV '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-trav", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'guarnicao:delete_trav' %}", `<p>Nenhuma TRAV cadastrada.</p>`);
                });
            }
        }
    });
}