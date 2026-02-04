// background.js
const SERVER_URL = "http://localhost:8000/predict";
// change to your server

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "PAGE_DATA") {
    const payload = message.payload;
    // call prediction API
    fetch(SERVER_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: payload.url, title: payload.title, hasPassword: payload.hasPassword, numForms: payload.numForms, hasIframe: payload.hasIframe })
    })
    .then(r => r.json())
    .then(json => {
      // store per-tab result so popup can read it
      const tabId = sender.tab?.id || "last";
      const key = `result-${tabId}`;
      chrome.storage.session?.set?.({ [key]: json });
      // optionally show badge if phishing high prob
      try {
        if (json.probability >= 0.8) {
          chrome.action.setBadgeText({ text: "PH", tabId: sender.tab.id });
          chrome.action.setBadgeBackgroundColor({ color: "#FF3333", tabId: sender.tab.id });
        } else {
          chrome.action.setBadgeText({ text: "", tabId: sender.tab.id });
        }
      } catch (e) {}
    })
    .catch(err => {
      console.error("Prediction fetch error", err);
    });
  }
});
