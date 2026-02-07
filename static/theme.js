function toggleTheme() {
    document.body.classList.toggle("light");
    localStorage.setItem("theme",
        document.body.classList.contains("light") ? "light" : "dark"
    );
}

window.onload = function () {
    if (localStorage.getItem("theme") === "light") {
        document.body.classList.add("light");
    }
};
