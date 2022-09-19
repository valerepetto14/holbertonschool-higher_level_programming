document.addEventListener("DOMContentLoaded", function() {
    $("INPUT#btn_translate").click(function(){
        $.get(`https://stefanbohacek.com/hellosalut/?lang=${$("INPUT#language_code").val()}`,function(data){
            $("DIV#hello").text(data.hello)
        })
    })
});