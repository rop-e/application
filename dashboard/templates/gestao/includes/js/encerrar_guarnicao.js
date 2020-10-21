$(document).ready(function(){
    {% include "gestao/includes/js/get_viaturas.js" %}

    getViaturas("listarviaturas", "{{ guarnicao.id }}", true);

    $.ajax({
        url: "{% url 'guarnicao:get_ocorrencias_guarnicao' %}",
        type: "GET",
        data: {"guarnicao": "{{ guarnicao.id }}"},
        success: (data) => {
            if(!data["ocorrencias"]){
                $("#listarocorrencias").append(`<p>Nenhuma ocorrência registrada.</p>`);
            } else {
                $("#listarocorrencias ul").css("display", "block");

                let rows = "";

                data.ocorrencias.forEach(ocorrencia => {
                    let local = `${ocorrencia["endereco"]["municipio"]["nome"]||""}, ${ocorrencia["endereco"]["bairro"]||""}, ${ocorrencia["endereco"]["rua"]||""}`;
                    let link = `{% url 'ocorrencia:mostrar' id=0 %}`.replace('0', ocorrencia["id"]);

                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${ocorrencia["id"]||""} - ${ocorrencia["infracao"]["tipo"]||""}
                        </div>
                        <div class="collapsible-body" style="position: relative;">
                            <p style="float: right;">
                                <a href="${link||""}" class="btn waves-effect waves-light">
                                    <span class="full-text">
                                        <i class="material-icons right">description</i>Visualizar 
                                    </span>
                                    <span class="short-text">
                                        <i class="material-icons">remove_red_eye</i>
                                    </span>
                                </a>
                            </p>
                            <p>
                                <strong class="full-text">Número da Ocorrência:</strong><strong class="short-text">Nº:</strong> ${ocorrencia["id"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Tipo:</strong><strong class="short-text">Tipo:</strong> ${ocorrencia["infracao"]["tipo"]||""}
                            </p>
                            <p>
                                <strong>Local:</strong> ${local||""}
                            </p>
                        </div>
                    </li>`;
                });
                $("#listarocorrencias ul").append(rows);
            }
        }
    });
    
    var noneRAT = `<p>Nenhuma RAT registrada.</p>`;

    $.ajax({
        url: "{% url 'guarnicao:get_rats_guarnicao' %}",
        type: "GET",
        data: {"guarnicao": "{{ guarnicao.id }}"},
        success: (data) => {
            if(!data["rats"]){
                $("#listarrats").append(noneRAT);
            } else {
                $("#listarrats ul").css("display", "block");

                let rows = "";

                data.rats.forEach(rat => {
                    let local = `${rat["endereco"]["municipio"]["nome"]||""}, ${rat["endereco"]["bairro"]||""}, ${rat["endereco"]["rua"]||""}`;
                    let link = `{% url 'rat:mostrar' id=0 %}`.replace('0', rat["id"]);
                    
                    rows += `<li>
                        <div class="collapsible-header" style="position: relative;">
                            <i class="material-icons">info</i>${rat["id"]||""} - ${rat["tipoacidente"]["tipo"]||""}
                        </div>
                        <div class="collapsible-body" style="position: relative;">
                            <p style="float: right;">
                                <a href="${link||""}" class="btn waves-effect waves-light">
                                    <span class="full-text">
                                        <i class="material-icons right">description</i>Visualizar 
                                    </span>
                                    <span class="short-text">
                                        <i class="material-icons">remove_red_eye</i>
                                    </span>
                                </a>
                            </p>
                            <p>
                                <strong class="full-text">Número da RAT:</strong><strong class="short-text">Nº:</strong> ${rat["id"]||""}
                            </p>
                            <p>
                                <strong class="full-text">Tipo de acidente:</strong><strong class="short-text">Tipo:</strong> ${rat["tipoacidente"]["tipo"]||""}
                            </p>
                            <p>
                                <strong>Local:</strong> ${local||""}
                            </p>
                        </div>
                    </li>`;
                });
                $("#listarrats ul").append(rows);
            }
        }
    });
    
    function verificaAndamento() {
        var erros = false;
        $.ajax({
            url: "{% url 'guarnicao:verifica_andamento' %}",
            data: {"guarnicao": "{{ guarnicao.id }}"},
            type: "GET",
            async: false,
            success: (response) => {
                if (response["ocorrencia"]){
                    M.toast({html: "Finalize as ocorrências em andamento!", classes: "red"});
                    erros = true;
                }
                if (response["opo"]){
                    M.toast({html: "Finalize as OPOs em andamento!", classes: "red"});
                    erros = true;
                }
                if (response["rat"]){
                    M.toast({html: "Finalize as RATs em andamento!", classes: "red"});
                    erros = true;
                }
            }
        });
        return erros;
    }

    $("#encerraGuarnicao").on("click", function(){
        var arrayViaturas = [];
        var viaturas = []
        $("#listarviaturas ul input[type=text]").each(function(){
            arrayViaturas.push("viatura");
            arrayViaturas.push($(this).data("id"));
            arrayViaturas.push("kmvolta");
            arrayViaturas.push($(this).val());
        });
        
        for(var i=0; i<arrayViaturas.length; i+=4){
            var objeto_viatura = {};
            objeto_viatura[arrayViaturas[i]] = arrayViaturas[i+1];
            objeto_viatura[arrayViaturas[i+2]] = arrayViaturas[i+3]
            viaturas.push(objeto_viatura);
        }

        var viaturaspreenchidas = 1;

        $("#listarviaturas ul input[type=text]").each(function(){
            if($(this).val() == ""){
                M.toast({html: "Informe a quilometragem de volta da viatura " + $(this).data("viatura") + "!", classes: "red"});
                viaturaspreenchidas = 0;
                return false;
            } else if ($(this).val() < $(this).data("kmanterior")){
                M.toast({html: "Quilometragem de volta da viatura " + $(this).data("viatura") + " menor que quilometragem de saída!", classes: "red"});
                viaturaspreenchidas = 0;
                return false;
            } else {
                viaturaspreenchidas += 1;
            }
        });

        if($("#listarviaturas ul li").length == 0){
            viaturaspreenchidas += 1;
        }

        if(viaturaspreenchidas > 0){
            if(!verificaAndamento()){
                if($("#id_relatorio").val() == ""){
                    M.toast({html: "Informe o relatório de encerramento de serviço!", classes: "red"});
                    return false;
                } else {
                    if(confirm("Deseja encerrar a guarnição?")){
                        localStorage.clear();

                        $.ajax({
                            url: "{% url 'guarnicao:post_encerra_guarnicao' %}",
                            type: "POST",
                            data: {
                                "guarnicao": "{{ guarnicao.id }}",
                                "viaturas": JSON.stringify(viaturas),
                                "relatorio": $("#id_relatorio").val(),
                            },
                            success: (response) => {
                                window.open(response.pdf, "_blank");
                                window.location.href = response.redirect;
                            }
                        });
                    } else {
                        return false;
                    }
                }
            }
        } else {
            return false;
        }
    });
});