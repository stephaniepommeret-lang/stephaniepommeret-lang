document.addEventListener("DOMContentLoaded", function () {
    const footerHtml = `
        <div class="social-icons">
            <a href="https://www.facebook.com/stephanie.pommeret" target="_blank" aria-label="Facebook"><img
                    src="images/facebook.png" alt="Facebook" width="25" height="25"></a>
            <a href="https://www.instagram.com/stephaniepommeret/" target="_blank" aria-label="Instagram"><img
                    src="images/instagram.png" alt="Instagram" width="25" height="25"></a>
        </div>
        <div class="contact-info">
            <p>Coordonnée / Coordinated : <a href="mailto:stephaniepommeret@hotmail.fr">stephaniepommeret@hotmail.fr</a>
            </p>
            <p>&copy; 2024 Stéphanie Pommeret.</p>
        </div>
    `;

    const footerEl = document.querySelector('footer');
    if (footerEl) {
        footerEl.innerHTML = footerHtml;
    }
});
