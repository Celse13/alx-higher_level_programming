$('#add_item').click(() => {
  const addItem = $('<li>').text('Item')
  $('ul.my_list').append(addItem);
});
