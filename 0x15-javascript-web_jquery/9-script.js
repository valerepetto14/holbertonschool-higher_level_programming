// $.ajax({
//     type: "POST",
//     url: "https://fourtonfish.com/hellosalut/?lang=fr",
//     dataType: "html",
//     success: function (result) {
//         console.log(result)
//     },
//     error: function (xhr, status, err) {
//         console.error(status);
//     }
// });

$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function(data){
    console.log(data.hello)
})