$(document).ready(() => {
    init_session("forgot-username");
	$("#form-container").on("submit", on_submit_frame);
    set_initial_frame("email");
});

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

    if (frame_name === "email") {
        let email = $("#email").val();

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/request_username_reminder",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                email: email,
            }),
            statusCode: {
                200: (e) => {
                    $("#email-used").text(email);
                    if (e["captcha-required"]) {
                        next_frame("h-captcha");
                    } else {
                        next_frame("done");
                        $("#submit-frame").prop("disabled", true);
                    }
                },
            }
        });
    } else if (frame_name === "h-captcha") {
        let captcha_token = hcaptcha.getResponse();
        if (captcha_token == "") return;
        data = {};
        data["h-captcha-token"] = captcha_token;

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/submit_captcha_token",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data),
            statusCode: {
                200: () => {
                    next_frame("done");
                    $("#submit-frame").prop("disabled", true);
                },
            }
        });
    }
}
