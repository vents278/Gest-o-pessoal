import { api } from "./api.js";
import { formatBRL } from "./utils.js";

export async function initExpenses(root) {
  const form = root.querySelector("#expense-form");
  const tbody = root.querySelector("#expense-table-body");
  async function load() {
    const list = await api.expenses.list();
    tbody.innerHTML = "";
    list.forEach(exp => {
      const tr = document.createElement("tr");
      tr.innerHTML = `<td>${exp.descricao}</td><td>${formatBRL(exp.valor_total)}</td><td>${exp.responsabilidade}</td><td>${exp.situacao}</td>`;
      tbody.appendChild(tr);
    });
  }
  form.addEventListener("submit", async e => {
    e.preventDefault();
    await api.expenses.create({ descricao: root.querySelector("#expense-descricao").value, valor_total: parseFloat(root.querySelector("#expense-valor").value), responsabilidade: root.querySelector("#expense-responsabilidade").value, situacao: root.querySelector("#expense-situacao").value });
    form.reset();
    await load();
  });
  root.querySelector("#logout-link").addEventListener("click", e => { e.preventDefault(); localStorage.removeItem("access_token"); window.location.hash = "#/login"; });
  await load();
}
