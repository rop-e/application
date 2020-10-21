$(document).ready(function(){
    var elementoApreensoes = $("#apreensoes");
    var divapreensoes = `
    <div class="row">
        <div class="col s12 l12 m12">
            <h5><strong>Apreensões</strong></h5>
        </div>
    </div>

    <div id="conteudoapreensoes"></div>
    `;
    var tabelaenvolvidos = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Envolvidos</span>
                        <span class="short-text">Envolvidos</span>
                    </span>
                    <div id="listarenvolvidos">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;
    var tabelaarmas = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Armas</span>
                        <span class="short-text">Armas</span>
                    </span>
                    <div id="listararmas">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;
    var tabeladrogas = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Drogas</span>
                        <span class="short-text">Drogas</span>
                    </span>
                    <div id="listardrogas">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;
    var tabeladiversos = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Objetos</span>
                        <span class="short-text">Objetos</span>
                    </span>
                    <div id="listardiversos">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;
    var tabeladocs = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Documentos</span>
                        <span class="short-text">Documentos</span>
                    </span>
                    <div id="listardocumentos">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;
    var tabelamunicoes = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Munições</span>
                        <span class="short-text">Munições</span>
                    </span>
                    <div id="listarmunicoes">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;
    var tabelaveiculos = `
    <div class="row">
        <div class="col s12 m12 l12">
            <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                    <span class="card-title">
                        <span class="full-text">Lista de Veículos</span>
                        <span class="short-text">Veículos</span>
                    </span>
                    <div id="listarveiculos">
                        <ul style="display: none;" class="collapsible black-text white row l12 m12 s12"></ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;

    function verificaAlgumaApreensaoExistente(){
        if(document.querySelector("#conteudoapreensoes") === null){
            elementoApreensoes.append(divapreensoes);
        }
    }

    $.ajax({
        url: "{% url 'ocorrencia:get_apreensoes' %}",
        type: "GET",
        data: {"ocorrencia": "{{ ocorrencia.id }}"},
        success: (data) => {
            if(data["envolvidos"]){
                verificaAlgumaApreensaoExistente();

                $("#conteudoapreensoes").append(tabelaenvolvidos);

                {% include "ocorrencia/includes/js/get_envolvidos.js" %}

                getEnvolvidos("listarenvolvidos", "{{ ocorrencia.id }}", true);
            }

            if(data["armas"]){
                verificaAlgumaApreensaoExistente();

                $("#conteudoapreensoes").append(tabelaarmas);

                {% include "ocorrencia/includes/js/get_armas.js" %}

                getArmas("listararmas", data["acessoriosocorrencia"], true);
            }

            if(data["drogas"]){
                verificaAlgumaApreensaoExistente();

                $("#conteudoapreensoes").append(tabeladrogas);

                {% include "ocorrencia/includes/js/get_drogas.js" %}

                getDrogas("listardrogas", data["acessoriosocorrencia"], true);
            }

            if(data["diversos"]){
                verificaAlgumaApreensaoExistente();
                
                $("#conteudoapreensoes").append(tabeladiversos);

                {% include "ocorrencia/includes/js/get_diversos.js" %}

                getDiversos("listardiversos", data["acessoriosocorrencia"], true);
            }

            if(data["docs"]){
                verificaAlgumaApreensaoExistente();
                
                $("#conteudoapreensoes").append(tabeladocs);

                {% include "ocorrencia/includes/js/get_documentos.js" %}

                getDocumentos("listardocumentos", data["acessoriosocorrencia"], true);
            }

            if(data["municoes"]){
                verificaAlgumaApreensaoExistente();
                
                $("#conteudoapreensoes").append(tabelamunicoes);

                {% include "ocorrencia/includes/js/get_municoes.js" %}

                getMunicoes("listarmunicoes", data["acessoriosocorrencia"], true);
            }

            if(data["veiculos"]){
                verificaAlgumaApreensaoExistente();
                
                $("#conteudoapreensoes").append(tabelaveiculos);

                {% include "ocorrencia/includes/js/get_veiculos.js" %}

                getVeiculos("listarveiculos", data["acessoriosocorrencia"], true);
            }
           $(".collapsible").collapsible();
        }
    });

    $("#apagaOcorrencia").on("click", function(event){
        event.stopPropagation();
        if(confirm("Deseja apagar essa ocorrência?")){
            $.ajax({
                url: "{% url 'ocorrencia:post_delete_ocorrencia' %}",
                type: "POST",
                data: {"ocorrencia": "{{ ocorrencia.id }}"},
                success: (response) => {
                    M.toast({html: "Ocorrência deletada com sucesso!", classes: "green", completeCallback: function(){ window.location.href = response.redirect }});
                }
            });
        } else {
            return false;
        }
    });

    $("#finalizarOcorrencia").on("click", function(event){
        event.stopPropagation();
        if(confirm("Deseja finalizar a ocorrência?")){
            $.ajax({
                url: "{% url 'ocorrencia:finalizar_ocorrencia' %}",
                type: "POST",
                data: {"ocorrencia": "{{ ocorrencia.id }}"},
                success: (response) => {
                    M.toast({html: "Ocorrência finalizada com sucesso!", classes: "green", completeCallback: function(){ window.location.href = response.redirect }});
                }
            });
        } else {
            return false;
        }
    });
});