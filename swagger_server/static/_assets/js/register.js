let MIN_USERNAME_LENGTH = 4;
let MAX_USERNAME_LENGTH = 32;
let USERNAME_LEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890-_ ";

let animation_duration = 700;  // ms
let active_frame = 1;

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
                if (e["captcha-required"]) {
                    console.log("show captcha");
                }
  			},
  		}
	});
});

if (window.location.href.search("frame=") != -1) {
    active_frame = new RegExp('[\?&]frame=([^&#]*)').exec(window.location.href)[1]
}

$(document).ready(() => {
	$("#form-container").on("submit", on_submit_frame);
    $("#first-frame").on("focusout", check_username_available);

    let initial_frame;
    if (active_frame == 1) {
        initial_frame = $("#first-frame");
    } else {
        initial_frame = $("#second-frame");
    }
    initial_frame.removeClass("measure");
})


function get_frame(frame_index) {
    if (frame_index == 1) {
        return $("#first-frame");
    } else if (frame_index == 2) {
        return $("#second-frame");
    } else {
        return $("#third-frame");
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

function after_frame_change() {
	// seamlessly reset the shift
	$("#frame-container").css("left", 0);
	$("#frame-container").prepend(get_frame(active_frame));
	// focus the new input
	get_frame(active_frame).find("input").eq(0).focus();
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
        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/register/start_registration",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                email: email,
                username: username,
            }),
            statusCode: {
                200: (e) => {
                    active_frame = 2;
                    grow_to($("#second-frame").height());
                    $("#second-frame").removeClass("measure");
                    $("#second-frame").find("#email-used").text(email);
                    $("#frame-container").animate(
                        {
                            left: "-=" + $("#form-container").outerWidth()
                        },
                        animation_duration,
                        after_frame_change,
                    );
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
                    active_frame = 3;
                    $("#third-frame").removeClass("measure");
                    grow_to($("#third-frame").height());
                    $("#second-frame").after($("#third-frame"));
                    $("#frame-container").animate(
                        {
                            left: "-=" + $("#form-container").outerWidth()
                        },
                        animation_duration,
                        after_frame_change,
                    );
                },
                403: (e) => {
                    // in theory, the email could also be invalid
                    // but since type=email does not allow you to submit invalid email adresses,
                    // we can be sure that its the username.
                    bad_input($(".input-container:has('#verification-code')"));
                },
            }
        });
    } else {
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

        data = {
            password: password,
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
