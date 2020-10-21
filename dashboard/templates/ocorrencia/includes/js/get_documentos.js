function getDocumentos(element, acessoriosocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'acessoriosocorrencia:get_docs' %}",
        type: "GET",
        data: {"acessoriosocorrencia": acessoriosocorrencia},
        success: function(data){
            if(!data["docs"]){
                elemento.append(`<p>Nenhum documento cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.docs.forEach(doc => {
                    let rowNumero = doc["numero"];

                    rowNumero = (rowNumero !== null) ? `${doc["numero"]||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${doc["tipodoc"]["tipo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-doc" style="position: absolute; right: 40px;" class="waves-effect" data-id="${doc["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-doc" style="position: absolute; right: 0;" class="red-text" data-id="${doc["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Tipo de Documento:</strong>
                                <strong class="short-text">Tipo:</strong> ${doc["tipodoc"]["tipo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Número:</strong>
                                <strong class="short-text">Núm.:</strong> ${rowNumero||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-doc", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'acessoriosocorrencia:edit_doc' id=0 %}`.replace('0', $(this).data("id")), 'Documento '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-doc", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'acessoriosocorrencia:delete_doc' %}", `<p>Nenhum documento cadastrado.</p>`);
                });
            }
        }
    });
}