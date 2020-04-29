$(document).ready(() => {
    var i;
    const weekdays = [
        "Sunnudagur",
        "Mánudagur",
        "Þriðjudagur",
        "Miðvikudagur",
        "Fimmtudagur",
        "Föstudagur",
        "Laugardagur"
    ]
    const months = [
        "janúar",
        "febrúar",
        "mars",
        "apríl",
        "maí",
        "júní",
        "júlí",
        "ágúst",
        "september",
        "október",
        "nóvember",
        "desember"
    ]
    let date = new Date();
    let weekd = date.getUTCDay();
    let day = date.getUTCDate().toString();
    let month = date.getUTCMonth();
    let fulldate = weekdays[weekd] + ", " + day + ". " + months[month]/* + " '" + year.slice(2, year.length)*/;
    $("#date").text(fulldate);

    let btn_id = $(".btn").first().attr('id').toString();
    let cat_code = btn_id.slice(4, btn_id.length);
    $("#"+btn_id).addClass("selected");
    $(".category").first().css("margin-right", "4.35em");
    $("#"+btn_id).children("span").removeClass("d-none");
    $("#site-"+cat_code).removeClass("hidden");

    let el = $(".site-wrapper ul");
    for (i=0; i<el.length; i++) {
        if (el[i].children.length == 0) {
            $(".site-wrapper")[i].innerHTML = "<ul><li>Empty</li></ul>"
        }
    }

    $(".site-title").each(function() {
        let title_len = $(this).text().length;
        if (title_len > 20 && title_len <= 48) {
            $(this).css("font-size", "1em");
            $(this).css("margin-top", "0.65em");
        }
        else if (title_len > 48) {
            $(this).css("font-size", "0.8em");
            $(this).css("margin-top", "0.8em");
        }
    });
    function getWeather() {
        if (!navigator.geolocation) {
            console.log("No support");
        } else {
            navigator.geolocation.getCurrentPosition((location) => {
                console.log(`Lat: ${location.coords.latitude}, Lon: ${location.coords.longitude}`);
                $.ajax({
                    url: '/weather/',
                    method: 'GET',
                    data: 'lat='+location.coords.latitude+'&lon='+location.coords.longitude,
                    success: (res) => {
                        console.log(res);
                        $("#weather").html(
                            `<span id="w-temp">${res.temp}&deg;</span>` +
                            `<span id="w-weather">${res.weather}</span>` +
                            `<img id="w-icon" src="${res.icon}">` +
                            `<span id="w-wind">${res.wind}m/s ${res.deg}</span>` +
                            // `<span id="w-deg">${res.deg}</span>` +
                            `<span id="location">&#128205; <span id="w-city">${res.city}</span></span>`
                        )
                }})
            })
        }
    }
    getWeather();
});