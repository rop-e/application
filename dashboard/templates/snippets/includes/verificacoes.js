$.ajax({
    url: "{% url 'ocorrencia:verifica_ocorrencia_nao_finalizada' %}",
    success: (response) => {
        if(response["pendentes"] !== 0){
            $("#HeaderMenuCriminal").append(`<span class="new badge red" data-badge-caption="pendentes">${response["pendentes"]}</span>`);

            $("#MenuCriminal").append(`
                <li>
                    <a class="waves-effect" href="{% url 'ocorrencia:listar_ocorrencias_sem_finalizar' %}">
                        <span class="new badge red" data-badge-caption="sem finalizar">${response["pendentes"]}</span>
                        <i class="material-icons">priority_high</i>Pendentes
                    </a>
                </li>
            `);
        }
    }
});
$.ajax({
    url: "{% url 'rat:verifica_rat_nao_finalizada' %}",
    success: (response) => {
        if(response["pendentes"] !== 0){
            $("#HeaderMenuRAT").append(`<span class="new badge red" data-badge-caption="pendentes">${response["pendentes"]}</span>`);

            $("#MenuRAT").append(`
                <li>
                    <a class="waves-effect" href="{% url 'rat:listar_rats_sem_finalizar' %}">
                        <span class="new badge red" data-badge-caption="sem finalizar">${response["pendentes"]}</span>
                        <i class="material-icons">priority_high</i>Pendentes
                    </a>
                </li>
            `);
        }
    }
});
$.ajax({
    url: "{% url 'guarnicao:ajax_verifica_guarnicao_ativa' %}",
    success: (response) => {
        if(response["ativa"]){
            $("#menuGuarnicao").append(`<span class="new badge" data-badge-caption="aberto"></span>`);
        }
    }
});
$.ajax({
    url: "{% url 'opo:checa_menuopo' %}",
    method: "GET",
    success: (response) => {
        switch (response["tipo"]) {
            case "coordenadordearea":
                $(".header-opo").append(`<sup>COORD. ÁREA</sup>`);
                $(".opo").css("display", "block");

                if(response["opo"] !== 0){
                    $(".header-opo").append(`<span class="new badge red" data-badge-caption="novos">${response["opo"]}</span>`);
                }

                $("#OPOMenu").append(`
                    <li>
                        <a class="waves-effect" href="{% url 'opo:listar' %}">
                            <i class="material-icons">list</i>Listar
                        </a>
                    </li>
                `);
                if(response["andamento"] !== 0){
                    $("#OPOMenu").append(`
                        <li>
                            <a class="waves-effect" href="{% url 'opo:listar' %}?status=andamento">
                                <i class="material-icons">priority_high</i>Em andamento
                                <span class="new badge red" data-badge-caption="novos">${response["andamento"]}</span>
                            </a>
                        </li>
                    `);
                }
                break;
            case "cicom":
                $(".header-opo").append(`<sup>CICOM</sup>`);
                $(".opo").css("display", "block");

                if(response["opo"] !== 0){
                    $(".header-opo").append(`<span class="new badge red" data-badge-caption="novos">${response["opo"]}</span>`);
                }

                $("#OPOMenu").append(`
                    <li>
                        <a class="waves-effect" href="{% url 'opo:listar' %}">
                            <i class="material-icons">list</i>Listar
                        </a>
                    </li>
                `);
                if(response["andamento"] !== 0){
                    $("#OPOMenu").append(`
                        <li>
                            <a class="waves-effect" href="{% url 'opo:listar' %}?status=andamento">
                                <i class="material-icons">priority_high</i>Em andamento
                                <span class="new badge red" data-badge-caption="novos">${response["andamento"]}</span>
                            </a>
                        </li>
                    `);
                }
                break;
            case "comandantecia":
                $(".header-opo").append(`<sup>COMANDANTE CIA</sup>`);
                $(".opo").css("display", "block");

                if(response["opo"] !== 0){
                    $(".header-opo").append(`<span class="new badge red" data-badge-caption="novos">${response["opo"]}</span>`);
                }

                $("#OPOMenu").append(`
                    <li>
                        <a class="waves-effect" href="{% url 'opo:listar' %}">
                            <i class="material-icons">list</i>Listar
                        </a>
                    </li>
                `);
                if(response["andamento"] !== 0){
                    $("#OPOMenu").append(`
                        <li>
                            <a class="waves-effect" href="{% url 'opo:listar' %}?status=andamento">
                                <i class="material-icons">priority_high</i>Em andamento
                                <span class="new badge red" data-badge-caption="novos">${response["andamento"]}</span>
                            </a>
                        </li>
                    `);
                }
                break;
            case "policial":
                if(response["opo"] !== 0){
                    $(".opo").css("display", "block");
                    $(".header-opo").append(`<span class="new badge red" data-badge-caption="novos">${response["opo"]}</span>`);
                    $(".header-opo").append(`<sup>POLICIAL</sup>`);
                }
                if(response["andamento"]){
                    $("#OPOMenu").append(`
                        <li>
                            <a class="waves-effect" href="{% url 'opo:listar_policial' %}?status=andamento">
                                <i class="material-icons">priority_high</i>Andamento
                                <span class="new badge red" data-badge-caption="novos">${response["andamento"]}</span>
                            </a>
                        </li>
                    `);
                }
                if(response["pendente"]){
                    $("#OPOMenu").append(`
                        <li>
                            <a class="waves-effect" href="{% url 'opo:listar_policial' %}?status=pendente">
                                <i class="material-icons">priority_high</i>Pendentes
                                <span class="new badge red" data-badge-caption="novos">${response["pendente"]}</span>
                            </a>
                        </li>
                    `);
                }
                break;
        }
    }
});