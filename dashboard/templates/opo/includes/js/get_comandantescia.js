function getComandantesCIA(element, opo, excludable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'opo:get_comandantescia' %}",
        type: "GET",
        data: {"opo": opo},
        success: (data) => {
            if(!data["comandantescia"]){
                elemento.append(`<p>Nenhum comandante inserido.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.comandantescia.forEach(comandantecia => {
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">person</i>${comandantecia["comandante"]["postograduacao"]["postograduacao"]||""} ${comandantecia["comandante"]["nomeguerra"]||""} - ${comandantecia["comandante"]["companhia"]["companhia"]||""}${(excludable === true) ? `
                            <a id="delete-comandantecia" style="position: absolute; right: 0;" class="red-text" data-id="${comandantecia["id"]||""}">
                                <i class="material-icons">delete</i>
                            </a>` : ``}
                        </div>
                        <div class="collapsible-body">
                            <p>
                                <strong>Comandante:</strong> ${comandantecia["comandante"]["postograduacao"]["postograduacao"]||""} ${comandantecia["comandante"]["nomeguerra"]||""}
                            </p>
                            <p>
                                <strong>Companhia:</strong> ${comandantecia["comandante"]["companhia"]["companhia"]||""}
                            </p>
                        </div>
                    </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#delete-comandantecia", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'opo:delete_comandantecia' %}", `<p>Nenhum comandante inserido.</p>`);
                });
            }
        }
    });
}