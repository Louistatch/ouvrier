function displayCountdown() {
  const targetDate = new Date('2024-01-30T00:00:00').getTime();

  const countdownInterval = setInterval(function () {
    const currentDate = new Date().getTime();
    const timeLeft = targetDate - currentDate;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    document.getElementById('countdown').innerHTML = `
      ${days} Jours ${hours} Heures ${minutes} Minutes ${seconds} Secondes restantes
    `;

    if (timeLeft < 0) {
      clearInterval(countdownInterval);
      document.getElementById('countdown').innerHTML = 'Le 30 janvier 2024 est enfin arrivé !';
    }
  }, 1000);
}

displayCountdown();

// Code JavaScript pour gérer les étapes du formulaire

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form');
    const formSteps = form.querySelectorAll('.form-step');
    let currentStep = 0;
  
    const nextButton = document.getElementById('next-button');
    const submitButton = document.querySelector('[type="submit"]');
    
    nextButton.addEventListener('click', function(e) {
      e.preventDefault(); // Empêche le formulaire de se soumettre lorsque le bouton "Suivant" est cliqué.
  
      if (currentStep < formSteps.length - 1) {
        formSteps[currentStep].style.display = 'none';
        currentStep++;
        formSteps[currentStep].style.display = 'block';
  
        if (currentStep === formSteps.length - 1) {
          // Si c'est la dernière étape, masquez le bouton "Suivant" et affichez le bouton "Soumettre".
          nextButton.style.display = 'none';
          submitButton.style.display = 'block';
        }
      }
    });
  });
  