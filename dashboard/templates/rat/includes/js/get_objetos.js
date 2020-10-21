function getObjetos(element, rat, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'rat:get_objetos' %}",
        type: "GET",
        data: {"rat": rat},
        success: (data) => {
            if(!data["objetos"]){
                elemento.append(`<p>Nenhum objeto cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.objetos.forEach(objeto => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${objeto["descricao"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-objeto" style="position: absolute; right: 40px;" class="waves-effect" data-id="${objeto["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-objeto" style="position: absolute; right: 0;" class="red-text" data-id="${objeto["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong>Descrição:</strong> ${objeto["descricao"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Quantidade:</strong>
                                <strong class="short-text">Qtd.:</strong> ${objeto["quantidade"]||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-objeto", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'rat:edit_objeto' id=0 %}`.replace('0', $(this).data("id")), 'Objeto '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-objeto", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'rat:delete_objeto' %}", `<p>Nenhum objeto cadastrado.</p>`);
                });
            }
        }
    });
}