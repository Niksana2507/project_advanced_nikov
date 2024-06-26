// Dropdown хамбургер
const toggleBtn = document.querySelector('.hamburger')
const toggleBtnIcon = document.querySelector('.hamburger i')
const dropDownMenu = document.querySelector('.dropdown')

toggleBtn.onclick = function() {
    dropDownMenu.classList.toggle('open')
    const isOpen = dropDownMenu.classList.contains('open')

    toggleBtnIcon.classList = isOpen
        ? 'fa-solid fa-xmark'
        : 'fa-solid fa-bars'
}




//Анимация на текст в заглавната страница
let TxtType = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};
 
TxtType.prototype.tick = function() {
    let i = this.loopNum % this.toRotate.length;
    let fullTxt = this.toRotate[i];

    if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

    let that = this;
    let delta = 200 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
    }

    setTimeout(function() {
    that.tick();
    }, delta);
};

function addText() {
    let elements = document.getElementsByClassName('typewrite');
    for (let i=0; i<elements.length; i++) {
        let toRotate = elements[i].getAttribute('datatype');
        let period = elements[i].getAttribute('dataperiod');
        if (toRotate) {
          new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }

    let css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
    document.body.appendChild(css);
};


// Изчисление за показване на галерията
let perPage = 3;

        const perPageRestrictions = {
            '-1200': 2,
            '-650': 1,
        };

        for (const [width, elementsOnDisplay] of Object.entries(perPageRestrictions)) {
            if (window.innerWidth <= Number(Math.abs(width))) {
                perPage = elementsOnDisplay;
            }
        }
    

        // Конфигурация за splide
        const splide = new Splide('.splide', {
            type: 'loop',
            drag: 'free',
            focus: 'center',
            snap: true,
            perPage: perPage,
            autoScroll: {
                speed: 1,
            },
        });

        splide.mount(window.splide.Extensions);

// Хамбургер меню за телефон
document.addEventListener("DOMContentLoaded", function () {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const mobileNav = document.getElementById("mobileNav");

    hamburgerMenu.addEventListener("click", function () {
        this.classList.toggle("active"); 
        mobileNav.classList.toggle("active"); 
    });
});
