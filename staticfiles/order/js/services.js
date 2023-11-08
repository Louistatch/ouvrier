document.addEventListener("DOMContentLoaded", function () {
    // Sélectionnez les éléments que vous souhaitez animer
    const floatingElements = document.querySelectorAll(".floating-element");

    // Fonction pour animer les éléments flottants
    function animateFloatingElements() {
        floatingElements.forEach((element) => {
            // Générez des valeurs de déplacement aléatoires en HD
            const translateY = Math.random() * 20 - 10;
            const translateX = Math.random() * 20 - 10;

            // Appliquez les transformations CSS pour créer l'effet de flottaison
            element.style.transform = `translate(${translateX}px, ${translateY}px)`;

            // Animation en boucle
            element.addEventListener("transitionend", () => {
                setTimeout(() => {
                    animateFloatingElements();
                }, 1000);
            });
        });
    }

    // Lancez l'animation des éléments flottants
    animateFloatingElements();
});
