(() => {
  "use strict";

  const supported = new Set(["zh-Hans", "zh-Hant-HK", "zh-Hant-TW", "en-US"]);
  const preferenceKey = "ps-pocket.language";
  const entryScript = document.currentScript;

  function savedLanguage() {
    try {
      const saved = window.localStorage.getItem(preferenceKey);
      return supported.has(saved) ? saved : null;
    } catch {
      return null;
    }
  }

  function browserLanguage() {
    const preferences = Array.isArray(navigator.languages) && navigator.languages.length
      ? navigator.languages : [navigator.language];
    for (const preference of preferences) {
      if (typeof preference !== "string") continue;
      const parts = preference.toLowerCase().replace(/_/g, "-").split("-");
      if (parts[0] === "en") return "en-US";
      if (parts[0] !== "zh") continue;
      if (parts.includes("hans")) return "zh-Hans";
      if (parts.includes("hant")) {
        return parts.includes("hk") || parts.includes("mo") ? "zh-Hant-HK" : "zh-Hant-TW";
      }
      if (parts.includes("hk") || parts.includes("mo")) return "zh-Hant-HK";
      if (parts.includes("tw")) return "zh-Hant-TW";
      return "zh-Hans";
    }
    return "en-US";
  }

  // Only shared entry URLs redirect. Explicit language URLs always stay put.
  if (entryScript && entryScript.dataset.autoLanguage === "true") {
    const routes = new Map([
      ["/ps-pocket/", ""],
      ["/ps-pocket/index.html", ""],
      ["/ps-pocket/support.html", "support.html"],
      ["/ps-pocket/privacy.html", "privacy.html"]
    ]);
    const current = window.location;
    if (routes.has(current.pathname)) {
      const language = savedLanguage() || browserLanguage();
      current.replace(`/ps-pocket/${language}/${routes.get(current.pathname)}${current.search}${current.hash}`);
      return;
    }
  }

  function rememberManualChoice() {
    document.querySelectorAll(".language-bar a[hreflang]").forEach(link => {
      link.addEventListener("click", () => {
        const language = link.getAttribute("hreflang");
        if (!supported.has(language)) return;
        try {
          window.localStorage.setItem(preferenceKey, language);
        } catch {
          // Normal links still work when browser storage is unavailable.
        }
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", rememberManualChoice, { once: true });
  } else {
    rememberManualChoice();
  }
})();
