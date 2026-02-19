// ============================================
// THEME INITIALIZATION (Runs Immediately)
// ============================================

(function () {
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme) {
    document.body.classList.toggle("light", savedTheme === "light");
  } else {
    // Auto detect system preference
    const prefersLight = window.matchMedia(
      "(prefers-color-scheme: light)",
    ).matches;
    document.body.classList.toggle("light", prefersLight);
  }

  updateThemeIcon();
})();

// ============================================
// TOGGLE FUNCTION
// ============================================

function toggleTheme() {
  const body = document.body;
  const isLight = body.classList.toggle("light");

  localStorage.setItem("theme", isLight ? "light" : "dark");

  updateThemeIcon();
}

// ============================================
// UPDATE BUTTON ICON
// ============================================

function updateThemeIcon() {
  const btn = document.querySelector(".theme-btn");

  if (!btn) return;

  if (document.body.classList.contains("light")) {
    btn.textContent = "🌙";
    btn.title = "Switch to Dark Mode";
  } else {
    btn.textContent = "☀️";
    btn.title = "Switch to Light Mode";
  }
}

// ============================================
// SMOOTH TRANSITION FIX
// ============================================

// Prevent abrupt theme change on load
window.addEventListener("load", () => {
  document.body.style.transition = "background 0.3s ease, color 0.3s ease";
});
