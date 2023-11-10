// static/mon_app/js/base.js
// JavaScript avec jQuery pour votre site web

$(document).ready(function() {
    // Code JavaScript avec jQuery ici

    // Exemple : Ajouter une animation au bouton de soumission
    $("#submit-button").click(function() {
        $(this).animate({ opacity: 0.5 }, 500);
    });

    // Animation de chargement de connexion
    $(".loading").hide();
    $("#submit-button").click(function() {
        $(".loading").show();
        // Créez un élément de cercle
        var circle = document.createElement("div");
        circle.classList.add("loader");
        circle.style.width = "100px";
        circle.style.height = "100px";
        circle.style.borderRadius = "50%";
        circle.style.backgroundColor = "gray";

        // Ajoutez le cercle à la page
        $(".loading").append(circle);

        // Commencez l'animation
        var animation = setInterval(function() {
            circle.style.backgroundColor = "white";
            setTimeout(function() {
                circle.style.backgroundColor = "gray";
            }, 500);
        }, 1000);

        // Arrêtez l'animation lorsque le chargement est terminé
        setTimeout(function() {
            clearInterval(animation);
            $(".loading").hide();
        }, 5000);
    });
});
