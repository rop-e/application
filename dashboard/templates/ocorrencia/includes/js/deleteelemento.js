// função para deletar elemento genérico
function deleteelemento(elemento, url, append){
    if(confirm("Deseja mesmo excluir esse elemento?") == true){
        $.ajax({
            url: url,
            type: "POST",
            data: {"id": $(elemento).data("id")},
            success: function(data){
                // alert(data["message"]);
                M.toast({html: data["message"], classes: "green"});
                removeelemento(elemento, append);
            }
        });
    } else {
        event.stopPropagation();
    }
}

function removeelemento(elemento, append){
    var UL = $(elemento).parents()[2];
    var LICount = $(UL).find("li").length;

    if(LICount === 1){
        var DIV = $(elemento).parents()[3];
        $(DIV).append(append);
        UL.style.display = "none";
        $(elemento).parents()[0].remove();
    } else {
        $(elemento).parents()[1].remove();
    }
}