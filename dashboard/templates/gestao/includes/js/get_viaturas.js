function getViaturas(element, guarnicao, populate=false){
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'guarnicao:get_viaturas' %}",
        type: "GET",
        data: {"guarnicao": guarnicao},
        success: (data) => {
            if(data["viaturas"]){
                elemento.children("ul").css("display", "block");

                let rows = "";

                data.policialviatura.filter(viatura => {
                    return viatura.kmsaida;
                }).forEach(viatura => {
                    let value = localStorage.getItem(viatura["viatura"]["numero_viatura"]);

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${viatura["viatura"]["numero_viatura"]||""}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong class="full-text">Viatura:</strong>
                                <strong class="short-text">Viatura:</strong> ${viatura["viatura"]["numero_viatura"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Motorista/Piloto:</strong>
                                <strong class="short-text">Motorista/Piloto:</strong> ${viatura["policial"]["nomeguerra"]||""} - ${viatura["policial"]["postograduacao"]["postograduacao"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Quilometragem de Saída:</strong>
                                <strong class="short-text">KM Saída:</strong> ${viatura["kmsaida"]||""}
                            </p>
                            ${(populate) ? `
                            <br>
                            <p class="input-field">
                                <input class="validate" id="input-viatura-${viatura["id"]||""}" value="${value||""}" type="text" data-kmanterior="${viatura["kmsaida"]||""}" data-id="${viatura["id"]||""}" data-viatura="${viatura["viatura"]["numero_viatura"]||""}">
                                <label for="input" class="active">
                                    <span class="full-text">Quilometragem de Volta</span>
                                    <span class="short-text">KM Volta</span>
                                </label>
                            </p>` : `
                            <p>
                                <strong class="full-text">Quilometragem de Volta:</strong>
                                <strong class="short-text">KM Volta:</strong> ${viatura["kmvolta"]||""}
                            </p>`}
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("change", "input[type=text]", function(event){
                    event.stopPropagation();
                    localStorage.setItem($(this).data("viatura"), $(this).val());
                });
            } else {
                elemento.append(`<p>Nenhuma viatura cadastrada.</p>`);
            }
        }
    });
}