const search_input = document.querySelector(".kw");
const form_input = document.querySelector("#kw");
const search_form = document.querySelector("#searchForm");

function search() {
  form_input.value = search_input.value;
  search_form.submit();
}
