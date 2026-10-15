const API_BASE = "/api/v1";

function getToken() {
  return localStorage.getItem("access_token");
}

async function request(path, options = {}) {
  const token = getToken();
  const headers = {};
  if (token && !options.noAuth) headers["Authorization"] = `Bearer ${token}`;
  if (options.body && !(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }
  Object.assign(headers, options.headers || {});
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  if (!res.ok) {
    let detail = "Erro na requisição";
    try {
      const data = await res.json();
      detail = data.detail || detail;
    } catch (e) {
      detail = res.statusText;
    }
    throw new Error(detail);
  }
  if (res.status === 204) return null;
  const ct = res.headers.get("content-type") || "";
  if (ct.includes("application/json")) return res.json();
  return res.blob();
}

export const api = {
  register: (p) => request("/auth/register", { method: "POST", body: JSON.stringify(p) }),
  login: (p) => request("/auth/login", { method: "POST", body: JSON.stringify(p) }),
  me: () => request("/users/me"),
  incomes: { list: () => request("/incomes/"), create: (p) => request("/incomes/", { method: "POST", body: JSON.stringify(p) }) },
  expenses: { list: () => request("/expenses/"), create: (p) => request("/expenses/", { method: "POST", body: JSON.stringify(p) }) },
  dashboard: { summary: () => request("/dashboard/summary") },
};
