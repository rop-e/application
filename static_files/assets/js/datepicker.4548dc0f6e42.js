var i18n_datepicker = {
    today: 'Hoje',
    cancel: 'Cancelar',
    clear: 'Limpar',
    done: 'Ok',
    nextMonth: 'Próximo mês',
    previousMonth: 'Mês anterior',
    weekdaysAbbrev: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
    weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
    weekdays: ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado'],
    monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
}

$(document).ready(function(){
    $('.datepicker').datepicker({
        container: 'body',
        showDaysInNextAndPreviousMonths: true,
        format: 'dd/mm/yyyy',
        i18n: i18n_datepicker,
        yearRange: ['1900', (new Date).getFullYear()],
        autoclose: false
    });
});