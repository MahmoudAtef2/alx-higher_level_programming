$(document).ready(function () {
  function translationPerform () {
    const userInput = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + userInput;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }, 'json');
  }
  $('#btn_translate').on('click', function () {
    translationPerform();
  });
  $('#language_code').on('keydown', function (event) {
    if (event.key === 'Enter') {
      translationPerform();
    }
  });
});
