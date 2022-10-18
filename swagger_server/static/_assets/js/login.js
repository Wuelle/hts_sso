$(document).ready(() => {

	// only the input in the active frame is required for form submission
	$("#form-container").on("submit", on_submit_frame);

    let data = {}

    const GET_redirect = new RegExp('[\?&]redirect=([^&#]*)')
	if (GET_redirect.test(window.location.href)) {
        data.redirect = GET-redirect.exec(window.location.href)[1];
    } else {
        data.redirect = "hackthissite.org" // TODO: replace with the right link
    }

    const GET_username = new RegExp('[\?&]username=([^&#]*)');
	if (GET_username.test(window.location.href)) {
		data.username = GET_username.exec(window.location.href)[1];
	}

    init_session("login").then(() => {
        $.ajax({
            method: "POST",
            url: "http://172.17.0.2:8080/_api/login/init_session",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(data), // TODO error handling
            statusCode: {
                200: (e) => {
                    set_initial_frame(e["first-frame"]);
                    if (e["first-frame"] != "username") create_back_button();
                }
            }
        })
    });
})

function on_submit_frame(e) {
	e.preventDefault();

    // remove all status effects
    $(".input-container").removeClass("input-error");

    let active_frame = get_current_frame_name();

	let value = undefined;
    if (active_frame === "username") {
        value = $("#username").val();
	    if (value == "") bad_input($(".input-container:has('#username')"));
    } else if (active_frame === "password") {
        value = $("#password").val();
	    if (value == "") bad_input($(".input-container:has('#password')"));
    } else if (active_frame === "mfa") {
        value = $("#mfa").val();
	    if (value == "") bad_input($(".input-container:has('#mfa')"));
    } else if (active_frame === "captcha") {
  		value = hcaptcha.getResponse();
    }

	let data = { 
  		 frame: active_frame, 
  		 value: value,
  	};

	$.ajax({
		method: "POST",
  		url: "http://172.17.0.2:8080/_api/login/submit_frame",
  		contentType: "application/json",
  		dataType: "json",
  		data: JSON.stringify(data),
  		statusCode: {
  			200: (e) => {
  				next_frame(e["next"]);
  			},
  			409: () => {
  				$("#error-modal").modal("show");
  			},
  			201: (e) => {
  				window.location = e["redirect"];
  				document.cookie = e["token"];
  			},
  			403: () => bad_input(get_frame(active_frame).find(".input-container").eq(0)),
  		}
	});
}
function create_back_button() {
	// Add a button to restart authentication from the beginning
	let restart_btn = $("<button>");
	restart_btn.attr("id", "restart-btn");
	restart_btn.addClass("btn btn-lg btn-primary button-primary btn-block");
	restart_btn.text("Go back");
	restart_btn.on("click", on_restart);

	let parent = $("#btn-container");
	parent.prepend(restart_btn);
}

// visually indicate that the input was incorrect
function bad_input(container) {
    container.addClass("input-error");
    container.focusin((e) => {
        $(e.delegateTarget).removeClass("input-error");
    });
    container.hover((e) => {
        $(e.delegateTarget).removeClass("input-error");
    });
}

// it can be assumed that this function will never be called
// from the username frame itself
function on_restart(e) {
	e.preventDefault();

	// put the username frame on the left
	$("#frame-container").css("left", -$("#form-container").outerWidth());
	$("#frame-container").prepend(get_frame("username"));
	get_frame("username").after(get_frame(active_frame));
	active_frame = "username";
	$("#frame-container").animate(
		{
			left: "+=" + $("#form-container").outerWidth()
		},
		after_frame_change,
	);
	$("#restart-btn").remove();
}
