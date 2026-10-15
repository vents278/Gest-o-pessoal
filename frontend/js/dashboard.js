import { api } from "./api.js";
import { formatBRL } from "./utils.js";

export async function initDashboard(root) {
  try {
    const [me, summary] = await Promise.all([api.me(), api.dashboard.summary()]);
    root.querySelector("#user-name").textContent = me.nome_completo;
    root.querySelector("#user-email").textContent = me.email;
    root.querySelector("#kpi-receita-total").textContent = formatBRL(summary.receita_total_casal);
    root.querySelector("#kpi-receita-individual").textContent = formatBRL(summary.receita_individual);
    root.querySelector("#kpi-despesas-total").textContent = formatBRL(summary.despesas_totais);
    root.querySelector("#kpi-despesas-compartilhadas").textContent = formatBRL(summary.despesas_compartilhadas);
    root.querySelector("#kpi-minha-parte").textContent = formatBRL(summary.minha_parte_pendente_compartilhada);
  } catch (err) {
    window.location.hash = "#/login";
  }
  root.querySelector("#logout-link").addEventListener("click", e => {
    e.preventDefault();
    localStorage.removeItem("access_token");
    window.location.hash = "#/login";
  });
}
