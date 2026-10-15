import { api } from "./api.js";
import { formatBRL } from "./utils.js";

export async function initIncomes(root) {
  const form = root.querySelector("#income-form");
  const tbody = root.querySelector("#income-table-body");
  async function load() {
    const list = await api.incomes.list();
    tbody.innerHTML = "";
    list.forEach(inc => {
      const tr = document.createElement("tr");
      tr.innerHTML = `<td>${inc.descricao}</td><td>${formatBRL(inc.valor)}</td><td>${inc.status}</td>`;
      tbody.appendChild(tr);
    });
  }
  form.addEventListener("submit", async e => {
    e.preventDefault();
    await api.incomes.create({ descricao: root.querySelector("#income-descricao").value, valor: parseFloat(root.querySelector("#income-valor").value), status: root.querySelector("#income-status").value });
    form.reset();
    await load();
  });
  root.querySelector("#logout-link").addEventListener("click", e => { e.preventDefault(); localStorage.removeItem("access_token"); window.location.hash = "#/login"; });
  await load();
}
