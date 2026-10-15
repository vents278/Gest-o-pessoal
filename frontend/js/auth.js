import { api } from "./api.js";

export function initAuth(root) {
  const loginForm = root.querySelector("#login-form");
  const registerForm = root.querySelector("#register-form");
  const tabs = root.querySelectorAll(".auth-tab");
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      if (tab.dataset.tab === "login") {
        loginForm.classList.remove("hidden");
        registerForm.classList.add("hidden");
      } else {
        loginForm.classList.add("hidden");
        registerForm.classList.remove("hidden");
      }
    });
  });
  loginForm.addEventListener("submit", async e => {
    e.preventDefault();
    const email = root.querySelector("#login-email").value;
    const senha = root.querySelector("#login-senha").value;
    const data = await api.login({ email, senha });
    localStorage.setItem("access_token", data.access_token);
    window.location.hash = "#/dashboard";
  });
  registerForm.addEventListener("submit", async e => {
    e.preventDefault();
    const nome_completo = root.querySelector("#register-nome").value;
    const email = root.querySelector("#register-email").value;
    const senha = root.querySelector("#register-senha").value;
    const nome_grupo = root.querySelector("#register-grupo").value;
    const data = await api.register({ nome_completo, email, senha, nome_grupo });
    localStorage.setItem("access_token", data.access_token);
    window.location.hash = "#/dashboard";
  });
}
