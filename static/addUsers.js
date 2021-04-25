"use strict";

$( "#target" ).submit(function( event ) {
    event.preventDefault();
    var new_event = {
          'firstname': document.getElementById('inputfirstname').value,
          'lastname': document.getElementById('inputlastname').value,
          'birthday': document.getElementById('inputbirthday').value,
          'role': document.getElementById('inputrole').value,
          'about': document.getElementById('inputabout').value,
         };
         console.log(new_event);
  
  
  $.ajax({
          url: '/addUser',
          data: $('form').serialize(),
          type: 'POST',
          success: function(response) {
              console.log(response);
          },
          error: function(error) {
              console.log(error);
          }
      });
  
  });












