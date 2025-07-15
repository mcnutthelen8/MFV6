(function inject() {
  const sourceCode = `
    try {
      // Stop claim timer if running
      if (window.claimTimerInterval) {
        clearInterval(window.claimTimerInterval);
        window.claimTimerInterval = null;
      }

      // Attempt to enable the button safely on load
      const claimBtn = document.getElementById('ClaimBtn');
      const claimBtnText = document.getElementById('loginBtnText');
      if (claimBtn && claimBtnText) {
        claimBtn.disabled = false;
        claimBtn.classList.remove('disabled');
        claimBtnText.textContent = 'Claim';
      }
    } catch (e) {
      console.error('Inject error:', e);
    }
  `;

  const script = document.createElement('script');
  script.textContent = sourceCode;
  (document.documentElement || document.head || document.body).appendChild(script);
  script.remove();
})();

// Fallback: In case DOM is not ready
setTimeout(() => {
  try {
    const claimBtn = document.getElementById('ClaimBtn');
    const claimBtnText = document.getElementById('loginBtnText');
    if (claimBtn && claimBtnText) {
      claimBtn.disabled = false;
      claimBtn.classList.remove('disabled');
      claimBtnText.textContent = 'Claim';
    }
  } catch (e) {
    console.error('Fallback error:', e);
  }
}, 1000);
// Utility for safe clicking (less detectable)
function safeClick(el) {
  if (!el) return;
  const evt = new MouseEvent('click', {
    bubbles: true,
    cancelable: true,
    view: window
  });
  el.dispatchEvent(evt);
}

// Control flags
let verifyClickAttempts = 0;
let verifyClicked2 = false;

// Base64 images to validate claim condition
const base64Images = [
  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABZElEQVRYhc1YSxbDIAjEvt4p99/hqezC15QCAqJJO6tEh8+AT02grQERFz3cEAK25OEinahhKKdG5KjIlXLGbfGNIJM6N6ymO7lrfcb7sOKz46blehGYqqTIG/aV7ZA5w2jalXeRftXtVGISH5GzxnE+AADwJQNvuMxZzxKPM9hxHCBQSimlyGeJWqs7cg52Pz3L/qySI0BEnxQvVYTPtvXFDrgI+nnm6kdb2khDZHXP8dYaa1etlS4fyjQCscEQqGK1A0A6KevHwqsFlq9nFVhcwzASaASdQdWOUmGV6nmr9xWZyig5VSQLxCLmRcrArPBdj5pfRGT3EBRpcLaJtGOrq4hBSlLJcg27gRh/p8imtdeoOt2HbIcjplplOT5CkTb/D7Ytu3iw9/ShnEDw/iAxpRBgx4mcw3WfbHLqDpH2p2Pk8r1YkaHIqf8Of4ivo37W4LdIZIKI/rUu7T1ou7eCqrcXOd5OshXZ9OEAAAAASUVORK5CYII=",
  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXB"
];

function claimEarnPepe() {
  const imageExists = [...document.querySelectorAll("img")].some(img =>
    base64Images.some(prefix => img.src.startsWith(prefix))
  );

  if (window.location.href.includes("earn-bonk.com/member/faucet")) {
    verifyClicked2 = false;

  }
  const claimButtonEarn = document.querySelector("button#ClaimBtn");
  const claimTextEl = document.querySelector("#loginBtnText");

  if (claimButtonEarn && claimTextEl && imageExists) {
    const text = claimTextEl.textContent.trim();
    const waitMatch = text.match(/^Please Wait (\d+)s$/);

    if (text === 'Claim' && !verifyClicked2) {
      safeClick(claimButtonEarn);
      verifyClicked2 = true;
      return true;
    } else if (waitMatch && !verifyClicked2 && parseInt(waitMatch[1]) <= 4) {
      safeClick(claimButtonEarn);
      verifyClicked2 = true;
    } else {
      console.log("Still waiting...");
    }
  }

  const verifyCheckbox = document.querySelector("#verifyCheckbox");
  const isVisible = el => el && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);

  if (isVisible(verifyCheckbox) && verifyClickAttempts < 3) {
      console.log("Clicking verify checkbox... Attempt:", verifyClickAttempts + 1);
      safeClick(verifyCheckbox);
      verifyClickAttempts++;
  }

  return false;
}
// Function to handle claims on Feyorra and Earn Pepe sites
function checkAndClaim() {

  const validURLs = [
    "https://feyorra.site/",
    "https://earn-pepe.com/",
    "https://earn-trump.com/",
    "https://earn-bonk.com/",
  ];
  
  const currentURL = window.location.href;
  const isTargetSite = validURLs.some(url => currentURL.startsWith(url));
  
  if (!isTargetSite) {
    console.log("This script only runs on the target sites.");
  } else {
    (async function checkIP() {
      try {
        const configResponse = await fetch(chrome.runtime.getURL("config.json"));
        const config = await configResponse.json();
        const targetIP = config.targetIP;
  
        while (true) {
          try {
            const response = await fetch("https://checkip.amazonaws.com/");
            const currentIP = (await response.text()).trim();

            //const response = await fetch("https://api.ipify.org?format=json");
            //const data = await response.json();
            //const currentIP = data.ip;
  
            console.log(`Current IP: ${currentIP}`);
  
            if (currentIP !== targetIP) {
              console.log("IP mismatch detected. Redirecting to Google.");
              window.location.href = "https://www.google.com";
              break;
            }
  
            await new Promise(resolve => setTimeout(resolve, 5000)); // Check IP every 5 seconds
          } catch (error) {
            console.error("Failed to fetch IP:", error);
          }
        }
      } catch (error) {
        console.error("Failed to fetch target IP:", error);
      }
    })();
  }
  

  if (window.location.href.includes("feyorra.site/member/faucet")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-pepe.com/member/faucet")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-bonk.com/member/faucet")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-trump.com/member/faucet")) {
    console.log("earn-trump.com.");
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  }
  console.log("checkAndClaim");
}

// Run the check every 1 second for Feyorra and Earn Pepe claims
const claimInterval = setInterval(checkAndClaim, 1000);
