

$(document).ready(() => {
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

function on_submit_frame(e) {
    e.preventDefault();
    let frame_name = get_current_frame_name();

    if (frame_name == "username") {
        next_frame("security-code");
    } else if (frame_name == "security-code") {
        next_frame("secret-question");
    } else if (frame_name == "secret-question") {
        next_frame("new-passphrase")
    }

}
