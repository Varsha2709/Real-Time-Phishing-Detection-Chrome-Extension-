document.addEventListener("DOMContentLoaded", async () => {
  const [tab] = await chrome.tabs.query({
    active: true,
    lastFocusedWindow: true
  });

  const key = "result-" + tab.id;

  chrome.storage.session.get([key], (res) => {
    const r = res[key];

    const statusEl = document.getElementById("status");
    const scoreEl = document.getElementById("score");

    if (!r) {
      statusEl.textContent = "No data yet";
      return;
    }

    // Convert probability to percentage
    const percent = (r.probability * 100).toFixed(2);

    if (r.verdict === "benign") {
      statusEl.innerHTML = "Safe ✅";
      statusEl.style.color = "green";
    } else {
      statusEl.innerHTML = "Phishing ⚠️";
      statusEl.style.color = "red";
    }

    scoreEl.innerHTML = `Phishing Risk: <b>${percent}%</b>`;
  });

  document.getElementById("report").onclick = () => {
    alert("Reported (demo)");
  };
});
