function getVeiculos(element, acessoriosocorrencia, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'acessoriosocorrencia:get_veiculos' %}",
        type: "GET",
        data: {"acessoriosocorrencia": acessoriosocorrencia},
        success: function(data){
            if(!data["veiculos"]){
                elemento.append(`<p>Nenhum veículo cadastrado.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.veiculos.forEach(veiculo => {
                    let rowPlaca = veiculo["veiculo"]["placa"];

                    rowPlaca = (rowPlaca !== null) ? `${veiculo["veiculo"]["placa"]||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${veiculo["veiculo"]["modelo"]||""}
                            ${(editable === true) ? `
                            <a title="Editar" id="edit-veiculo" style="position: absolute; right: 40px;" class="waves-effect" data-id="${veiculo["veiculo"]["id"]||""}">
                                <i class="material-icons">edit</i>
                            </a>
                            <a id="delete-veiculo" style="position: absolute; right: 0;" class="red-text" data-id="${veiculo["veiculo"]["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Modelo:</strong>
                                <strong class="short-text">Modelo:</strong> ${veiculo["veiculo"]["modelo"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Cor:</strong>
                                <strong class="short-text">Cor:</strong> ${veiculo["veiculo"]["cor"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Placa:</strong>
                                <strong class="short-text">Placa:</strong> ${rowPlaca||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-veiculo", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'acessoriosocorrencia:edit_veiculo' id=0 %}`.replace('0', $(this).data("id")), 'Veículo '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-veiculo", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'acessoriosocorrencia:delete_veiculo' %}", `<p>Nenhum veículo cadastrado.</p>`);
                });
            }
        }
    });
}