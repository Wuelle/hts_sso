let MIN_USERNAME_LENGTH = 4;
let MAX_USERNAME_LENGTH = 32;
let USERNAME_LEGAL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW1234567890-_ ";
$(document).ready(() => {
})

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
			warnings.text("Illegal character: '" + c + "'");
			return false;
		}
	});
	return true;
}