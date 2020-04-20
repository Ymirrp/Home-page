document.querySelector("input").addEventListener("invalid", ev => {
    ev.preventDefault();
});

document.addEventListener("click", (e) => {
   let target = e.target;
   let menus = document.getElementsByClassName("menu");
   let menu;
   for (let i=0; i<menus.length; i++) {
       if (menus[i].style.display === "block") {
           menu = menus[i];
           break;
       }
   }

   if (menu !== undefined && target.className.search("edit") === -1 ) {
       do {
           if (target == menu) {
               return;
           }
           target = target.parentNode;
       } while (target);
       menu.style.display = "none";
   }

});

function openTab(cat) {
    var i;
    let wrappers = document.getElementsByClassName('site-wrapper');
    let tabs = document.getElementsByClassName("btn");
    let cats = document.getElementsByClassName("category");
    document.getElementById("addsite-popup").style.display = "none";
    for (i=0; i<cats.length; i++) {
        if (cats[i].children[0].className.search(" selected") > 0) {
            cats[i].style.marginRight = "0.1em";
        }
        // if (cats[i].id === "cat-ADD") {
        //     cats[i].style.marginRight = 0;
        // }
    }
    for (i=0; i<wrappers.length; i++) {
        if (wrappers[i].className.search(" hidden") < 0) {
            wrappers[i].className += " hidden";
        }
    }
    for (i=0; i<tabs.length; i++) {
        tabs[i].children.item(1).className = "d-none";
        tabs[i].className = tabs[i].className.replace(" selected", '');
    }
    document.getElementById("site-"+cat).className = "site-wrapper";
    document.getElementById("btn-"+cat).className += " selected";
    document.getElementById("btn-"+cat).children.item(1).className = "";
    for (i=0; i<cats.length; i++) {
        if (cats[i].children[0].className.search(" selected") > 0) {
            cats[i].style.marginRight = "4.35em";
        }
        // if (cats[i].id === "cat-ADD") {
        //     cats[i].style.marginRight = "3.8em";
        // }
    }
    // if (cat === "ADD") {
    //     let options = document.getElementById("site-cat").children;
    //     console.log(options);
    //     for (i=0; i<options.length; i++) {
    //         options[i].removeAttribute("selected")
    //     }
    //     options[9].setAttribute("selected", '');
    // }
}

function add_site(cat) {
    // TODO: Fix options selected changes under #cat-ADD tab
    let container = document.getElementById("addsite-popup");
    container.style.display = "block";
    let options = document.getElementsByTagName("select")[1]
    for (let i=0; i<options.length; i++) {
        if (options[i].getAttribute("selected") !== null) {
            options[i].removeAttribute("selected");
        }
        if (options[i].getAttribute("value") === cat) {
            options[i].setAttribute("selected", "");
        }
    }
}

function close_form() {
    console.log("close");
    document.getElementById("addsite-popup").style.display = "none";
}

function open_menu(s_id) {
    let menus = document.getElementsByClassName("menu");
    for (let i=0; i<menus.length; i++) {
        menus[i].style.display = "none"
    }
    document.getElementById("menu-"+s_id).style.display = "block";
}

function close_menu(s_id) {
    document.getElementById("menu-"+s_id).style.display = "none";
}



function confirm_del(s_id) {
    // let host = window.location.hostname;
    // let port = window.location.port.toString();
    // if (port !== '') {
    //     port = ':' + port;
    // }
    let modal = '<div class="delete-wrapper" id="delbox-' + s_id + '">' +
        '<span class="fas fa-exclamation-circle alert-icon"></span>' +
        '<span class="del-msg">Ertu viss að þú viljir eyða þessa síðu?</span>' +
        '<button class="confirm_del-btn" onclick="del_site(' + s_id + ')">Eyða</button>' +
        '<button class="close_del-btn" onclick="close_del(' + s_id + ')">Hætta við</button>' +
        '</div>';
    // '<a href="/del/' + s_id + '"><button class="confirm_del-btn">Eyða</button></a>' +
    let elem = document.getElementById("delete-container");
    elem.innerHTML = modal;
    elem.style.display = "block"
}
function close_del() {
    let elem = document.getElementById("delete-container");
    elem.style.display = "none";
    elem.innerHTML = '';
    // return null;
}

function del_site(s_id) {
    let xhttp = new XMLHttpRequest();
    let csrftoekn = getCookie('csrftoken');
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log("Síðan hefur verið fjarlægð");
            let snackbar = document.getElementById("snackbar");
            snackbar.innerText = "Síðan hefur verið fjarlægð";
            snackbar.className = "show";
            document.getElementById("delete-container").style.display = "none";
            setTimeout(() => {
                snackbar.className = snackbar.className.replace("show", '');
                snackbar.innerText = '';
            }, 3000);
            window.location.reload()
        }
    };
    xhttp.open('DELETE', '/del/'+s_id, true);
    xhttp.setRequestHeader("X-CSRFToken", csrftoekn);
    xhttp.send();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function switch_cont() {
    let cont1 = document.getElementById("cont1");
    let cont2 = document.getElementById("cont2");
    cont1.classList.toggle("hidden");
    cont1.addEventListener('invalid', e => {
        e.preventDefault();
    }, true);
    cont2.classList.toggle("hidden");
    cont2.addEventListener('invalid', e => {
        e.preventDefault();
    }, true);
}

// api: api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c5d83ac177a5989b9d9ee9f886892237
// apiKey: c5d83ac177a5989b9d9ee9f886892237

// function getLocation() {
//     function success(pos) {
//         const lon = pos.coords.longitude;
//         const lat = pos.coords.latitude;
//         console.log(`Latitude ${lat}, Longitude: ${lon}`);
//     }
//     function error() {
//         console.log("Error");
//     }
//     if (!navigator.geolocation) {
//         console.log("No support");
//     } else {
//         navigator.geolocation.getCurrentPosition(success, error)
//     }
// }