$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", (content) => {
  $('#hello').text(content.hello);
});
