
function expand_nav() {
    let i;
    let navbar = document.getElementById('navbar');
    let menu_btn = document.getElementById("menu-btn");
    let btns = document.querySelector('.nav-btns');
    let txts = document.getElementsByClassName('menu-txt');

    if (navbar.className.search("expand") === -1) {
        navbar.style.textAlign = 'left';
        menu_btn.classList.replace("fa-bars", "fa-times");
        navbar.classList.toggle("expand");
        setTimeout(() => {
            for (i=0; i<txts.length; i++) {
                txts[i].classList.toggle("hidden");
            }
        }, 300);

    }
    else {
        setTimeout(() => {
            menu_btn.classList.replace("fa-times", "fa-bars");
            navbar.classList.toggle("expand");
            navbar.style.textAlign = 'center';
        }, 100);
        for (i=0; i<txts.length; i++) {
            txts[i].classList.toggle("hidden");
        }


    }

}