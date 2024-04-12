document.addEventListener("DOMContentLoaded", function() {
    const backgrounds = [
      "bg2.jpg"
    ];

    const randomIndex = Math.floor(Math.random() * backgrounds.length);
    const selectedBackground = backgrounds[randomIndex];
    document.body.style.background = `url("/static/img/bg/${selectedBackground}") no-repeat center/cover`;
  });