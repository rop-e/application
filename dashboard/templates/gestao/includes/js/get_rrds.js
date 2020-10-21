function getRrds(element, guarnicao, editable=false){
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'guarnicao:get_rrds_guarnicao' %}",
        type: "GET",
        data: {"guarnicao": guarnicao},
        success: (data) => {
            if(!data["rrds"]){
                elemento.append(`<p>Nenhuma RRD cadastrada.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.rrds.forEach(rrd => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${rrd["codigo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-rrd" style="position: absolute; right: 40px;" class="waves-effect" data-id="${rrd["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-rrd" style="position: absolute; right: 0;" class="red-text" data-id="${rrd["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Código:</strong>
                                <strong class="short-text">Código:</strong> ${rrd["codigo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Veículo:</strong>
                                <strong class="short-text">Veículo:</strong> ${rrd["tipoveiculo"].toUpperCase()||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-rrd", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'guarnicao:edit_rrd' id=0 %}`.replace('0', $(this).data("id")), 'RRD '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-rrd", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'guarnicao:delete_rrd' %}", `<p>Nenhuma RRD cadastrada.</p>`);
                });
            }
        }
    });
}