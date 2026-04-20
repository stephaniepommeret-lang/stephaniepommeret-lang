// Language handling is now static via Jekyll pages.
// No JS redirection needed for now.

// Swiper Initialization
document.addEventListener("DOMContentLoaded", function () {
    // Check if Swiper is loaded
    if (typeof Swiper === 'undefined') {
        console.error('Swiper.js not loaded');
        return;
    }

    // Initialize Swiper for .gallery and .carousel-container
    // We add the 'swiper' class to these containers first
    const galleryContainers = document.querySelectorAll('.gallery, .carousel-container');

    galleryContainers.forEach(container => {
        container.classList.add('swiper');

        // Wrap all direct children (images) in a swiper-wrapper and then swiper-slide
        const images = Array.from(container.children).filter(child => child.tagName === 'IMG');

        if (images.length === 0) return;

        const wrapper = document.createElement('div');
        wrapper.className = 'swiper-wrapper';

        images.forEach(img => {
            const slide = document.createElement('div');
            slide.className = 'swiper-slide';

            // Move image into slide
            slide.appendChild(img);
            wrapper.appendChild(slide);
        });

        // Clear container and append wrapper
        container.innerHTML = '';
        container.appendChild(wrapper);

        // Add pagination and navigation
        const pagination = document.createElement('div');
        pagination.className = 'swiper-pagination';
        container.appendChild(pagination);

        const nextButton = document.createElement('div');
        nextButton.className = 'swiper-button-next';
        container.appendChild(nextButton);

        const prevButton = document.createElement('div');
        prevButton.className = 'swiper-button-prev';
        container.appendChild(prevButton);

        // Initialize Swiper instance
        new Swiper(container, {
            loop: true,
            speed: 600,
            autoHeight: true, // Adjust height to the current slide
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
            },
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
        });
    });
});
