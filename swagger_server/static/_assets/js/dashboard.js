let active_page = "profile";  // initial page, can be overriden by fragment link
let is_dirty = false;
let animation_duration = 400;  // ms

$(window).on("beforeunload", () => {
    if (is_dirty) {
        // This message is not actually displayed (in firefox at least)
        // but the fact that we return a nonempty string leads to the browser
        // asking the user effectively the same thing
        return "You have unsaved changes, are you sure you want to leave?";
    }
});

$(document).ready(() => {
    if (window.location.href.indexOf("#") != -1) {
        let fragment_link = window.location.href.split("#", 2)[1].toLowerCase();
        if (get_page(fragment_link).length > 0) {
            active_page = fragment_link;
        }
    }

    $("[page-container]").append(get_page(active_page));
    $("#timezone").select2({
        theme: "hackthissite",
        placeholder: "Select an option",
        escapeMarkup: function(markup) {
            return markup;
        },
        templateResult: (data) => {
            if (data.hasOwnProperty("loading") && data["loading"]) {
                return data;
            } else {
                return "<span class='gmt-offset'>(GMT" + data.element.attributes["gmt-offset"].value + ")</span>:<br>" + data.element.attributes["locations"].value
            }
        }
    });

    $("#timezone").on("select2:open", () => {
        $('input.select2-search__field').attr('placeholder', 'Search');
    });

    $('#account-delete-modal').on('shown.bs.modal', function (e) {
        console.log("shown");
        $(this).find("input").eq(0).focus();
    });

    

    init_session("dashboard").then(() => {
        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/dashboard/get_user_info",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({}),
            statusCode: {
                200: (e) => {
                    // Update basic account info
                    $(".contains-username").text(e["account-info"]["account-name"]);
                    $("#account-name").text(e["account-info"]["account-name"]);
                    $("#display-name").text(e["account-info"]["display-name"]);
                    $("#joined-date").text(e["account-info"]["joined"]);
                    $("#last-login-date").text(e["account-info"]["last-login"]);
                    $("#email").text(e["account-info"]["email"]);
                    $("#website a").text(e["account-info"]["website"].replace("http://", "").replace("https://", ""));
                    $("#website a").attr("href", e["account-info"]["website"]);
                    $("#about-me-content").text(e["account-info"]["about-me"]);
                    update_remaining_characters();

                    // Update linked accounts
                    let linked_accounts = e["account-info"]["linked-accounts"]
                    for(const site in linked_accounts) {
                        let label = $("<label class=\"profile-data-key\">" + site.toUpperCase() + "</label>");
                        let name = $("<a class=\"profile-data-value href-primary\" rel=\"nofollow\" href=\"" + linked_accounts[site].href + "\">" + linked_accounts[site].name + "</span>");
                        $("#linked-accounts").append(label);
                        $("#linked-accounts").append($("<br>"));
                        $("#linked-accounts").append(name);
                        $("#linked-accounts").append($("<br>"));

                    }

                    // Update timezone
                    $("#timezone").val(e["account-info"]["timezone"]);
                    $("#timezone").trigger("change"); 

                    // Update privacy settings
                    $("#privacy-email-hide-from-profile input").prop("checked", e["privacy-settings"]["email"]["hidden-from-profile"]);
                    $("#privacy-email-hide-from-discord input").prop("checked", e["privacy-settings"]["email"]["hidden-from-discord"]);
                    $("#privacy-discord-hide-from-profile input").prop("checked", e["privacy-settings"]["linked-discord-accounts"]["hidden-from-profile"]);
                    $("#privacy-discord-hide-from-discord input").prop("checked", e["privacy-settings"]["linked-discord-accounts"]["hidden-from-discord"]);
                    $("#privacy-irc-hide-from-profile input").prop("checked", e["privacy-settings"]["irc-nicks"]["hidden-from-profile"]);
                    $("#privacy-irc-hide-from-discord input").prop("checked", e["privacy-settings"]["irc-nicks"]["hidden-from-discord"]);
                }
            }
        })
    });
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

function on_profile_picture_upload() {
    let new_pp = $("#profile-picture-upload")[0].files[0];

    // 20kB max
    if (new_pp.size > 20 * 1024) {
        alert("too large");
    } else {
        let url = URL.createObjectURL(new_pp);
        console.log(url);
        $("#profile-picture")[0].src = url;
        console.log("update pp");
    }
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

function set_sidebar_visible(visibility) {
    let width;
    if (visibility) {
        width = "15%";
    } else {
        width = 0;
    }

    $("#dashboard-navigation-bar").animate(
        {
            width: width,
        },
        animation_duration,
    );
}

function set_dashboard_dirty(dirty) {
    $("#dashboard-content").attr("data-dirty", dirty);
}
