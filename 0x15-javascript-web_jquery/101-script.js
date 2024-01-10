$(document).ready(() => {
  $('#add_item').click(() => {
    $('<li>').text('Item').appendTo('ul.my_list');
  });
  $('#remove_item').click(() => {
    $('ul.my_list li:last-child').remove();
  });
  $('#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
