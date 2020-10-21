function getArmas(element, acessoriosocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'acessoriosocorrencia:get_armas' %}",
        type: "GET",
        data: {"acessoriosocorrencia": acessoriosocorrencia},
        success: function(data){
            if(!data["armas"]){
                elemento.append(`<p>Nenhuma arma cadastrada.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.armas.forEach(arma => {
                    let rowCalibre = arma["arma"]["calibre"], rowNumeroSerie = arma["arma"]["numeroserie"], rowFabricante = arma["arma"]["fabricantearma"];

                    rowCalibre = (rowCalibre !== null) ? `${arma["arma"]["calibre"]["calibre"]||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rowNumeroSerie = (rowNumeroSerie !== null) ? `${arma["arma"]["numeroserie"]||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;
                    
                    rowFabricante = (rowFabricante !== null) ? `${arma["arma"]["fabricantearma"]["sigla"]||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${arma["arma"]["modelo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-arma" style="position: absolute; right: 40px;" class="waves-effect" data-id="${arma["arma"]["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-arma" style="position: absolute; right: 0;" class="red-text" data-id="${arma["arma"]["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Arma:</strong>
                                <strong class="short-text">Arma:</strong> ${arma["arma"]["tipoarma"]["tipo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Tipo:</strong>
                                <strong class="short-text">Tipo:</strong> ${arma["arma"]["modelo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Calibre:</strong>
                                <strong class="short-text">Calibre:</strong> ${rowCalibre||""}
                            </p>
                            <p>
                                <strong class="full-text">Fabricante:</strong>
                                <strong class="short-text">Fabric.:</strong> ${rowFabricante||""}
                            </p>
                            <p>
                                <strong class="full-text">Nº Série:</strong>
                                <strong class="short-text">Série:</strong> ${rowNumeroSerie||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-arma", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'acessoriosocorrencia:edit_arma' id=0 %}`.replace('0', $(this).data("id")), 'Arma '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-arma", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'acessoriosocorrencia:delete_arma' %}", `<p>Nenhuma arma cadastrada.</p>`);
                });
            }
        }
    });
}