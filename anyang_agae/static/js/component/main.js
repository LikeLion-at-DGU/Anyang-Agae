$('#hospital_btn').on('click', function () {
  $('html, body').animate(
    {
      scrollTop: $('#hospital_area').offset().top - 10,
    },
    400,
  )
})

$('#community_btn').on('click', function () {
  $('html, body').animate(
    {
      scrollTop: $('#community_area').offset().top - 10,
    },
    400,
  )
})

$('#review_btn').on('click', function () {
  $('html, body').animate(
    {
      scrollTop: $('#review_area').offset().top - 10,
    },
    400,
  )
})

$('#diary_btn').on('click', function () {
  $('html, body').animate(
    {
      scrollTop: $('#diary_area').offset().top - 10,
    },
    400,
  )
})
