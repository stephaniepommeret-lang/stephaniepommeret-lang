// Menu principal : une seule source de vérité (ce fichier est chargé par _layouts/default.html).
// Objectifs : utilisable au clavier, états ARIA corrects, comportement identique
// au rendu précédent en apparence.
document.addEventListener("DOMContentLoaded", function () {
    const nav = document.querySelector("header nav");
    const menuButton = document.querySelector(".menu-icon");
    const navLinks = document.getElementById("nav-links");
    const dropdownButtons = Array.from(document.querySelectorAll(".dropdown-toggle"));
    const mobile = window.matchMedia("(max-width: 768px)");

    if (!nav || !menuButton || !navLinks) return;

    function setMainMenu(open) {
        navLinks.classList.toggle("show", open);
        menuButton.setAttribute("aria-expanded", String(open));
    }

    function setDropdown(button, open) {
        const item = button.closest(".dropdown");
        if (!item) return;
        item.classList.toggle("is-open", open);
        button.setAttribute("aria-expanded", String(open));
    }

    function closeAllDropdowns() {
        dropdownButtons.forEach(function (button) { setDropdown(button, false); });
    }

    menuButton.addEventListener("click", function () {
        setMainMenu(!navLinks.classList.contains("show"));
    });

    dropdownButtons.forEach(function (button) {
        const item = button.closest(".dropdown");
        if (!item) return;

        button.addEventListener("click", function () {
            const willOpen = !item.classList.contains("is-open");
            closeAllDropdowns();
            setDropdown(button, willOpen);
        });

        // Sur desktop, le survol et le focus ouvrent le sous-menu (comme avant).
        item.addEventListener("mouseenter", function () {
            if (!mobile.matches) setDropdown(button, true);
        });

        item.addEventListener("mouseleave", function () {
            if (!mobile.matches && !item.contains(document.activeElement)) setDropdown(button, false);
        });

        item.addEventListener("focusin", function () {
            if (!mobile.matches) setDropdown(button, true);
        });

        item.addEventListener("focusout", function () {
            window.setTimeout(function () {
                if (!mobile.matches && !item.contains(document.activeElement)) setDropdown(button, false);
            }, 0);
        });
    });

    // Fermeture du menu mobile après un clic sur un lien, et mémorisation de la langue.
    navLinks.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
            if (mobile.matches) setMainMenu(false);
            closeAllDropdowns();

            const choice = link.dataset.langChoice;
            if (choice) {
                try {
                    localStorage.setItem("user_lang", choice);
                } catch (e) {
                    // Le stockage peut être bloqué : la navigation reste fonctionnelle.
                }
            }
        });
    });

    document.addEventListener("click", function (event) {
        if (!nav.contains(event.target)) closeAllDropdowns();
    });

    document.addEventListener("keydown", function (event) {
        if (event.key !== "Escape") return;

        const openButton = dropdownButtons.find(function (button) {
            return button.getAttribute("aria-expanded") === "true";
        });

        if (openButton) {
            setDropdown(openButton, false);
            openButton.focus();
        } else if (navLinks.classList.contains("show")) {
            setMainMenu(false);
            menuButton.focus();
        }
    });

    function syncViewport() {
        setMainMenu(false);
        closeAllDropdowns();
    }

    if (mobile.addEventListener) {
        mobile.addEventListener("change", syncViewport);
    } else if (mobile.addListener) {
        mobile.addListener(syncViewport);
    }
});
