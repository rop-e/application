function getMunicoes(element, acessoriosocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'acessoriosocorrencia:get_municoes' %}",
        type: "GET",
        data: {"acessoriosocorrencia": acessoriosocorrencia},
        success: function(data){
            if(!data["municoes"]){
                elemento.append(`<p>Nenhuma munição cadastrada.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.municoes.forEach(municao => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${municao["municao"]["calibre"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-municao" style="position: absolute; right: 40px;" class="waves-effect" data-id="${municao["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-municao" style="position: absolute; right: 0;" class="red-text" data-id="${municao["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Calibre:</strong>
                                <strong class="short-text">Calibre:</strong> ${municao["municao"]["calibre"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Quantidade:</strong>
                                <strong class="short-text">Qtd.:</strong> ${municao["quantidade"]||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-municao", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'acessoriosocorrencia:edit_municao' id=0 %}`.replace('0', $(this).data("id")), 'Munição '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-municao", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'acessoriosocorrencia:delete_municao' %}", `<p>Nenhuma munição cadastrada.</p>`);
                });
            }
        }
    });
}