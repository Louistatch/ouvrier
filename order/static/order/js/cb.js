$(document).ready(function() {
    $('#countdown-clock').countdown('2024/01/30', function(event) {
      $(this).html(event.strftime('%D days %H:%M:%S'));
    });
  });
 
displayCountdown();
