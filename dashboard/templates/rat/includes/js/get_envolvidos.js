function formataData(data) {
    var dsplit = data.split("-");
    var dataformatada = dsplit[2] + "/" + dsplit[1] + "/" + dsplit[0];
    return dataformatada;
}

function getEnvolvidos(element, rat, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'envolvido:get_envolvidosrat' %}",
        data: {"rat": rat},
        success: (data) => {
            if(!data["veiculoenvolvidos"] && !data["envolvidossemveiculo"]){
                elemento.append(`<p>Nenhum envolvido cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";
            
                if(data["veiculoenvolvidos"]){
                    data.veiculoenvolvidos.forEach(veiculoenvolvido => {
                        let rowDtnascimento = veiculoenvolvido["envolvido"]["pessoa"]["datanascimento"], rowMae = veiculoenvolvido["envolvido"]["pessoa"]["mae"];

                        switch (veiculoenvolvido["envolvido"]["pessoa"]["sexo"]) {
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
                                <i class="material-icons">person</i>${veiculoenvolvido["envolvido"]["pessoa"]["nome"]||""} - ${veiculoenvolvido["envolvido"]["tipoenvolvimento"]["tipo"]||""} - ${veiculoenvolvido["ratveiculos"]["veiculo"]["modelo"]||""} ${veiculoenvolvido["ratveiculos"]["cor"]||""}
                                ${(editable === true) ? `
                                <a title="Editar" id="edit-envolvido" style="position: absolute; right: 40px;" class="waves-effect" data-id="${veiculoenvolvido["envolvido"]["id"]||""}">
                                    <i class="material-icons">edit</i>
                                </a>
                                <a title="Remover" id="delete-envolvido" style="position: absolute; right: 0;" class="red-text" data-id="${veiculoenvolvido["envolvido"]["id"]||""}">
                                    <i class="material-icons">delete</i>
                                </a>` : ``}
                            </div>
                            <div class="collapsible-body">
                                <p>
                                    <strong>Nome:</strong> ${veiculoenvolvido["envolvido"]["pessoa"]["nome"]||""}
                                </p>
                                <p>
                                    <strong>Sexo:</strong> ${rowSexo||""}
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
                }

                if(data["envolvidossemveiculo"]){
                    data.envolvidossemveiculo.forEach(envolvidosemveiculo => {
                        let rowDtnascimento = envolvidosemveiculo["pessoa"]["datanascimento"], rowMae = envolvidosemveiculo["pessoa"]["mae"];

                        switch (envolvidosemveiculo["pessoa"]["sexo"]) {
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
                                <i class="material-icons">person</i>${envolvidosemveiculo["pessoa"]["nome"]||""} - ${envolvidosemveiculo["tipoenvolvimento"]["tipo"]||""} - SEM VEÍCULO
                                ${(editable === true) ? `
                                <a title="Editar" id="edit-envolvido" style="position: absolute; right: 40px;" class="waves-effect" data-id="${envolvidosemveiculo["id"]||""}">
                                    <i class="material-icons">edit</i>
                                </a>
                                <a title="Remover" id="delete-envolvido" style="position: absolute; right: 0;" class="red-text" data-id="${envolvidosemveiculo["id"]||""}">
                                    <i class="material-icons">delete</i>
                                </a>` : ``}
                            </div>
                            <div class="collapsible-body">
                                <p>
                                    <strong>Nome:</strong> ${envolvidosemveiculo["pessoa"]["nome"]||""}
                                </p>
                                <p>
                                    <strong>Sexo:</strong> ${rowSexo||""}
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
                }

                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-envolvido", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'envolvido:edit_envolvido_rat' id=0 %}`.replace('0', $(this).data("id")), 'Envolvido '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-envolvido", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'envolvido:delete_envolvido' %}", `<p>Nenhum envolvido cadastrado.</p>`);
                });
            }
        }
    });
}