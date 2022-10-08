let MIN_USERNAME_LENGTH = 4;
let MAX_USERNAME_LENGTH = 32;
let USERNAME_LEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890-_ ";

let animation_duration = 700;  // ms
let active_frame = 1;
let captcha_visible = false;


let verification_code = undefined;
if (window.location.href.search("verification_code=") != -1) {
    verification_code = new RegExp('[\?&]verification_code=([^&#]*)').exec(window.location.href)[1]
}

$(document).ready(() => {
    // initialize session manager
    init_session("registration").then(() => {
        // check whether we need a captcha on the first frame
        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/is_initial_captcha_required",
            contentType: "application/json",
            dataType: "json",
            statusCode: {
                200: (e) => {
	                let captcha = $(".h-captcha").eq(0);
                    captcha.css("opacity", 1);
                    if (e["captcha-required"]) {
			            captcha.removeClass("inactive-captcha");
                        $("#first-frame").append(captcha);
                        captcha_visible = true;
                    }
                },
            }
        });
    });


	$("#form-container").on("submit", on_submit_frame);
    $("#first-frame").on("focusout", check_username_available);

    let initial_frame;
    if (verification_code === undefined) {
        active_frame = 1;
        initial_frame = $("#first-frame");
    } else {
        initial_frame = $("#second-frame");
        active_frame = 2;
        $("#verification-code").val(verification_code);
    }
    initial_frame.removeClass("measure");
})


function get_frame(frame_index) {
    if (frame_index == 1) {
        return $("#first-frame");
    } else if (frame_index == 2) {
        return $("#second-frame");
    } else if (frame_index == 3) {
        return $("#third-frame");
    } else {
        return $("#fourth-frame");
    }
}

function change_verification_mail() {
    animate_change_frame(4);
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
                animate_change_frame(2);  // transition to same frame for visual feedback
            },
        }
    });
}

function animate_change_frame(new_frame_nr) {
    if (new_frame_nr != active_frame) {
        let old_frame = get_frame(active_frame);
        let new_frame = get_frame(new_frame_nr);

        // lock container height
        $("#frame-container").css("height", $("#frame-container").height());

        // some trickery is necessary to compute the height of the element correctly
        new_frame.css("max-width", $(old_frame).width())
        old_frame.after(get_frame(new_frame));
        new_frame.removeClass("measure");
        new_height = new_frame.height();

        active_frame = new_frame_nr;

        if (new_height > old_frame.height()) {
            // grow first, then transition
            grow_to(new_frame.height());
            active_frame = new_frame_nr;
            $("#frame-container").animate(
                {
                    left: "-=" + $("#form-container").outerWidth()
                },
                animation_duration,
                () => {
                    old_frame.addClass("measure");
                    // seamlessly reset the shift
                    $("#frame-container").css("left", 0);
                    $("#frame-container").prepend(get_frame(active_frame));
                    // focus the new input
                    get_frame(active_frame).find("input").eq(0).focus();
                }
            );
        } else {
            // transition first, then shrink
            active_frame = new_frame_nr;
            $("#frame-container").animate(
                {
                    left: "-=" + $("#form-container").outerWidth()
                },
                animation_duration,
                () => {
                    grow_to(new_height);
                    old_frame.addClass("measure");
                    // seamlessly reset the shift
                    $("#frame-container").css("left", 0);
                    $("#frame-container").prepend(get_frame(active_frame));
                    // focus the new input
                    get_frame(active_frame).find("input").eq(0).focus();
                }
            );
        }
    } else {
        let old_frame = get_frame(active_frame);
        let new_frame = old_frame.clone();
        old_frame.before(new_frame);
        $("#frame-container").animate(
            {
                left: "-=" + $("#form-container").outerWidth()
            },
            animation_duration,
            () => {
                // different frame change than usual
	            $("#frame-container").css("left", 0);
                old_frame.remove();
	            get_frame(active_frame).find("input").eq(0).focus();
            }
        );
    }
}

function grow_to(target_height) {
    $("#frame-container").animate(
        {
            height: "+=" + (target_height - $("#frame-container").height()),
        },
        animation_duration,
    );
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

    if (active_frame == 1) {
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
                    $("#second-frame").find("#email-used").text(email);
                    animate_change_frame(2);
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
    } else if (active_frame == 2) {
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
                    animate_change_frame(3);
                },
                403: (e) => {
                    // in theory, the email could also be invalid
                    // but since type=email does not allow you to submit invalid email adresses,
                    // we can be sure that its the username.
                    bad_input($(".input-container:has('#verification-code')"));
                },
            }
        });
    } else if (active_frame == 3) {
        // finish registration
        let secret_question = $("#secret-question").val();
        let secret_answer = $("#secret-answer").val();
        let password = $("#password").val();
        let password_confirm = $("#confirm-password").val();

        if (secret_question != "" && secret_answer == "") {
            bad_input($(".input-container:has('#secret-answer')"));
            return;
        }

        if (password == "") {
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
        }

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
    } else if (active_frame == 4) {
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
                    animate_change_frame(2);
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
