$(document).ready(function(){
    $('.timepicker').timepicker({
        i18n: {
            cancel: 'Cancelar',
            clear: 'Limpar',
            done: 'Ok'
        },
        default: 'now',
        vibrate: true,
        twelveHour : false,
        autoclose: false,
    });
});