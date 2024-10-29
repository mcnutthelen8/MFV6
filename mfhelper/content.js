// Function to handle Feyorra
function claimFeyorra() {
  const verifiedBadgeFeyorra = document.querySelector("div.mb-2.badge.bg-success");
  const claimButtonFeyorra = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeFeyorra && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  }
  return false;
}

// Function to handle Earn Pepe
function claimEarnPepe() {
  const verifiedBadgeEarnPepe = document.querySelector("div.mb-16.badge.hp-text-color-black-100.hp-bg-success-3");
  const claimButtonEarnPepe = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeEarnPepe && claimButtonEarnPepe) {
    console.log(" Verified on earn-pepe.com - Clicking the Claim button...");
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
    console.log("=4 404 Error Detected - Redirecting to Google...");
    window.location.href = "https://feyorra.site/member/faucet";
  }
}


// Check and claim every 2 seconds
function checkAndClaim() {
  handleAlerts(); // Check and handle alerts
  handle404Errors(); // Check and handle 404 errors
  //handleInfiniteLoading(); // Handle long page loading

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

// Run the check every 1 second
const claimInterval = setInterval(checkAndClaim, 1000);
