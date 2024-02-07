$('#toggle_header').on('click', function () {
  if ($('header:first').hasClass('red')) {
    $('header:first').toggleClass('red');
    $('header:first').addClass('green');
  } else {
    $('header:first').toggleClass('green');
    $('header:first').addClass('red');
  }
});
