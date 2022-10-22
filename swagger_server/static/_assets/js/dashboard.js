let active_page = "profile";  // initial page
$(document).ready(() => {
    $("[page-container]").append(get_page(active_page));
});

function get_page(page_name) {
    return $("[data-page='" + page_name + "']");
}
function show_page(page_name) {
    $("[page-store]").append(get_page(active_page));
    $("[page-container]").append(get_page(page_name));
    active_page = page_name;
}

function on_profile_picture_click() {
    $("#profile-picture-upload").click();
}
