//navbar
document.addEventListener('DOMContentLoaded', function(){
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
  });


//sidebar 
document.addEventListener('DOMContentLoaded', function(){
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});


//select
document.addEventListener('DOMContentLoaded', function(){
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

document.addEventListener("DOMContentLoaded",function(){
	var elems = document.querySelectorAll('.datepicker');
	elems.length&&(datepickerOptions.format=get_format('DATE_INPUT_FORMATS')[0].replace("%Y","yyyy").replace("%m","mm").replace("%d","dd"),M.Datepicker.init(e,datepickerOptions));
	var t = document.querySelectorAll('.timepicker');
	t.length && M.Timepicker.init(t,timeOptions)
});