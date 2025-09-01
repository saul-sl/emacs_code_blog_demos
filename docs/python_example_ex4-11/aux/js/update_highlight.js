var hlf = function () {
    // Highlights code blocks after changing their class
    Array.prototype.forEach.call(
        document.querySelectorAll("pre.src"),
        function (t) {
            var e;
            e = t.getAttribute("class"),
	    e = e.replace(/src-(\w+)/, "src-$1 $1"),
	    console.log(e),
	    t.setAttribute("class", e),
	    hljs.highlightBlock(t);
        }
    );
};

// Wait until DOM is ready
addEventListener("DOMContentLoaded", function() {
    // Changes the Highlight.js theme
    function updateHighlightTheme(mode) {
        const link = document.querySelector('link[href*="highlight.js"]');
        if (link) {
            if (mode === "dark") {
                link.href = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/nnfx-dark.css";
            } else {
                link.href = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/googlecode.css";
            }
            // Update highlighting of block
            hlf();
        }
    }

    // Wrap nice-org-html original setMode to also update the highlight theme
    const originalSetMode = setMode;
    setMode = function(newMode) {
        originalSetMode(newMode);
        updateHighlightTheme(newMode);
    };

    // Run once on page load
    updateHighlightTheme(getMode());
});
