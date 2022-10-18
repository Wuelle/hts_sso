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

    if (frame_name === "username") {
        let username = $("#username").val();

        if (username === "") {
            bad_input($(".input-container:has('#username')"));
            return;
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
    } else if (frame_name === "security-code") {
        let security_code = $("#security-code").val();

        if (security_code === "") {
            bad_input($(".input-container:has('#security-code')"));
            return;
        }

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/submit_passphrase_update_token",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                token: security_code,
            }),
            statusCode: {
                200: (e) => {
                    if (e.hasOwnProperty("secret-question")) {
                        $("#secret-question").text(e["secret-question"]);
                        next_frame("secret-question");
                    } else {
                        next_frame("new-passphrase");
                    }
                },
                403: (e) => {
                    bad_input($(".input-container:has('#security-code')"));
                },
            }
        });
    } else if (frame_name === "secret-question") {
        let secret_answer = $("#secret-answer").val();

        if (secret_answer === "") {
            bad_input($(".input-container:has('#secret-answer')"));
            return;
        }

        data = {}
        data["secret-answer"] = secret_answer;

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/submit_secret_answer",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data),
            statusCode: {
                200: (e) => {
                    next_frame("new-passphrase");
                },
                403: (e) => {
                    bad_input($(".input-container:has('#secret-answer')"));
                },
            }
        });
    } else if (frame_name === "new-passphrase") {
        let passphrase = $("#new-passphrase").val();
        let passphrase_confirm = $("#confirm-passphrase").val();

        if (passphrase === "") {
            bad_input($(".input-container:has('#new-passphrase')"));
            return;
        }

        if (passphrase !== passphrase_confirm) {
            bad_input($(".input-container:has('#confirm-passphrase')"));
            return;
        }
        data = {}
        data["update-token"] = "foo"; // TODO: remove
        data["new-passphrase"] = passphrase;

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/update_passphrase",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data),
            statusCode: {
                200: (e) => {
                    if (e["captcha-required"]) {
                        next_frame("h-captcha");
                    } else {
                        // TODO: prob redirect to landing page or sth similar
                    }
                },
                403: (e) => {
                    // this shouldn't happen as the client should not be able to submit
                    // invalid passphrases
                    bad_input($(".input-container:has('#new-passphrase')"));
                },
            }
        });
    } else if (frame_name === "h-captcha") {
        let captcha_token = hcaptcha.getResponse();
        if (captcha_token == "") return
        data = {};
        data["h-captcha-token"] = captcha_token;

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/account_recovery/submit_captcha_token",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data),
            statusCode: {
                200: (e) => {
                    // TODO: prob redirect to landing page or sth similar
                },
            }
        });
    }

}
