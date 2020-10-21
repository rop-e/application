function getDiversos(element, acessoriosocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'acessoriosocorrencia:get_diversos' %}",
        type: "GET",
        data: {"acessoriosocorrencia": acessoriosocorrencia},
        success: function(data){
            if(!data["diversos"]){
                elemento.append(`<p>Nenhum objeto cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.diversos.forEach(diverso => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${diverso["tipodiversos"]["tipo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-diverso" style="position: absolute; right: 40px;" class="waves-effect" data-id="${diverso["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-diverso" style="position: absolute; right: 0;" class="red-text" data-id="${diverso["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Tipo:</strong>
                                <strong class="short-text">Tipo:</strong> ${diverso["tipodiversos"]["tipo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Descrição:</strong>
                                <strong class="short-text">Descr.:</strong> ${diverso["descricao"]||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-diverso", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'acessoriosocorrencia:edit_diverso' id=0 %}`.replace('0', $(this).data("id")), 'Objeto '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-diverso", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'acessoriosocorrencia:delete_diverso' %}", `<p>Nenhum objeto cadastrado.</p>`);
                });
            }
        }
    });
}