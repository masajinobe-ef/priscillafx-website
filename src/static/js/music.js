// This code is licensed under the GPL-3.0 license
// Written by masajinobe-ef

document.addEventListener("DOMContentLoaded", function () {
  // Музыка
  var audio = new Audio("/static/audio/BoT_bg.mp3");
  audio.volume = 0.3;

  var isMuted = false;

  document.getElementById("music").addEventListener("click", function () {
    if (isMuted) {
      audio.volume = 0.3;
      isMuted = false;
    } else {
      audio.volume = 0;
      isMuted = true;
    }

    if (audio.paused) {
      audio.play().catch(function (error) {
        console.log("Autoplay was prevented: " + error);
      });
    } else {
      audio.pause();
    }
  });

  // Auto play the music when the website loads
  audio.play().catch(function (error) {
    console.log("Autoplay was prevented: " + error);
  });
});
