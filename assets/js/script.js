// Galeries d'images (Swiper). Sans JavaScript, ou si Swiper ne se charge pas,
// les images restent affichées les unes sous les autres (cf. _sass/site.scss).
//
// Toutes les galeries se trouvent sous l'image principale : Swiper (script et
// CSS) n'est donc demandé qu'une fois la page chargée — l'image principale a
// alors toute la bande passante — ou dès que le lecteur commence à défiler.
const swiperAssets = document.currentScript ? document.currentScript.dataset : {};
let swiperReady = null;

function loadSwiper() {
    if (swiperReady) return swiperReady;

    const stylesheet = new Promise(function (resolve) {
        if (!swiperAssets.swiperCss) return resolve();
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = swiperAssets.swiperCss;
        link.addEventListener('load', resolve, { once: true });
        link.addEventListener('error', resolve, { once: true });
        document.head.appendChild(link);
    });

    const library = new Promise(function (resolve, reject) {
        if (typeof Swiper !== 'undefined') return resolve();
        if (!swiperAssets.swiperJs) return reject(new Error('chemin de Swiper absent'));
        const script = document.createElement('script');
        script.src = swiperAssets.swiperJs;
        script.addEventListener('load', resolve, { once: true });
        script.addEventListener('error', reject, { once: true });
        document.head.appendChild(script);
    });

    swiperReady = Promise.all([stylesheet, library]);
    return swiperReady;
}

function afterLoadOrFirstInteraction(callback) {
    let started = false;
    const start = function () {
        if (started) return;
        started = true;
        callback();
    };
    if (document.readyState === 'complete') return start();
    window.addEventListener('load', start, { once: true });
    ['scroll', 'pointerdown', 'keydown'].forEach(function (type) {
        window.addEventListener(type, start, { once: true, passive: true });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    const galleryContainers = document.querySelectorAll('.gallery, .carousel-container');
    if (!galleryContainers.length) return;

    afterLoadOrFirstInteraction(function () {
        loadSwiper()
            .then(function () { initGalleries(galleryContainers); })
            .catch(function () { console.error('Swiper non chargé : affichage statique conservé.'); });
    });
});

function initGalleries(galleryContainers) {

    const isEnglish = document.documentElement.lang === 'en';
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const text = isEnglish ? {
        gallery: 'Image gallery',
        carousel: 'carousel',
        slide: 'slide',
        slideLabel: 'Image {{index}} of {{slidesLength}}',
        previous: 'Previous image',
        next: 'Next image',
        bullet: 'Go to image {{index}}',
    } : {
        gallery: 'Galerie d’images',
        carousel: 'carrousel',
        slide: 'diapositive',
        slideLabel: 'Image {{index}} sur {{slidesLength}}',
        previous: 'Image précédente',
        next: 'Image suivante',
        bullet: 'Aller à l’image {{index}}',
    };

    galleryContainers.forEach(container => {
        // Seules les images deviennent des diapositives ; les autres enfants
        // éventuels restent en place, après le carrousel.
        const images = Array.from(container.children).filter(child => child.tagName === 'IMG');
        if (images.length === 0) return;

        container.classList.add('swiper');

        const wrapper = document.createElement('div');
        wrapper.className = 'swiper-wrapper';

        images.forEach(img => {
            const slide = document.createElement('div');
            slide.className = 'swiper-slide';
            slide.appendChild(img);
            wrapper.appendChild(slide);
        });

        // Ordre du DOM = ordre de tabulation : précédent, suivant, puces.
        const trailingContent = container.firstElementChild;
        container.insertBefore(wrapper, trailingContent);

        const prevButton = document.createElement('button');
        prevButton.type = 'button';
        prevButton.className = 'swiper-button-prev';
        container.insertBefore(prevButton, trailingContent);

        const nextButton = document.createElement('button');
        nextButton.type = 'button';
        nextButton.className = 'swiper-button-next';
        container.insertBefore(nextButton, trailingContent);

        const pagination = document.createElement('div');
        pagination.className = 'swiper-pagination';
        container.insertBefore(pagination, trailingContent);

        const swiper = new Swiper(container, {
            loop: images.length > 1,
            rewind: images.length <= 1,
            speed: reducedMotion ? 0 : 600,
            autoHeight: true,
            watchOverflow: true,
            pagination: {
                el: pagination,
                clickable: true,
            },
            navigation: {
                nextEl: nextButton,
                prevEl: prevButton,
            },
            // Le clavier est géré plus bas, carrousel par carrousel : le
            // module de Swiper ferait défiler toutes les galeries visibles.
            keyboard: { enabled: false },
            a11y: {
                enabled: true,
                containerMessage: text.gallery + ' (' + images.length + ')',
                containerRoleDescriptionMessage: text.carousel,
                itemRoleDescriptionMessage: text.slide,
                slideLabelMessage: text.slideLabel,
                prevSlideMessage: text.previous,
                nextSlideMessage: text.next,
                firstSlideMessage: text.previous,
                lastSlideMessage: text.next,
                paginationBulletMessage: text.bullet,
                slideRole: 'group',
            },
        });

        // Le carrousel est une région nommée, atteignable au clavier :
        // flèches gauche/droite, Début et Fin quand il a le focus.
        container.setAttribute('role', 'region');
        if (!container.hasAttribute('tabindex')) container.tabIndex = 0;

        container.addEventListener('keydown', event => {
            if (event.altKey || event.ctrlKey || event.metaKey) return;
            const keys = {
                ArrowLeft: () => swiper.slidePrev(),
                ArrowRight: () => swiper.slideNext(),
                Home: () => swiper.slideToLoop(0),
                End: () => swiper.slideToLoop(images.length - 1),
            };
            const action = keys[event.key];
            if (!action) return;
            event.preventDefault();
            action();
        });
    });
}
