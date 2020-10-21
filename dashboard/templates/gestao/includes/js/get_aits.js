function getAits(element, guarnicao, editable=false){
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'guarnicao:get_aits_guarnicao' %}",
        type: "GET",
        data: {"guarnicao": guarnicao},
        success: (data) => {
            if(!data["aits"]){
                elemento.append(`<p>Nenhuma AIT cadastrada.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.aits.forEach(ait => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${ait["codigo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-ait" style="position: absolute; right: 40px;" class="waves-effect" data-id="${ait["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-ait" style="position: absolute; right: 0;" class="red-text" data-id="${ait["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Código:</strong>
                                <strong class="short-text">Código:</strong> ${ait["codigo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Veículo:</strong>
                                <strong class="short-text">Veículo:</strong> ${ait["tipoveiculo"].toUpperCase()||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-ait", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'guarnicao:edit_ait' id=0 %}`.replace('0', $(this).data("id")), 'AIT '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-ait", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'guarnicao:delete_ait' %}", `<p>Nenhuma AIT cadastrada.</p>`);
                });
            }
        }
    });
}