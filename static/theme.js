function toggleTheme() {
  const body = document.body;
  body.classList.toggle("light");
  body.classList.toggle("dark");

  if (body.classList.contains("light")) {
    localStorage.setItem("theme", "light");
  } else {
    localStorage.setItem("theme", "dark");
  }
}

window.onload = () => {
  const saved = localStorage.getItem("theme");
  if (saved === "light") {
    document.body.classList.remove("dark");
    document.body.classList.add("light");
  }
};
