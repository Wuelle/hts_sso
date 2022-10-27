let active_page = "profile";  // initial page, can be overriden by fragment link

$(document).ready(() => {
    if (window.location.href.indexOf("#") != -1) {
        let fragment_link = window.location.href.split("#", 2)[1].toLowerCase();
        if (get_page(fragment_link).length > 0) {
            active_page = fragment_link;
        }
    }

    $(".contains-username").text("Alaska");

    $("[page-container]").append(get_page(active_page));
    $("#timezone").select2();

    $('#account-delete-modal').on('shown.bs.modal', function (e) {
        console.log("shown");
        $(this).find("input").eq(0).focus();
    });

    update_remaining_characters();
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

function edit(name) {
    let element = $("#" + name);
    element.prop("contenteditable", true);

    // set focus to end of value
    let length = element.text().length;
    var selection = window.getSelection();
    var range = document.createRange();
    range.setStart(element[0].childNodes[0], length);
    range.collapse(true);
    selection.removeAllRanges();
    selection.addRange(range);

    element.focus();
}

function stop_editing(name) {
    $("#" + name).prop("contenteditable", false);
}

function update_remaining_characters() {
    let about_me = $("#about-me-content").val();
    // we don't need to check for lengths above the maximum here, since
    // the "maxlength" attribute on the textarea is set, those aren't possible
    // in normal operation
    $("#about-me-length").text(about_me.length);
}
