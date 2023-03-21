let selected;
let main_nav = $("[data-name=MAIN_NAV_TRIGGER_CONTAINER");
let main_nav_drop_down = $(".main-nav-dropdown");
let nav_report = $("[data-menu-dropdown=report]");
let main_nav_report = $("[data-name=NAV_DROPDOWN]")
let ele;
let blanket = $("[data-name=BLANKET]")
let main_search_bar = $("[data-name=AUTOCOMPLETE_SEARCHBOX]");
let search_bar = $("[data-name=AUTOCOMPLETE_CLEAR]")
let search_blanket = $("[data-name=AUTOCOMPLETE_BLANKET]")

main_nav.on("mouseenter", function () {
  main_nav_drop_down.addClass("is-open");
  $("html").addClass("nav-open");
  blanket.removeClass("animate-fade-hidden");
});

main_nav.on("mouseleave", function () {
  main_nav_drop_down.removeClass("is-open");
  $("html").removeClass("nav-open");
  blanket.addClass("animate-fade-hidden");
  main_nav_drop_down.removeClass("has-visible-subsection");

  ele.attr("hidden");
  ele.remove("is-selected");
});

$(".main-nav-dropdown__item").on("mouseenter", function () {
  selected = $(this).children("a").attr("data-detail");
  selected = selected.slice(16).slice(0, -2);

  ele = $("[data-list-id=" + selected + "]");

  main_nav_drop_down.addClass("has-visibile-subsection");
  $(".main-nav-dropdown__subsection").attr("hidden", "");
  $(".main-nav-dropdown__subsection").removeClass("is-selected");

  ele.removeAttr("hidden");
  ele.addClass("is-selected");
});

main_nav_report.on("mouseenter", function () {
  nav_report.removeClass("animate-fade-hidden");
  nav_report.addClass("animate-fade-entered");
  blanket.removeClass("animate-fade-hidden");
  blanket.addClass("animate-fade-entered");
});

main_nav_report.on("mouseleave", function () {
  nav_report.addClass("animate-fade-hidden");
  nav_report.removeClass("animate-fade-entered");
  blanket.addClass("animate-fade-hidden");
  blanket.removeClass("animate-fade-entered");
});

main_search_bar.on("click", function(){
  search_bar.removeAttr("hidden");
  $("html").addClass("search-open");
})

search_blanket.on("click", function(){
  $("html").removeClass("search-open");
  search_bar.attr("hidden", "");
})