// Améliorations discrètes appliquées sur toutes les pages.
// Tout est progressif : sans JavaScript, la page reste complète et lisible.
document.addEventListener("DOMContentLoaded", function () {

    /* ------------------------------------------------------------------
       1. Typographie française
       Les fichiers source sont écrits avec des apostrophes droites et des
       espaces ordinaires, pour rester simples à éditer. On applique ici les
       règles typographiques françaises à l'affichage uniquement : espaces
       insécables avant la ponctuation double, apostrophes courbes, guillemets.
       ------------------------------------------------------------------ */
    const lang = (document.documentElement.lang || "fr").toLowerCase();

    if (lang.startsWith("fr")) {
        const main = document.querySelector("main");

        if (main) {
            const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, {
                acceptNode: function (node) {
                    const parent = node.parentElement;
                    if (!parent) return NodeFilter.FILTER_REJECT;
                    if (parent.closest("script, style, code, pre, textarea, [data-no-typography]")) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    return NodeFilter.FILTER_ACCEPT;
                },
            });

            const nodes = [];
            while (walker.nextNode()) nodes.push(walker.currentNode);

            nodes.forEach(function (node) {
                const value = node.nodeValue;
                // On laisse tranquilles les adresses et les URL.
                if (/https?:\/\/|\S+@\S+/.test(value)) return;

                node.nodeValue = value
                    // Guillemets droits -> guillemets français avec espaces fines.
                    .replace(/"([^"\n]+)"/g, "« $1 »")
                    // Apostrophe droite entre deux lettres -> apostrophe courbe.
                    .replace(/(\p{L})'(\p{L})/gu, "$1’$2")
                    // Espace fine insécable avant ; ! ?
                    .replace(/(\S)[   ]*([;!?])/g, "$1 $2")
                    // Espace insécable avant les deux-points.
                    .replace(/(\S)[   ]*:(\s|$)/g, "$1 :$2")
                    // Espaces à l'intérieur des guillemets déjà présents.
                    .replace(/«[   ]*/g, "« ")
                    .replace(/[   ]*»/g, " »");
            });
        }
    }

    /* ------------------------------------------------------------------
       2. Images : chargement différé et apparition en fondu
       L'image principale de chaque page (fetchpriority="high") est exclue :
       elle doit rester immédiate, c'est elle qui porte le LCP.
       ------------------------------------------------------------------ */
    document.querySelectorAll("main img").forEach(function (img) {
        // L'image principale porte le LCP : ni chargement différé, ni fondu.
        if (img.hasAttribute("fetchpriority")) return;

        if (!img.hasAttribute("loading")) img.loading = "lazy";
        img.decoding = "async";
        img.classList.add("image-reveal");

        const reveal = function () { img.classList.add("is-loaded"); };

        if (img.complete) {
            requestAnimationFrame(reveal);
        } else {
            img.addEventListener("load", reveal, { once: true });
            img.addEventListener("error", reveal, { once: true });
        }
    });

    /* ------------------------------------------------------------------
       3. Sécurité des liens sortants
       ------------------------------------------------------------------ */
    document.querySelectorAll('a[target="_blank"]').forEach(function (link) {
        const rel = (link.getAttribute("rel") || "").split(/\s+/).filter(Boolean);
        if (!rel.includes("noopener")) rel.push("noopener");
        if (!rel.includes("noreferrer")) rel.push("noreferrer");
        link.setAttribute("rel", rel.join(" "));
    });

    /* ------------------------------------------------------------------
       4. Intégrations tierces (reel Instagram du Petit Écho)
       Le script de la plateforme n'est demandé qu'à l'approche du bloc :
       rien n'est chargé depuis un tiers tant que le lecteur n'y arrive pas.
       Sans JavaScript, le bloc reste un lien vers la publication.
       ------------------------------------------------------------------ */
    const embeds = document.querySelectorAll("[data-embed-src]");
    const loadedEmbeds = new Set();

    function loadEmbed(container) {
        const src = container.dataset.embedSrc;
        if (loadedEmbeds.has(src)) return;
        loadedEmbeds.add(src);
        const script = document.createElement("script");
        script.async = true;
        script.src = src;
        document.body.appendChild(script);
    }

    if (embeds.length && "IntersectionObserver" in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                observer.unobserve(entry.target);
                loadEmbed(entry.target);
            });
        }, { rootMargin: "800px 0px" });
        embeds.forEach(function (container) { observer.observe(container); });
    } else {
        embeds.forEach(loadEmbed);
    }
});
