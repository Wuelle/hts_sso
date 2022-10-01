let MIN_USERNAME_LENGTH = 4;
let MAX_USERNAME_LENGTH = 32;
let USERNAME_LEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890-_ ";

let animation_duration = 700;  // ms
let active_frame = 1;

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
        // if (username.length == 0) {
        //     bad_input($(".input-container:has('#username')"));
        //     return;
        // }
        // if (email.length == 0) {
        //     bad_input($(".input-container:has('#email')"));
        //     return;
        // }

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
    } else if (active_frame == 2) {
        let verification_code = $("#verification-code").val();
        // if (verification-code.length == 0) {
        //     bad_input($(".input-container:has('#verification-code')"));
        //     return;
        // }

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
    } else {
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

        // replace with ajax call later
        if (username == "Alaska") {
			warnings.html("<span class='inline-highlight'>" + username + "</span> is not available");
        }
    }

}
