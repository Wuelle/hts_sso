let MIN_USERNAME_LENGTH = 4;
let MAX_USERNAME_LENGTH = 32;
let USERNAME_LEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890-_ ";

let captcha_visible = false;


let verification_code = undefined;
if (window.location.href.search("verification_code=") != -1) {
    verification_code = new RegExp('[\?&]verification_code=([^&#]*)').exec(window.location.href)[1]
}

$(document).ready(() => {
    // initialize session manager
    init_session("registration")

	$("#form-container").on("submit", on_submit_frame);
    get_frame("username").on("focusout", check_username_available);

    if (verification_code === undefined) {
        set_initial_frame("username");
    } else {
        set_initial_frame("verification-code");
        $("#verification-code").val(verification_code);
    }
})

const contains_uppercase = new RegExp("(?=.*[a-z])");
const contains_lowercase = new RegExp("(?=.*[a-z])");
const contains_nonalphabetic = new RegExp("(?=.*[^a-zA-Z])");

function validate_passphrase() {
    let passphrase = $("#password").val();
    let warnings = $("#passphrase-warnings");
    if (passphrase.length < 15) {
        warnings.text("must be at least 15 characters long");
        return false;
    }
    if (passphrase.length > 140) {
        warnings.text("must be no more than 140 characters long");
        return false;
    }
    if (!contains_uppercase.test(passphrase)) {
        warnings.text("must contain an uppercase character");
        return false;
    }
    if (!contains_lowercase.test(passphrase)) {
        warnings.text("must contain an lowercase character");
        return false;
    }
    if (!contains_nonalphabetic.test(passphrase)) {
        warnings.text("must contain an nonalphabetic character");
        return false;
    }
}

function change_verification_mail() {
    next_frame("update-email-address");
}

function resend_verification_mail() {
    let email = $("#email").val();
    $.ajax({
        method: "POST",
        url: "http://172.17.0.2:8080/_api/register/resend_verification_mail",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            email: email,
        }),
        statusCode: {
            200: (e) => {
                // transition to same frame for visual feedback
                next_frame("verification-code");
            },
        }
    });
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

    // remove all status effects
    $(".input-container").removeClass("input-error");

    let active_frame = get_current_frame_name();
    if (active_frame == "username") {
        let username = $("#username").val();
        let email = $("#email").val();

        if (username.length == 0) {
            bad_input($(".input-container:has('#username')"));
            return;
        }
        if (email.length == 0) {
            bad_input($(".input-container:has('#email')"));
            return;
        }

        let data = {
            email: email,
            username: username,
        };

        if (captcha_visible) {
            let captcha_token = hcaptcha.getResponse();
            if (captcha_token == "") return
            data["h-captcha-response"] = captcha_token;
        }

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/start_registration",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data),
            statusCode: {
                200: (e) => {
                    get_frame("verification-code").find("#email-used").text(email);
                    next_frame("verification-code");
                    captcha_visible = false;
                },
                403: (e) => {
                    // in theory, the email could also be invalid
                    // but since type=email does not allow you to submit invalid email adresses,
                    // we can be sure that its the username.
                    bad_input($(".input-container:has('#username')"));
                },
            }
        });
    } else if (active_frame == "verification-code") {
        // verify email
        let verification_code = $("#verification-code").val();
        let username = $("#username").val(); // TODO remove on next API iteration
        
        if (verification_code.length == 0) {
            bad_input($(".input-container:has('#verification-code')"));
            return;
        }

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/verify_email_address",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                username: username,
                "verification-code": verification_code,
            }),
            statusCode: {
                200: (e) => {
                    if (e["captcha-required"]) {
                        $("#third-frame").append($(".h-captcha").eq(0));
                        show_captcha();
                    }
                    next_frame("set-password");
                },
                403: (e) => {
                    // in theory, the email could also be invalid
                    // but since type=email does not allow you to submit invalid email adresses,
                    // we can be sure that its the username.
                    bad_input($(".input-container:has('#verification-code')"));
                },
            }
        });
    } else if (active_frame == "set-password") {
        let secret_question = $("#secret-question").val();
        let secret_answer = $("#secret-answer").val();
        let password = $("#password").val();
        let password_confirm = $("#confirm-password").val();

        if (secret_question != "" && secret_answer == "") {
            bad_input($(".input-container:has('#secret-answer')"));
            return;
        }

        if (password == "" || !validate_passphrase()) {
            bad_input($(".input-container:has('#password')"));
            return;
        }

        if (password != password_confirm) {
            bad_input($(".input-container:has('#confirm-password')"));
            return;
        }

        if (!$("#terms-and-conditions").is(":checked")) {
            bad_input($(".input-container:has('#terms-and-conditions')"));
            return;
        }

        let data = {
            password: password,
        };

        if (captcha_visible) {
            let captcha_token = hcaptcha.getResponse();
            if (captcha_token == "") return
            data["h-captcha-response"] = captcha_token;
        }

        // VERY important to not send empty questions/answers
        if (secret_question != "") {
            data["secret-question"] = secret_question;
            data["secret-answer"] = secret_answer;
        }

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/finish_registration",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data),
            statusCode: {
                201: (e) => {
                    window.location = e["redirect"];
                    document.cookie = e["token"];
                },
            }
        });
    } else if (active_frame == "update-email-address") {
        let old_email = $("#old-email").val();
        let new_email = $("#new-email").val();
        let username = $("#username").val(); // TODO remove on next API iteration


        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/change_verification_email",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                "old-email": old_email,
                "new-email": new_email,
                "username": username,
            }),
            statusCode: {
                200: (e) => {
                    $("#second-frame").find("#email-used").text(new_email);
                    next_frame("verification-code");
                },
                403: (e) => {
                    bad_input($(".input-container:has('#old-email')"));
                }
            },

        });
    }
}

function validate_username() {
	let username = $("#username").val();
	let warnings = $("#username-warnings");
	warnings.text(" ")

	if (username.length < MIN_USERNAME_LENGTH) {
		warnings.text("Too short (at least 4 characters)")
		return false;
	} else if (username.length > 32) {
		warnings.text("Too long (at most 32 characters)")
		return false;
	} 
	Array.from(username).forEach(function(c) {
		if (USERNAME_LEGAL_CHARS.indexOf(c) < 0) {
			warnings.html("Illegal character: <span class='inline-highlight'>" + c + "</span>");
			return false;
		}
	});
	return true;
}

function check_username_available() {
    // don't check if the username is invalid
    if (validate_username()) {
        let username = $("#username").val();
	    let warnings = $("#username-warnings");

        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/is_username_available",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                username: username,
            }),
            statusCode: {
                200: (e) => {
                    if (!e["is-available"]) {
			            warnings.html("<span class='inline-highlight'>" + username + "</span> is not available");
                    }
                }
            }
        })
    }
}

function show_captcha() {
	let captcha = $(".h-captcha").eq(0);
	captcha_visible = true;
	captcha.removeClass("inactive-captcha");
	hcaptcha.reset();
}
