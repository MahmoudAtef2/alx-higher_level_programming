$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const userInput = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + userInput;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }, 'json');
  });
});
