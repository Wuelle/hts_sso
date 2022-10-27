// General terminology:
//
// frame = one panel that can slide in/out of the view
// frame Container = the view div where active frames appear
// frame store = the place where inactive frames are stored

let active_frame_name = undefined;
let animation_duration = 700;  // ms

function get_current_frame_name() {
    return active_frame_name;
}

function get_frame(frame_name) {
    return $("[data-frame='" + frame_name + "']");
}

function get_frame_container() {
    return $("[data-frame-container]");
}

function get_frame_store() {
    return $("[data-frame-store]");
}

function set_initial_frame(frame_name) {
    let initial_frame = get_frame(frame_name);
    get_frame_container().append(initial_frame);
    active_frame_name = frame_name;
    initial_frame.find("input").eq(0).focus();
}

function grow_to(target_height) {
    let frame_container = get_frame_container();
    if (target_height !== frame_container.height()) {
        return frame_container.animate(
            {
                height: "+=" + (target_height - frame_container.height()),
            },
            animation_duration,
        ).promise();
    }
}

// Like next_frame, except sliding to the right
// doesn't have all the capabilities (because its only used in one place
// right now)
// TODO: merge this with next_frame
function previous_frame(frame_name) {
    let frame_container = get_frame_container();
    let old_frame = get_frame(get_current_frame_name());
    let new_frame = get_frame(frame_name);

    // lock container height - the following dom manipulations would cause the view height
    // to spasm around otherwise
    frame_container.css("height", frame_container.height());

    // some trickery is necessary to compute the height of the element correctly
	frame_container.css("left", -$("#form-container").outerWidth());
	frame_container.prepend(new_frame);
    new_frame.css("max-width", $(old_frame).width())

	active_frame_name = frame_name;
    new_height = new_frame.height();

    if (new_height > old_frame.height()) {
        // for some reason, this *one* animation behaves different than every other one.
        // Have to 
        // 1) remove new frame
        // 2) grow to size of new frame
        // 3) re-insert new frame
        // else the current frame will be invisible during the animation.
        // This solution seems to work cross platform and has, apart from being a bit hacky,
        // no downsides 
        // TODO: investigate and fix
	    frame_container.css("left", 0);
        get_frame_store().append(new_frame);
        grow_to(new_height).then(() => {
            frame_container.css("left", -$("#form-container").outerWidth());
            frame_container.prepend(new_frame);

            frame_container.animate(
                {
                    left: "+=" + $("#form-container").outerWidth()
                },
                animation_duration,
                () => {
                    // get_frame_store().append(old_frame);
                    // focus the new input
                    // new_frame.find("input").eq(0).focus();
                },
            );
        });
    } else {
        frame_container.animate(
            {
                left: "+=" + $("#form-container").outerWidth()
            },
            animation_duration,
            () => {
                grow_to(new_height);

                get_frame_store().append(old_frame);
                // focus the new input
                new_frame.find("input").eq(0).focus();
            },
        );
    }
}

function next_frame(frame_name) {
    let frame_container = get_frame_container();

    if (frame_name != active_frame_name) {
        let old_frame = get_frame(active_frame_name);
        let new_frame = get_frame(frame_name);

        // lock container height - the following dom manipulations would cause the view height
        // to spasm around otherwise
        frame_container.css("height", frame_container.height());

        // some trickery is necessary to compute the height of the element correctly
        new_frame.css("max-width", $(old_frame).width())
        old_frame.after(new_frame);
        new_height = new_frame.height();

        active_frame_name = frame_name;

        if (new_height > old_frame.height()) {
            // grow first, then transition
            // grow_to(new_frame.height());
            grow_to(new_height);
            frame_container.animate(
                {
                    left: "-=" + $("#form-container").outerWidth()
                },
                animation_duration,
                () => {
                    get_frame_store().append(old_frame);

                    // seamlessly reset the shift
                    frame_container.css("left", 0);
                    frame_container.prepend(get_frame(active_frame_name));

                    // focus the new input
                    new_frame.find("input").eq(0).focus();
                }
            );
        } else {
            // transition first, then shrink
            frame_container.animate(
                {
                    left: "-=" + $("#form-container").outerWidth()
                },
                animation_duration,
                () => {
                    get_frame_store().append(old_frame);
                    grow_to(new_height);

                    // seamlessly reset the shift
                    frame_container.css("left", 0);
                    frame_container.prepend(get_frame(active_frame_name));

                    // focus the new input
                    new_frame.find("input").eq(0).focus();
                }
            );
        }
    } else {
        let old_frame = get_frame(active_frame_name);
        let new_frame = old_frame.clone();
        old_frame.before(new_frame);
        frame_container.animate(
            {
                left: "-=" + $("#form-container").outerWidth()
            },
            animation_duration,
            () => {
	            frame_container.css("left", 0);
                old_frame.remove();
	            get_frame(active_frame_name).find("input").eq(0).focus();
            }
        );
    }
}
