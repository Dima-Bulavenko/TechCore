document.addEventListener("DOMContentLoaded", function () {
    var navbar = document.getElementById("navbar");
    var mainContent = document.getElementById("main-content");

    function adjustPadding() {
        var navbarHeight = navbar.offsetHeight;
        mainContent.style.paddingTop = navbarHeight + "px";
    }

    // Adjust padding on page load
    adjustPadding();

    // Adjust padding on window resize
    window.addEventListener("resize", adjustPadding);
});
