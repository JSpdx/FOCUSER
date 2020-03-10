

/*==============================JS for FOCUSER==================================*/
var focuserBg =
document.getElementsByClassName('focuser_background')[0];
var apod_img =
document.getElementsByClassName('apod_img')[0];


/* Function is called on load. It's placed in the body tag of templates/base.html */
function focus() {
    if (focuserBg != null) {        /* these IF statements keep errors from being thrown. The variable is null if the class name didn't exist on that page */
    focuserBg.classList.add('focused');
    }
    if (apod_img != null) {
    apod_img.classList.add('apod_img_transition');
    console.log("asdasd");
    }
}

/*============================== END JS for FOCUSER==================================*/