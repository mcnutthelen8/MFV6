

async function validate_ipaddress() {
  const validURLs = ["https://feyorra.site/", "https://earn-pepe.com/", "https://claimcoin.in/faucet"];
  const currentURL = window.location.href;

  // Check if the current URL matches the target pattern
  const isTargetSite = validURLs.some((url) => currentURL.startsWith(url));

  if (!isTargetSite) {
      console.log("This script only runs on the target sites.");
      return;
  }

  try {
      // Fetch the target IP from the JSON file
      const configResponse = await fetch(chrome.runtime.getURL("config.json"));
      const config = await configResponse.json();
      const targetIP = config.targetIP;

      // Stop the page from loading temporarily
      console.log(targetIP);

      // Fetch the current IP address before the page fully loads
      const response = await fetch("https://api.ipify.org?format=json");
      const data = await response.json();
      const currentIP = data.ip;

      // Log the current IP to the console
      console.log(`Current IP: ${currentIP}`);

      // Store IP check result in sessionStorage
      sessionStorage.setItem(currentIP, true);

      // Redirect to Google if IP does not match
      if (currentIP !== targetIP) {
          console.log("IP mismatch detected. Redirecting to Google.");
          window.location.href = "https://www.google.com";
      } else {
          console.log("IP matches the target");
          return currentIP;
          // Allow the page to reload after IP validation
          //window.location.reload();
      }
  } catch (error) {
      console.error("Failed to fetch IP address or validate:", error);
      // If there's an error, handle it gracefully and redirect to Google
      //window.location.href = "https://www.google.com";
  }
}

// Function to get the current URL
function getCurrentURL() {
  return window.location.href;
}

// Function to check if we are on a restricted page
function isOnRestrictedPage() {
  const restrictedUrls = [
    'https://www.popmack.com/prizes',
    'https://www.baymack.com/prizes',
    'https://www.popmack.com/waitfornextday',
    'https://www.baymack.com/waitfornextday'
  ];
  
  const currentURL = getCurrentURL();
  
  // Check if the current URL is exactly in the restricted URLs
  if (restrictedUrls.includes(currentURL)) {
    return true;
  }
  
  // Check if the current URL starts with the restricted path for checkinflow (baymack or popmack)
  if (currentURL.startsWith('https://www.baymack.com/checkinflow/') || 
      currentURL.startsWith('https://www.popmack.com/checkinflow/')) {
    return true;
  }

  return false;
}

// Function to check and click the "Next Video" button
function clickNextVideo() {
  if (isOnRestrictedPage()) {
    console.log("On a restricted page, skipping 'Next Video' click.");
    return false; // Skip clicking if on a restricted page
  }

  const selectors = [
    'a.retention-click.themeBtn.bluebtn#nextvideo',
    '#next-video',
    '#nextvideo',
    'a.retention-click.themeBtn',
    'a.themeBtn',
    'a.try_again'
  ];

  // Check if the captcha textarea exists
  if (document.querySelector('textarea.captcha-textarea')) {
    console.log("Captcha textarea found, skipping the 'Next Video' click.");
    return false; // Skip clicking if captcha textarea is present
  }

  // Loop through the selectors and try to find and click the button
  for (let selector of selectors) {
    const nextVideoButton = document.querySelector(selector);
    if (nextVideoButton) {
      nextVideoButton.click();
      console.log("Next Video button clicked: " + selector);
      return true; // Exit once a button is clicked
    }
  }

  console.log("Next Video button not found");
  return false;
}

// Function to periodically check for the "Next Video" button every 1 second
function startCheckingForNextVideo() {
  setInterval(() => {
    clickNextVideo();
  }, 1000); // Check every 1 second
}

// Function to handle Feyorra claims
function claimFeyorra() {
  const verifiedBadgeFeyorra = document.querySelector(".mb-2.badge.bg-success");
  const claimButtonFeyorra = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeFeyorra && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  }
  return false;
}

// Function to handle Earn Pepe claims
function claimEarnPepe() {
  const verifiedBadgeEarnPepe = document.querySelector(".mb-16.badge.hp-text-color-black-100.hp-bg-success-3");
  const claimButtonEarnPepe = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeEarnPepe && claimButtonEarnPepe) {
    console.log(" Verified on earn-pepe.com - Clicking the Claim button...");
    claimButtonEarnPepe.click();
    return true; // Stop the interval if the claim button is clicked
  }
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
  handleAlerts(); // Check and handle alerts
  handle404Errors(); // Check and handle 404 errors
  validate_ipaddress();

  if (window.location.href.includes("feyorra.site")) {
    if (claimFeyorra()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-pepe.com")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  }
}

// Start checking for "Next Video" button
startCheckingForNextVideo();

// Run the check every 1 second for Feyorra and Earn Pepe claims
const claimInterval = setInterval(checkAndClaim, 1000);
