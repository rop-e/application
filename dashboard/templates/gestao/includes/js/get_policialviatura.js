function getPoliciaisViaturas(element, guarnicao, excludable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'guarnicao:get_policiais_guarnicao' %}",
        type: "GET",
        data: {"guarnicao": guarnicao},
        success: (data) => {
            if(!data["policialviatura"]){
                elemento.append(`<p>Nenhum policial inserido.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.policialviatura.forEach(policialviatura => {
                    let rowViatura = policialviatura["viatura"];

                    rowViatura = (rowViatura !== null) ? `${policialviatura["viatura"]["numero_viatura"]||""}` : `<span class="full-text">Não informado.</span><span class="short-text">-</span>`;

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">person</i>${policialviatura["policial"]["matricula"]["matricula"]||""} - ${policialviatura["policial"]["postograduacao"]["postograduacao"]||""} ${policialviatura["policial"]["nomeguerra"]||""}${(excludable === true) ? `
                            <a id="delete-policial" style="position: absolute; right: 0;" class="red-text" data-id="${policialviatura["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong>Policial:</strong> ${policialviatura["policial"]["matricula"]["matricula"]||""} - ${policialviatura["policial"]["nomeguerra"]||""}
                            </p>
                            <p>
                                <strong>Função:</strong> ${policialviatura["funcao"]["funcao"]||""}
                            </p>
                            <p>
                                <strong>Viatura:</strong> ${rowViatura||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#delete-policial", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'guarnicao:delete_policial' %}", `<p>Nenhum policial inserido.</p>`);
                });
            }
        }
    });
}