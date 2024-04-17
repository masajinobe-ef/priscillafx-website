document.addEventListener("DOMContentLoaded", function () {
    var backgrounds = ["bg2.jpg"];
    var randomIndex = Math.floor(Math.random() * backgrounds.length);
    var selectedBackground = backgrounds[randomIndex];
    document.body.style.background = "url(\"/static/img/bg/".concat(selectedBackground, "\") no-repeat center/cover");
});
