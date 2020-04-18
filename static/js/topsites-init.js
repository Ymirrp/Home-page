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
    // let year = date.getUTCFullYear().toString();
    let fulldate = weekdays[weekd] + ", " + day + ". " + months[month]/* + " '" + year.slice(2, year.length)*/;
    // console.log(fulldate);
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

    // let modal = '<div class="delete-wrapper" id="delbox-"' + s_id + '>' +
    //     '<span>Ertu viss að þú viljir eyða þessa síðu?</span>' +
    //     '<input type="submit" value="Eyða">' +
    //     '<button onclick="close_del(' + s_id + ')">Hætta við</button>' +
    //     '</div>';
    // $("#delete-confirmation").innerHTML = modal;
    // $("#delete-confirmation").html('<div class="delete-wrapper" id="delbox-"' + s_id + '>' +
    //     '<span>Ertu viss að þú viljir eyða þessa síðu?</span>' +
    //     '<input type="submit" value="Eyða">' +
    //     '<button onclick="close_del(' + s_id + ')">Hætta við</button>' +
    //     '</div>');
    $(".site-title").each(function() {
        let title_len = $(this).text().length;
        // console.log($(this).text() + ": " + title_len);
        if (title_len > 20 && title_len <= 48) {
            $(this).css("font-size", "1em");
            $(this).css("margin-top", "0.65em");
        }
        else if (title_len > 48) {
            $(this).css("font-size", "0.8em");
            $(this).css("margin-top", "0.8em");
        }
    });
});