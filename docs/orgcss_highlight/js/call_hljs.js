var hlf = function () {
    Array.prototype.forEach.call(
	document.querySelectorAll("pre.src"),
	function (t) {
	    var e;
	    e = t.getAttribute("class"),
            e = e.replace(/src-(\w+)/, "src-$1 $1"),
            console.log(e),
            t.setAttribute("class", e),
            hljs.highlightBlock(t);
	},
    );
};
addEventListener("DOMContentLoaded", hlf);
