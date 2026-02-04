// contentScript.js
(() => {
  try {
    const url = window.location.href;
    const title = document.title || '';
    const bodyText = (document.body && document.body.innerText) ? document.body.innerText.slice(0, 5000) : '';
    // simple page signals (do not send full body to server without consent)
    const hasPassword = !!document.querySelector('input[type="password"]');
    const numForms = document.forms ? document.forms.length : 0;
    const hasIframe = !!document.querySelector('iframe');

    // Send to background for decision (background may call server)
    chrome.runtime.sendMessage({
      type: "PAGE_DATA",
      payload: { url, title, hasPassword, numForms, hasIframe, snippet: bodyText.slice(0,1000) }
    });
  } catch (e) {
    // fail quietly
    console.warn("contentScript error", e);
  }
})();
