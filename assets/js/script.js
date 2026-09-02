// La gestion des langues est statique, via les pages Jekyll.
// Aucune redirection JS n'est nécessaire ici.

document.addEventListener("DOMContentLoaded", function () {
    const galleryContainers = document.querySelectorAll('.gallery, .carousel-container');
    if (!galleryContainers.length) return;

    if (typeof Swiper === 'undefined') {
        // Sans Swiper, les images restent affichées les unes sous les autres (cf. CSS).
        console.error('Swiper.js non chargé : affichage statique conservé.');
        return;
    }

    const isEnglish = document.documentElement.lang === 'en';
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    galleryContainers.forEach(container => {
        // Seules les images deviennent des diapositives. Les autres enfants
        // (l'intégration Instagram du Petit Écho, par exemple) restent en place.
        const images = Array.from(container.children).filter(child => child.tagName === 'IMG');
        if (images.length === 0) return;

        container.classList.add('swiper');
        container.setAttribute('aria-label', isEnglish ? 'Image gallery' : 'Galerie d’images');

        const wrapper = document.createElement('div');
        wrapper.className = 'swiper-wrapper';

        images.forEach(img => {
            const slide = document.createElement('div');
            slide.className = 'swiper-slide';
            slide.appendChild(img);
            wrapper.appendChild(slide);
        });

        // On insère la galerie en tête, sans effacer le reste du conteneur.
        const trailingContent = container.firstElementChild;
        container.insertBefore(wrapper, trailingContent);

        const pagination = document.createElement('div');
        pagination.className = 'swiper-pagination';
        container.insertBefore(pagination, trailingContent);

        const nextButton = document.createElement('button');
        nextButton.type = 'button';
        nextButton.className = 'swiper-button-next';
        container.insertBefore(nextButton, trailingContent);

        const prevButton = document.createElement('button');
        prevButton.type = 'button';
        prevButton.className = 'swiper-button-prev';
        container.insertBefore(prevButton, trailingContent);

        new Swiper(container, {
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
            keyboard: {
                enabled: true,
                onlyInViewport: true,
            },
            a11y: {
                enabled: true,
                prevSlideMessage: isEnglish ? 'Previous image' : 'Image précédente',
                nextSlideMessage: isEnglish ? 'Next image' : 'Image suivante',
            },
        });
    });
});
