let active_frame = "username";  // first frame show to the user
let animation_duration = 700;  // ms

// just for debugging, will be replaced with an ajax call later
function __next_frame(current) {
	if (current == "username") {
		return "password";
	} else if (current == "password") {
		return "mfa";
	} else if (current == "mfa") {
		return "username";
	}
}

function make_invalid() {
	// color the input in the current frame as being invalid
}

function get_frame(name) {
	if (name == "username") {
		return $("#username-frame");
	} else if (name == "password") {
		return $("#password-frame");
	} else if (name == "mfa") {
		return $("#mfa-frame");
	}
}

function cleanup() {
	$("#frame-container").css("left", 0);
	$("#frame-container").prepend(get_frame(active_frame));
}

$(document).ready(() => {
	// only the input in the active frame is required for form submission
	$("#form-container").on("submit", on_submit_frame);
	$("#frame-container").prepend(get_frame(active_frame));
})


function on_submit_frame(e) {
	e.preventDefault();

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

	let next_frame = __next_frame(active_frame);
	if (next_frame != active_frame) {
		if (next_frame == "username") {
			$("#restart-btn").remove();
		}
		get_frame(active_frame).after(get_frame(next_frame))
		active_frame = next_frame;
		shift_view_left();
	}
}

// visually indicate that the input was incorrect
function bad_input() {
	let container = get_frame(active_frame).children(".input-container").eq(0);
	container.addClass("input-error");
	container.focusin((e) => {
		$(e.delegateTarget).removeClass("input-error");
	});
	container.hover((e) => {
		$(e.delegateTarget).removeClass("input-error");
	});
}

function shift_view_left() {
	$("#frame-container").animate(
		{
			left: "-=" + $("#form-container").outerWidth()
		},
		animation_duration,
		cleanup
	);
}

function shift_view_right() {
	$("#frame-container").animate(
		{
			left: "+=" + $("#form-container").outerWidth()
		},
		animation_duration,
		cleanup,
	);
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
	shift_view_right();
	$("#restart-btn").remove();
}