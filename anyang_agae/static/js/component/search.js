const search_input = document.querySelector(".kw");
const form_input = document.querySelector("#kw");
const page = document.querySelector("#page");
const search_form = document.querySelector("#searchForm");

function clickSearch() {
  form_input.value = search_input.value;
  page.value = 1;
  search_form.submit();
}

function search() {
  if (window.event.keyCode === 13) {
    form_input.value = search_input.value;
    page.value = 1;
    search_form.submit();
  }
}
