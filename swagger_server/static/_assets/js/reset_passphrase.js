

$(document).ready(() => {
    init_session("reset-passphrase");

	$("#form-container").on("submit", on_submit_frame);

    // The user can skip the first frame by clicking the link in the mail, which includes a "security_code" GET param
    if (window.location.href.search("security_code=") != -1) {
        let security_code = new RegExp('[\?&]security_code=([^&#]*)').exec(window.location.href)[1]
        set_initial_frame("security-code");
        $("#security-code").val(security_code)
    } else {
        set_initial_frame("username");
    }
});

function resend_security_mail() {
    next_frame("security-code");
}

function bad_input(container) {
    container.addClass("input-error");
    container.focusin((e) => {
        $(e.delegateTarget).removeClass("input-error");
    });
    container.hover((e) => {
        $(e.delegateTarget).removeClass("input-error");
    });
}

function on_submit_frame(e) {
    e.preventDefault();
    let frame_name = get_current_frame_name();

    if (frame_name == "username") {
        let username = $("#username").val();

        if (username === "") {
            bad_input($(".input-container:has('#username')"));
        }
        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/request_passphrase_update_token",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                username: username,
            }),
            statusCode: {
                200: (e) => {
                    next_frame("security-code");
                },
                403: (e) => {
                    bad_input($(".input-container:has('#username')"));
                },
            }
        });
    } else if (frame_name == "security-code") {
        let username = $("#username").val();

        if (username === "") {
            bad_input($(".input-container:has('#username')"));
        }
        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/request_passphrase_update_token",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                username: username,
            }),
            statusCode: {
                200: (e) => {
                    next_frame("secret-question");
                },
                403: (e) => {
                    bad_input($(".input-container:has('#username')"));
                },
            }
        });
    } else if (frame_name == "secret-question") {
        next_frame("new-passphrase")
    }

}
