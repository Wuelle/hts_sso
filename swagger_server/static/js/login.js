let active_frame = "username";  // first frame show to the user
let animation_duration = 700;  // ms
let captcha_visible = false;


function get_frame(name) {
	if (name == "username") {
		return $("#username-frame");
	} else if (name == "password") {
		return $("#password-frame");
	} else if (name == "mfa") {
		return $("#mfa-frame");
	}
}

$(document).ready(() => {
	// only the input in the active frame is required for form submission
	$("#form-container").on("submit", on_submit_frame);
	$("#frame-container").prepend(get_frame(active_frame));
	get_frame(active_frame).find("input").eq(0).focus();
})

function on_submit_frame(e) {
	e.preventDefault();

	// remove potential input warnings
	get_frame(active_frame).children(".input-container").eq(0).removeClass("input-error");

	let value = get_frame(active_frame).find("input").eq(0).val();
	if (value == "") {
		bad_input();
		return;
	}

	let data = { 
  		 frame: active_frame, 
  		 value: value,
  	};
  	if (captcha_visible) {
  		let captcha_token = hcaptcha.getResponse();
  		if (captcha_token == "") return
  		data["h-captcha-response"] = captcha_token;
  		hide_captcha()
  	}

	$.ajax({
		method: "POST",
  		url: "http://172.17.0.2:8080/_api/login",
  		contentType: "application/json",
  		dataType: "json",
  		data: JSON.stringify(data),
  		statusCode: {
  			200: (e) => {
  				switch_frame(e["next"]);
  				if (e["show-captcha"]) {
  					show_captcha();
  				}
  			},
  			409: () => {
  				$("#error-modal").modal("show");
  			},
  			201: (e) => {
  				document.cookie = e["token"];
  				window.location = e["redirect"];
  			},
  			403: bad_input,
  		}
	});
}

function switch_frame(next_frame) {
	if (active_frame == "username") {
		// Add a button to restart authentication from the beginning
		let restart_btn = $("<button>");
		restart_btn.attr("id", "restart-btn");
		restart_btn.addClass("btn btn-lg btn-primary button-primary btn-block");
		restart_btn.text("Go back");
		restart_btn.on("click", on_restart);

		let parent = $("#btn-container");
		parent.prepend(restart_btn);
	}

	if (next_frame != active_frame) {
		if (next_frame == "username") {
			$("#restart-btn").remove();
		}
		get_frame(active_frame).after(get_frame(next_frame)); // insert next frame after current frame
		active_frame = next_frame;
		get_frame(active_frame).focus();
		$("#frame-container").animate(
			{
				left: "-=" + $("#form-container").outerWidth()
			},
			animation_duration,
			after_frame_change
		);
	}
}

function after_frame_change() {
	// seamlessly reset the shift
	$("#frame-container").css("left", 0);
	$("#frame-container").prepend(get_frame(active_frame));
	// focus the new input
	get_frame(active_frame).find("input").eq(0).focus();
}

// visually indicate that the input was incorrect
function bad_input() {
	let container = get_frame(active_frame).children(".input-container").eq(0);
	container.addClass("input-error");

	// remove the indicator if the input is hovered/focused
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

	if (captcha_visible) {
		hide_captcha()
	}

	// clear username input
	// other frames are cleared later so the user still sees
	// their input sliding away
	get_frame("username").find("input").eq(0).val("")

	// put the username frame on the left
	$("#frame-container").css("left", -$("#form-container").outerWidth());
	$("#frame-container").prepend(get_frame("username"));
	get_frame("username").after(get_frame(active_frame));
	active_frame = "username";
	$("#frame-container").animate(
		{
			left: "+=" + $("#form-container").outerWidth()
		},
		animation_duration,
		() => {
			after_frame_change();

			// clear other inputs
			get_frame("password").find("input").eq(0).val("")
			get_frame("mfa").find("input").eq(0).val("")

		},
	);
	$("#restart-btn").remove();
}

function show_captcha() {
	captcha_visible = true;
	// need to do some black magic to smoothly animate captcha
	let captcha = $(".h-captcha").eq(0);
	$("#captcha-container").animate(
		{
			height: "+=" + captcha.height(),
		},
		animation_duration / 2,
		() => {
			captcha.removeClass("inactive-captcha");
			captcha.animate({
				"opacity": 1
			}, animation_duration / 2);
		},
	);
}

function hide_captcha() {
	captcha_visible = false;
	let captcha = $(".h-captcha").eq(0);
	captcha.animate({
			"opacity": 0
		}, 
		animation_duration / 2, 
		() => {
			captcha.addClass("inactive-captcha");
			$("#captcha-container").animate(
			{
				height: "-=" + captcha.height()
			},
			animation_duration / 2);
	});
	hcaptcha.reset();
}
