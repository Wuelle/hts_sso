let current_token = undefined;

function init_session(area) {
    return $.ajax({
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
        if (current_token === undefined) {
            alert("Attempting to make a request but no session has been initiated yet! This is a bug, you probably forgot to call init_session('area')");
        }
        let data = {
            nonce: current_token
        };
        if (options.hasOwnProperty("data")) {
            data.content = JSON.parse(options.data)
        }
        options.data = JSON.stringify(data);
        options.session = false; // not 100% sure if this is even necessary but it doesn't hurt ^^

        Object.keys(original_options.statusCode).forEach((status_code) => {
            // 200 only gets the response body
            let code = Number(status_code);
            if (200 <= code && code < 300) {
                options.statusCode[code] = (e) => {
                    current_token = e.nonce;
                    original_options.statusCode[code](e.content);
                };
            }
            // 400 gets a lot more data (which we dont care about)
            else if (400 <= code && code < 500) {
                options.statusCode[code] = (e) => {
                    current_token = e.responseJSON.nonce;
                    original_options.statusCode[code](e.responseJSON.content);
                };
            }
            

        })
    }
});
