document.addEventListener("DOMContentLoaded", function() {
    const welcomeText = document.getElementById("welcome-text");
    const headline = document.getElementById("headline");

    // Wait for the typewriter animation to end before showing the headline
    welcomeText.addEventListener('animationend', function() {
        headline.style.opacity = 1; // Make the headline visible
    });
});
