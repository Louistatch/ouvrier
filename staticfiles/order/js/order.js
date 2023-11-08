document.addEventListener('DOMContentLoaded', function() {
    // Sélectionnez les éléments du formulaire et du carrousel par leurs classes ou ID
    const formulaire = document.querySelector('.container-fluid form');
    const carrouselItems = document.querySelectorAll('.carousel-item');
    const formFields = document.querySelectorAll('.container-fluid form table td input');
    const tableRows = document.querySelectorAll('.table-row');
  
    // Ajoutez un gestionnaire d'événement pour les éléments du formulaire
    formulaire.addEventListener('mouseover', function() {
      formulaire.style.backgroundColor = '#e3e3e3';
    });
  
    formulaire.addEventListener('mouseout', function() {
      formulaire.style.backgroundColor = '';
    });
  
    // Ajoutez un gestionnaire d'événement pour les éléments du carrousel
    carrouselItems.forEach(function(item) {
      item.addEventListener('mouseover', function() {
        item.style.transform = 'scale(1.05)';
      });
  
      item.addEventListener('mouseout', function() {
        item.style.transform = '';
      });
    });
  
    // Changez la couleur de fond du corps du site au clic
    document.body.addEventListener('click', function() {
      document.body.style.backgroundColor = 'lightblue';
    });
  
    // Réinitialisez la couleur de fond au double clic
    document.body.addEventListener('dblclick', function() {
      document.body.style.backgroundColor = '';
    });
  
    // Ajoutez un gestionnaire d'événement pour les champs du formulaire
    formFields.forEach(function(field) {
      field.addEventListener('mouseover', function() {
        field.style.transition = 'all 0.3s';
        field.style.transform = 'translateZ(10px)';
      });
  
      field.addEventListener('mouseout', function() {
        field.style.transition = 'all 0.3s';
        field.style.transform = '';
      });
    });
  
    // Ajoutez des événements pour les lignes du tableau
    tableRows.forEach(function(row) {
      row.addEventListener('mouseenter', function() {
        row.style.transform = 'perspective(500px) rotateX(10deg)';
        row.style.transition = 'transform 0.3s';
      });
  
      row.addEventListener('mouseleave', function() {
        row.style.transform = 'perspective(500px) rotateX(0deg)';
      });
    });
  
    function setCSRFCookie(csrf_cookie_name, csrf_token) {
      Cookies.set(csrf_cookie_name, csrf_token, { path: '/' });
    }
  });
  