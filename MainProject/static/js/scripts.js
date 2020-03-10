

/*==============================JS for FOCUSER==================================*/
var focuserBg =
document.getElementsByClassName('focuser_background')[0];
var apod_img =
document.getElementsByClassName('apod_img')[0];
console.log(focuserBg);

/* Function is called on load. It's placed in the body tag of templates/base.html */
function focus() {
    if (focuserBg != null) {
    focuserBg.classList.add('focused');
    }
    if (apod_img != null) {
    apod_img.classList.add('apod_img_transition');
    console.log("asdasd");
    }
}

/*============================== END JS for FOCUSER==================================*/