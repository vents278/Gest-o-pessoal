import { initAuth } from "./auth.js";
import { initDashboard } from "./dashboard.js";
import { initIncomes } from "./incomes.js";
import { initExpenses } from "./expenses.js";

const app = document.querySelector("#app");

async function loadPage(path) {
  const res = await fetch(path);
  app.innerHTML = await res.text();
  const token = localStorage.getItem("access_token");
  if (path.includes("login.html")) { initAuth(app); return; }
  if (!token) { window.location.hash = "#/login"; return; }
  if (path.includes("dashboard.html")) initDashboard(app);
  if (path.includes("incomes.html")) initIncomes(app);
  if (path.includes("expenses.html")) initExpenses(app);
}

function router() {
  const hash = window.location.hash || "#/login";
  const map = {
    "#/login": "./pages/login.html",
    "#/dashboard": "./pages/dashboard.html",
    "#/incomes": "./pages/incomes.html",
    "#/expenses": "./pages/expenses.html",
  };
  loadPage(map[hash] || "./pages/login.html");
}

window.addEventListener("hashchange", router);
window.addEventListener("load", router);
