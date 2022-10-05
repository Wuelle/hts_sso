let current_token = undefined;

function init_session(area) {
    $.ajax({
        method: "GET",
        url: "http://172.17.0.2:8080/_api/session/get_nonce_token",
        data: {
            area: area,
        },
        session: false, // this must not be intercepted - there is no token yet!
        statusCode: {
            200: (e) => {
                current_token = e.nonce;
            }
        }
    })
}

$.ajaxPrefilter(function(options, original_options, xhr) {
    // callers can disable the intercept by setting session = false
    if(!(options.hasOwnProperty("session") && !options.session)) {
        options.data = JSON.stringify({
            nonce: current_token,
            content: JSON.parse(options.data)
        });

        for (callback in original_options.statusCode) {
            options.statusCode[callback] = (e) => {
                current_token = e.nonce;
                original_options.statusCode[callback](e.content);
            };
        }
    }
});
