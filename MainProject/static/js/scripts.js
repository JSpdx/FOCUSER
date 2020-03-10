

/*==============================JS for FOCUSER==================================*/
var focuserBg =
document.getElementsByClassName('focuser_background')[0];
console.log(focuserBg);

/* Function is called on load. It's placed in the body tag of templates/base.html */
function focus() {
    focuserBg.classList.add('focused');
    console.log("asdasd");
}

/*============================== END JS for FOCUSER==================================*/