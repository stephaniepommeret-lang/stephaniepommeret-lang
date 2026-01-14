// function toggleMenu() removed - handled in menu.js

document.addEventListener("DOMContentLoaded", function () {
    const carousels = document.querySelectorAll('.carousel-container');

    carousels.forEach(container => {
        const images = container.querySelectorAll('img');
        if (images.length === 0) return;

        let currentIndex = 0;
        images[currentIndex].classList.add('active');

        const prevBtn = document.createElement('button');
        prevBtn.innerHTML = '&#10094;';
        prevBtn.className = 'carousel-btn prev-btn';

        const nextBtn = document.createElement('button');
        nextBtn.innerHTML = '&#10095;';
        nextBtn.className = 'carousel-btn next-btn';

        container.appendChild(prevBtn);
        container.appendChild(nextBtn);

        function showImage(index) {
            images[currentIndex].classList.remove('active');
            currentIndex = (index + images.length) % images.length;
            images[currentIndex].classList.add('active');
        }

        prevBtn.addEventListener('click', () => showImage(currentIndex - 1));
        nextBtn.addEventListener('click', () => showImage(currentIndex + 1));

        // Auto-play (optional)
        setInterval(() => showImage(currentIndex + 1), 5000);
    });
});
