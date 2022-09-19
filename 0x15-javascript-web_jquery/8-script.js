$.get("https://swapi-api.hbtn.io/api/films/?", function (data)  {
    for (let i of data.results){
        $("UL#list_movies").append(`<li>${i.title}</li>`)
    }
})