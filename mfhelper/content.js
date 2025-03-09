


function claimEarnPepe() {
  // Find the element with the text "Verified!"
  //const verifiedBadgeFeyorra = document.evaluate(
  //  "//*[contains(text(), 'Verified!')]",
  //  document,
   // null,
  //  XPathResult.FIRST_ORDERED_NODE_TYPE,
  //  null
  //).singleNodeValue;

  // Find error messages within the form
  // Find the claim button
  const claimButtonEarn = document.querySelector("button#ClaimBtn");

  function checkFormForIcons() {
      let xpathExpression = `//form[@method="POST"]//*[contains(@class, "bxs-") or 
          contains(@class, "bx-") or contains(@class, "la-") or 
          contains(@class, "fa-") or contains(@class, "fas fa-") or 
          contains(@class, "far fa-") or contains(@class, "ri-") or 
          contains(@class, "ti ti-") or contains(@class, "bi bi-") or 
          contains(text(), "Pick the one clear, similar icon from above.")]`;

      // Evaluate XPath expression
      let matchingElements = document.evaluate(xpathExpression, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);

      let filteredElements = [];
      console.log("All matching elements with computed styles:");

      for (let i = 0; i < matchingElements.snapshotLength; i++) {
          let element = matchingElements.snapshotItem(i);
          let style = window.getComputedStyle(element);

          let opacity = parseFloat(style.opacity); // Convert opacity to a number
          let filter = style.filter.trim(); // Trim spaces
          let filterOpacityMatch = filter.match(/opacity\(([\d.]+)\)/);
          let filterOpacity = filterOpacityMatch ? parseFloat(filterOpacityMatch[1]) : null;

          // Keep elements where opacity is > 0.5 OR no filter opacity is applied
          if ((filterOpacity === null || filterOpacity > 0.5) && opacity > 0.5) {
              filteredElements.push(element);
          }
      }

      ///onsole.log("Filtered elements (opacity > 0.5):", filteredElements);

      // Return false if more than 6 elements, otherwise true
      return filteredElements.length <= 6;
  }


  const checkFormFor = checkFormForIcons();
  console.log("checkFormForIcons: ",checkFormFor); // Returns true if found, otherwise false

  const base64Images = [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABZElEQVRYhc1YSxbDIAjEvt4p99/hqezC15QCAqJJO6tEh8+AT02grQERFz3cEAK25OEinahhKKdG5KjIlXLGbfGNIJM6N6ymO7lrfcb7sOKz46blehGYqqTIG/aV7ZA5w2jalXeRftXtVGISH5GzxnE+AADwJQNvuMxZzxKPM9hxHCBQSimlyGeJWqs7cg52Pz3L/qySI0BEnxQvVYTPtvXFDrgI+nnm6kdb2khDZHXP8dYaa1etlS4fyjQCscEQqGK1A0A6KevHwqsFlq9nFVhcwzASaASdQdWOUmGV6nmr9xWZyig5VSQLxCLmRcrArPBdj5pfRGT3EBRpcLaJtGOrq4hBSlLJcg27gRh/p8imtdeoOt2HbIcjplplOT5CkTb/D7Ytu3iw9/ShnEDw/iAxpRBgx4mcw3WfbHLqDpH2p2Pk8r1YkaHIqf8Of4ivo37W4LdIZIKI/rUu7T1ou7eCqrcXOd5OshXZ9OEAAAAASUVORK5CYII=",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXB",
    ];
    const base64Images2 = [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUgAAAAXCAIAAADm2UHyAAAACXB",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV0AAAAXCAIAAAAnXgteAAAACXBI"
    ];
  //Check if any image on the page matches a base64 image from the list
  const imageExists = [...document.querySelectorAll("img")].some(img => {
    return base64Images.some(prefix => img.src.startsWith(prefix));
  });
  const imageExists2 = [...document.querySelectorAll("img")].some(img => {
    return base64Images2.some(prefix => img.src.startsWith(prefix));
  });

  console.log("imageExists: ", imageExists);
  console.log("imageExists2: ", imageExists2);
  // If there's an error message, log and stop execution
  //if (imageExists2  && claimButtonEarn || imageExists3  && claimButtonEarn || imageExists  && claimButtonEarn) {
  if (imageExists && claimButtonEarn) {
    console.log("verified on ");
    claimButtonEarn.click();
    return true; // Stop further execution
  }

  // If CAPTCHA is still loading, do not proceed
  //if (loadingCaptcha) {
  //  console.log("Loading CAPTCHA, please wait...");
  //  return false; // Stop execution until CAPTCHA is loaded
  //}

  // If the verification badge is found and the claim button exists, click it
  //if (verifiedBadgeFeyorra && claimButtonEarn) {
  //  console.log("Verified on claimEarnPepe.site - Clicking the Claim button...");
  //  claimButtonEarn.click();
  //  return true; // Stop the interval if the claim button is clicked
  //}

  return false;
}

// Function to automatically close alerts
function handleAlerts() {
  if (window.confirm) {
    window.confirm = () => true; // Auto confirm all alerts
  }
  if (window.alert) {
    window.alert = () => {}; // Auto dismiss alerts
  }
  if (window.prompt) {
    window.prompt = () => null; // Auto dismiss prompts
  }
}

// Function to check for 404 and redirect to Google
function handle404Errors() {
  const pageTitle = document.title.toLowerCase();
  if (pageTitle.includes("404") || pageTitle.includes("not found")) {
    console.log("404 Error Detected - Redirecting to Google...");
    window.location.href = "https://feyorra.site/member/faucet";
  }
}

// Function to handle claims on Feyorra and Earn Pepe sites
function checkAndClaim() {

  const validURLs = [
    "https://feyorra.site/",
    "https://earn-pepe.com/",
    "https://earn-trump.com/",
    "https://earn-bonk.com/",
    "https://claimcoin.in/faucet/"
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
            const response = await fetch("https://api.ipify.org?format=json");
            const data = await response.json();
            const currentIP = data.ip;
  
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
  
  handleAlerts(); // Check and handle alerts
  handle404Errors(); // Check and handle 404 errors

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
