// Sélectionnez les éléments du formulaire et du carrousel par leurs classes ou ID
const formulaire = document.querySelector('.container-fluid form');
const carrouselItems = document.querySelectorAll('.carousel-item');

// Ajoutez un gestionnaire d'événement pour les éléments du formulaire
formulaire.addEventListener('mouseover', () => {
  formulaire.style.backgroundColor = '#e3e3e3'; // Changez la couleur de fond au survol
});

formulaire.addEventListener('mouseout', () => {
  formulaire.style.backgroundColor = ''; // Réinitialisez la couleur de fond
});

// Ajoutez un gestionnaire d'événement pour les éléments du carrousel
for (const item of carrouselItems) {
  item.addEventListener('mouseover', () => {
    item.style.transform = 'scale(1.05)'; // Animez l'élément au survol
  });

  item.addEventListener('mouseout', () => {
    item.style.transform = ''; // Réinitialisez la transformation
  });
}

// Changez la couleur de fond du corps du site au clic
document.body.addEventListener('click', () => {
  document.body.style.backgroundColor = 'lightblue';
});

// Réinitialisez la couleur de fond au double clic
document.body.addEventListener('dblclick', () => {
  document.body.style.backgroundColor = '';
});
// Sélectionnez les éléments du formulaire par leur classe ou ID
const formFields = document.querySelectorAll('.container-fluid form table td input');

// Ajoutez un gestionnaire d'événement pour les champs du formulaire
for (const field of formFields) {
  field.addEventListener('mouseover', () => {
    field.style.transition = 'all 0.3s'; // Ajoutez une transition de 0.3 secondes
    field.style.transform = 'translateZ(10px)'; // Appliquez une transformation en Z pour l'effet 3D
  });

  field.addEventListener('mouseout', () => {
    field.style.transition = 'all 0.3s'; // Ajoutez une transition de 0.3 secondes
    field.style.transform = ''; // Réinitialisez la transformation
  });
}

const tableRows = document.querySelectorAll('.table-row');

tableRows.forEach((row) => {
    row.addEventListener('mouseenter', () => {
        // Appliquer des transformations 3D aux cellules
        row.style.transform = 'perspective(500px) rotateX(10deg)';
        row.style.transition = 'transform 0.3s';
    });

    row.addEventListener('mouseleave', () => {
        // Réinitialiser les transformations 3D
        row.style.transform = 'perspective(500px) rotateX(0deg)';
    });
});

function setCSRFCookie(csrf_cookie_name, csrf_token) {
    Cookies.set(csrf_cookie_name, csrf_token, { path: '/' });
}