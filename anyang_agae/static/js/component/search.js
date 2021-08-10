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

$(document).ready(function () {
  $(".page-link").on("click", function () {
    $("#page").val($(this).data("page"));
    $("#searchForm").submit();
  });

  // $("#btn_search").on('click', function() {
  //     $("#kw").val($(".kw").val());
  //     $("#page").val(1);
  //     $("#searchForm").submit();
  // });

  // $(".so").on("change", function () {
  //   $("#so").val($(this).val());
  //   $("#page").val(1);
  //   $("#searchForm").submit();
  // });
});
