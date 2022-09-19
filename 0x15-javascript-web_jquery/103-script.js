document.addEventListener("DOMContentLoaded", function() {
    $("INPUT#btn_translate").click(function(){
        $.get(`https://stefanbohacek.com/hellosalut/?lang=${$("INPUT#language_code").val()}`,function(data){
            $("DIV#hello").text(data.hello)
        })
    })
    $('INPUT#language_code').keypress(function(e) {
        if(e.keyCode == 13) {
            e.preventDefault(); // Stop the default behaviour
            $('INPUT#btn_translate').click();
        }
    });
});