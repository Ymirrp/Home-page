// document.getElementById('menu-btn').addEventListener('click', ev => {
//     let navbar = document.getElementById('navbar');
//     let btns = document.querySelector('nav-btns');
//     let txts = document.getElementsByClassName('menu-txt');
//
//     navbar.style.width = "10em";
// });

function expand_nav() {
    let i;
    let navbar = document.getElementById('navbar');
    let btns = document.querySelector('.nav-btns');
    let txts = document.getElementsByClassName('menu-txt');

    if (navbar.className.search("expand") === -1) {
        console.log("expanding...");
        navbar.style.textAlign = 'left';
        navbar.classList.toggle("expand");
        setTimeout(() => {
            for (i=0; i<txts.length; i++) {
                txts[i].classList.toggle("hidden");
            }
        }, 300);

    }
    else {
        console.log("closing...");
        setTimeout(() => {
            navbar.classList.toggle("expand");
            navbar.style.textAlign = 'center';
        }, 100);
        for (i=0; i<txts.length; i++) {
            txts[i].classList.toggle("hidden");
        }


    }

}