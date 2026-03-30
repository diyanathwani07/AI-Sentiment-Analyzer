// JS Loaded confirmation
console.log("JS Connected Successfully");

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector("button");
    const textarea = document.querySelector("textarea");

    // 🔥 Button loading animation
    if (form && button) {
        form.addEventListener("submit", function () {
            button.innerText = "Analyzing...";
            button.classList.add("loading");
        });
    }

    // ✨ Auto-expand textarea (typing effect)
    if (textarea) {
        textarea.addEventListener("input", function () {
            this.style.height = "auto";
            this.style.height = this.scrollHeight + "px";
        });
    }

});