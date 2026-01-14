document.addEventListener("DOMContentLoaded", function () {
    const headerHtml = `
    <div class="logo">
        <h1><a href="index.html">Stéphanie Pommeret</a></h1>
        <p>Plasticienne / Poètesse / Photographe</p>
    </div>
    <nav>
        <div class="menu-icon" onclick="toggleMenu()">☰</div>
        <ul id="nav-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="cv.html">CV</a></li>
            <li class="dropdown">
                <a href="#">Expositions</a>
                <div class="dropdown-content">
                    <a href="huisclos.html">Huis Clos</a>
                    <a href="lepetitechodelamode.html">Le Petit Echo de la Mode</a>
                    <a href="paradise.html">Paradise</a>
                    <a href="collectioncartedumonde.html">Collection de carte du monde</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="#">Résidences</a>
                <div class="dropdown-content">
                    <a href="saotome.html">Sao Tomé</a>
                    <a href="casablanca.html">Casablanca</a>
                    <a href="inde.html">Inde</a>
                    <a href="centrebretagne.html">Centre Bretagne</a>
                    <a href="maroc.html">Maroc</a>
                </div>
            </li>
            <li class="dropdown">
                <a href="#">Séries photographies</a>
                <div class="dropdown-content">
                    <a href="toutesmigrantes.html">Tout.e.s migrant.e.s</a>
                    <a href="habiterlaforet.html">Habiter la forêt</a>
                    <a href="confinement.html">Confinement</a>
                </div>
            </li>
        </ul>
    </nav>
    `;

    const headerEl = document.querySelector('header');
    if (!headerEl.innerHTML.trim()) {
        headerEl.innerHTML = headerHtml;
    }

    // Highlight active link based on current URL
    const currentPage = window.location.pathname.split("/").pop() || "index.html";
    const links = document.querySelectorAll('#nav-links a');

    links.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
            // Also underscore the parent dropdown if it's a dropdown item
            const parentDropdown = link.closest('.dropdown');
            if (parentDropdown) {
                parentDropdown.querySelector('a').classList.add('active');
            }
        }
    });
});

function toggleMenu() {
    var navLinks = document.getElementById("nav-links");
    navLinks.classList.toggle("show");
}
