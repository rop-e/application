function formataData(data) {
    var dsplit = data.split("-");
    var dataformatada = dsplit[2] + "/" + dsplit[1] + "/" + dsplit[0];
    return dataformatada;
}

function getEnvolvidos(element, ocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'envolvido:get_envolvidos' %}",
        type: "GET",
        data: {"ocorrencia": ocorrencia},
        success: (data) => {
            if(!data["envolvidos"]){
                elemento.append(`<p>Nenhum envolvido cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.envolvidos.forEach(envolvido => {
                    let rowDtnascimento = envolvido["pessoa"]["datanascimento"], rowMae = envolvido["pessoa"]["mae"];

                    switch (envolvido["pessoa"]["sexo"]) {
                        case "M":
                            rowSexo = "MASCULINO";
                            break;
                        case "F":
                            rowSexo = "FEMININO";
                            break;
                    }

                    rowDtnascimento = (rowDtnascimento !== null) ? `${formataData(rowDtnascimento||"")}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rowMae = (rowMae !== "") ? `${rowMae||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">person</i>${envolvido["pessoa"]["nome"]||""} - ${envolvido["tipoenvolvimento"]["tipo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-envolvido" style="position: absolute; right: 40px;" class="waves-effect" data-id="${envolvido["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a title="Remover" id="delete-envolvido" style="position: absolute; right: 0;" class="red-text" data-id="${envolvido["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Nome:</strong>
                                <strong class="short-text">Nome:</strong> ${envolvido["pessoa"]["nome"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Sexo:</strong>
                                <strong class="short-text">Sexo:</strong> ${rowSexo||""}
                            </p>
                            <p>
                                <strong class="full-text">Data de Nascimento:</strong>
                                <strong class="short-text">Nasc.:</strong> ${rowDtnascimento||""}
                            </p>
                            <p>
                                <strong class="full-text">Nome da mãe:</strong>
                                <strong class="short-text">Mãe:</strong> ${rowMae||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-envolvido", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'envolvido:edit_envolvido_ocorrencia' id=0 %}`.replace('0', $(this).data("id")), 'Envolvido '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-envolvido", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'envolvido:delete_envolvido' %}", `<p>Nenhum envolvido cadastrado.</p>`);
                });
            }
        }
    });
}