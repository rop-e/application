function getAnexos(element, rat, editable=false) {
    var elemento = $(`#${element}`);
    elemento.children("ul").html("");

    $.ajax({
        url: "{% url 'rat:get_anexos' %}",
        type: "GET",
        data: {"rat": rat},
        success: (data) => {
            if(!data["anexos"]){
                elemento.append(`<p>Nenhum anexo inserido.</p>`);
            } else {
                elemento.children("ul").css("display", "block");
                elemento.children("p").remove();

                let rows = "";

                data.anexos.forEach((anexo, index) => {
                    index+=1;

                    rows += `<li>
                    <div class="collapsible-header" style="position: relative;">
                        <i class="material-icons">info</i>#${index||""} - ${anexo["observacao"]["observacao"]||""}
                        ${(editable === true) ? `
                        <a id="delete-anexo" style="position: absolute; right: 0;" class="red-text" data-id="${anexo["id"]||""}">
                            <i class="material-icons">delete</i>
                        </a>` : ``}
                    </div>
                    <div class="collapsible-body" style="position: relative;">
                        <p style="float: right;">
                            <a href="${anexo["anexo"]||""}" target="_blank" class="btn waves-effect waves-light">
                                <span class="full-text">
                                    <i class="material-icons right">description</i>Visualizar 
                                </span>
                                <span class="short-text">
                                    <i class="material-icons">remove_red_eye</i>
                                </span>
                            </a>
                        </p>
                        <p>
                            <strong>Observação:</strong> ${anexo["observacao"]["observacao"]||""}
                        </p>
                    </div>
                </li>`;
                });
                elemento.children("ul").append(rows);
                elemento.children("ul").children("li").on("click", "#delete-anexo", function(event){
                    event.stopPropagation();
                    deleteelemento($(this), "{% url 'rat:delete_anexo' %}", `<p>Nenhum anexo inserido.</p>`);
                });
            }
        }
    });
}