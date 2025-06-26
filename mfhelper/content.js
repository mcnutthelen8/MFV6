// Inject code into page context to override timer and interaction checks safely
(function inject() {
  const sourceCode = `
    // Stop any existing claim timer interval to prevent countdown reset
    if (window.claimTimerInterval) {
      clearInterval(window.claimTimerInterval);
      window.claimTimerInterval = null;
    }

    // Lock remainingTime at 0 to stop countdown
    Object.defineProperty(window, 'remainingTime', {
      get: () => 0,
      set: () => {},
      configurable: true
    });

    // Patch isUserInteraction to always return true for seamless form submit
    window.isUserInteraction = () => true;

    // Override startClaimTimer to instantly enable button & update text
    window.startClaimTimer = function() {
      const claimBtn = document.getElementById('ClaimBtn');
      const claimBtnText = document.getElementById('loginBtnText');
      if (claimBtn && claimBtnText) {
        claimBtn.disabled = false;
        claimBtn.classList.remove('disabled');
        claimBtnText.textContent = 'Claim';
      }
    };

    // Immediately run patched startClaimTimer so button is enabled on page load
    window.startClaimTimer();
  `;

  const script = document.createElement('script');
  script.textContent = sourceCode;
  (document.documentElement || document.head || document.body).appendChild(script);
  script.remove();
})();

// Fallback: In case DOM is not ready at document_start, enable button after 1 second
setTimeout(() => {
  const claimBtn = document.getElementById('ClaimBtn');
  const claimBtnText = document.getElementById('loginBtnText');
  if (claimBtn && claimBtnText) {
    claimBtn.disabled = false;
    claimBtn.classList.remove('disabled');
    claimBtnText.textContent = 'Claim';
  }
}, 1000);


function claimEarnPepe() {

 
  const base64Images = [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABZElEQVRYhc1YSxbDIAjEvt4p99/hqezC15QCAqJJO6tEh8+AT02grQERFz3cEAK25OEinahhKKdG5KjIlXLGbfGNIJM6N6ymO7lrfcb7sOKz46blehGYqqTIG/aV7ZA5w2jalXeRftXtVGISH5GzxnE+AADwJQNvuMxZzxKPM9hxHCBQSimlyGeJWqs7cg52Pz3L/qySI0BEnxQvVYTPtvXFDrgI+nnm6kdb2khDZHXP8dYaa1etlS4fyjQCscEQqGK1A0A6KevHwqsFlq9nFVhcwzASaASdQdWOUmGV6nmr9xWZyig5VSQLxCLmRcrArPBdj5pfRGT3EBRpcLaJtGOrq4hBSlLJcg27gRh/p8imtdeoOt2HbIcjplplOT5CkTb/D7Ytu3iw9/ShnEDw/iAxpRBgx4mcw3WfbHLqDpH2p2Pk8r1YkaHIqf8Of4ivo37W4LdIZIKI/rUu7T1ou7eCqrcXOd5OshXZ9OEAAAAASUVORK5CYII=",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXB",
    ];

  //Check if any image on the page matches a base64 image from the list
  const imageExists = [...document.querySelectorAll("img")].some(img => {
    return base64Images.some(prefix => img.src.startsWith(prefix));
  });

  console.log("imageExists: ", imageExists);


  const claimButtonEarn = document.querySelector("button#ClaimBtn");
  const claimTextEl = document.querySelector('#loginBtnText');

  if (claimButtonEarn && claimTextEl && imageExists) {
    const text = claimTextEl.textContent.trim();
  

    const waitMatch = text.match(/^Please Wait (\d+)s$/);

    if (text === 'Claim') {
     
      claimButtonEarn.click();
      return true;
    } else if (waitMatch && parseInt(waitMatch[1]) <= 4) {

      claimButtonEarn.click();
      return true;
    } else {
      console.log('Still waiting. Not safe to click.');
    }
  } else {
    console.log('Claim button or text not found or image condition failed');
  }
  const verifyCheckbox = document.querySelector("#verifyCheckbox");

  const isVisible = (el) => {
    return el && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
  };
  if (verifyCheckbox && isVisible(verifyCheckbox)) {
    console.log("verifyCheckbox is visible, clicking...");
    verifyCheckbox.click();
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
