// blog.js

document.addEventListener("DOMContentLoaded", function () {
    const articleCards = document.querySelectorAll(".card");

    // Ajoutez une interaction pour ouvrir l'article complet en cliquant sur la carte
    articleCards.forEach((card) => {
        card.addEventListener("click", function () {
            // Redirigez l'utilisateur vers la page de l'article complet
            window.location.href = "lien-vers-l-article-complet.html";
        });
    });
});
