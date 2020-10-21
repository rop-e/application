function getDrogas(element, acessoriosocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'acessoriosocorrencia:get_drogas' %}",
        type: "GET",
        data: {"acessoriosocorrencia": acessoriosocorrencia},
        success: function(data){
            if(!data["drogas"]){
                elemento.append(`<p>Nenhuma droga cadastrada.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.drogas.forEach(droga => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${droga["tipodroga"]["tipo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-droga" style="position: absolute; right: 40px;" class="waves-effect" data-id="${droga["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-droga" style="position: absolute; right: 0;" class="red-text" data-id="${droga["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Droga:</strong>
                                <strong class="short-text">Droga:</strong> ${droga["tipodroga"]["tipo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Quantidade:</strong>
                                <strong class="short-text">Qtd.:</strong> ${droga["quantidade"]||""} ${droga["medida"]["unidade"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Estado:</strong>
                                <strong class="short-text">Estado:</strong> ${droga["armazenamentodroga"]["armazenamento"]||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-droga", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'acessoriosocorrencia:edit_droga' id=0 %}`.replace('0', $(this).data("id")), 'Droga '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-droga", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'acessoriosocorrencia:delete_droga' %}", `<p>Nenhuma droga cadastrada.</p>`);
                });
            }
        }
    });
}