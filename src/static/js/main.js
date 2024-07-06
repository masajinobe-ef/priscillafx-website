// This code is licensed under the GPL-3.0 license
// Written by masajinobe-ef

document.addEventListener("DOMContentLoaded", function () {
  // Рандомный background
  var backgrounds = [
    // "bg1.jpg",
    "bg2.jpg",
    // "bg3.jpg",
    // "bg4.jpg",
    // "bg5.jpg"
  ];
  var usedBackgrounds = [];

  if (backgrounds.length > 0) {
    if (usedBackgrounds.length === backgrounds.length) {
      console.log("All backgrounds have been used.");
      return;
    }

    var availableBackgrounds = backgrounds.filter(function (bg) {
      return !usedBackgrounds.includes(bg);
    });

    var randomIndex = Math.floor(Math.random() * availableBackgrounds.length);
    var selectedBackground = availableBackgrounds[randomIndex];

    usedBackgrounds.push(selectedBackground);

    document.body.style.background = 'url("/static/img/background/'.concat(
      selectedBackground,
      '") no-repeat center/cover'
    );
  } else {
    console.log("No backgrounds available.");
  }
});
