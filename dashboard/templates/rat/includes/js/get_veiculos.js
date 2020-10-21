function getRATVeiculos(element, rat, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");
    
    $("#selectVeiculos").html(`<option value="">---------</option>`);

    $.ajax({
        url: "{% url 'rat:get_veiculos' %}",
        type: "GET",
        data: {"rat": rat},
        success: (data) => {
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
                            <i class="material-icons">info</i>${veiculo["veiculo"]["modelo"]||""} - ${veiculo["veiculo"]["cor"]||""}
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
                                <strong>Modelo:</strong> ${veiculo["veiculo"]["modelo"]||""}
                            </p>
                            <p>
                                <strong>Cor:</strong> ${veiculo["veiculo"]["cor"]||""}
                            </p>
                            <p>
                                <strong>Placa:</strong> ${rowPlaca||""}
                            </p>
                        </div>
                    </li>`;

                    $("#selectVeiculos").append(`
                        <option value="${veiculo["id"]||""}">${veiculo["veiculo"]["modelo"]||""} - ${veiculo["veiculo"]["cor"]||""}</option>
                    `);
                });

                $('select').formSelect();

                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#edit-veiculo", function(event){
                    event.stopPropagation();
                    window.open(`{% url 'rat:edit_veiculo' id=0 %}`.replace('0', $(this).data("id")), 'Veículo '+ $(this).data("id"), 'width=600,height=800,scrollbars=no');
                });
                elemento.children("ul").children("li").on("click", "#delete-veiculo", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'rat:delete_veiculo' %}", `<p>Nenhum veículo cadastrado.</p>`);
                });
            }
        }
    });
}