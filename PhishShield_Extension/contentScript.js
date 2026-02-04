console.log("PhishShield content script loaded");

chrome.runtime.sendMessage({
  type: "PAGE_DATA",
  payload: {
    url: window.location.href,
    title: document.title,
    hasPassword: document.querySelectorAll("input[type=password]").length > 0,
    numForms: document.forms.length,
    hasIframe: document.querySelectorAll("iframe").length > 0
  }
});
