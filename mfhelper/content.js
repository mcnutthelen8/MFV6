
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
  const verifiedBadgeFeyorra = document.querySelector("div.mb-2.badge.bg-success");
  const successcloudfl = document.querySelector("span#success-text");
  const claimButtonFeyorra = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeFeyorra && claimButtonFeyorra || successcloudfl && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  }
  else if (successcloudfl && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  } else {
    
  }
  return false;
}

// Function to handle Earn Pepe claims
function claimEarnPepe() {
  const verifiedBadgeEarnPepe = document.querySelector("div.mb-16.badge.hp-text-color-black-100.hp-bg-success-3");
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
function createNotification(message) {
  const notification = document.createElement('div');
  notification.id = 'captcha-solver-notification';
  notification.style.cssText = `
      position: fixed;
      top: 10px;
      left: 10px;
      background-color: rgba(0, 0, 0, 0.8);
      color: white;
      padding: 15px;
      border-radius: 8px;
      z-index: 9999;
      font-family: sans-serif;
      box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
      display: flex;
      align-items: center;
  `;

  const messageSpan = document.createElement('span');
  messageSpan.textContent = message;
  notification.appendChild(messageSpan);

  const closeButton = document.createElement('button');
  closeButton.textContent = '×';
  closeButton.style.cssText = `
      margin-left: 10px;
      background: transparent;
      border: none;
      color: white;
      font-size: 1.2em;
      cursor: pointer;
  `;
  closeButton.addEventListener('click', () => notification.remove());
  notification.appendChild(closeButton);

  document.body.appendChild(notification);

  setTimeout(() => {
      if (notification.parentNode) notification.remove();
  }, 1000);
}

async function getCoins() {
  let coins = null;

  try {
      // Determine sitekey based on page URL
      const url = window.location.href;

      let sitekey = null;
      if (url.includes("earn-pepe.com")) {
          sitekey = 1;
      } else if (url.includes("feyorra.site")) {
          sitekey = 2;
      } else if (url.includes("claimcoin.in")) {
          sitekey = 3;
      } else {
          console.log("Unsupported site.");
          return false;
      }

      // Process based on sitekey
      if (sitekey === 1) {
          let selectElement = document.querySelector('small span span');
          if (selectElement) {
              coins = selectElement.textContent.trim();
          } else {
              console.log(`Sitekey:${sitekey} not found`);
          }
      }

      if (sitekey === 2) {
          let selectElement = document.querySelector('select.form-select option[selected]');
          if (selectElement) {
              let selectedText = selectElement.textContent.trim();
              console.log(`Selected option text: ${selectedText}`);
              coins = selectedText;
          } else {
              console.log(`Sitekey:${sitekey} not found`);
          }
      }

      if (sitekey === 3) {
          let element = document.querySelector('div.col-md-6.col-xl-3:nth-child(4) p.lh-1.mb-1.font-weight-bold');
          if (element) {
              coins = element.textContent.trim();
          } else {
              console.log(`Sitekey:${sitekey} not found`);
          }
      }

      console.log(`SiteKey${sitekey}: ${coins}`);

      // Handle specific processing for sitekey 3
      if (sitekey === 3 && coins && coins.includes('/')) {
          let numerator = coins.split('/')[0];
          return numerator;
      }

      // Extract numeric value
      let numericValue = coins && coins.match(/\d+\.\d+/);
      if (numericValue) {
          console.log(`SiteKey${sitekey}: ${coins}`);
          return parseFloat(numericValue[0]);
      }

      return false;
  } catch (error) {
      console.error(`ERR on GetCoins | ${error.message}`);
  }

  return false;
}
async function solveIconCaptcha() {
  try {
      // Check if the current URL matches the given URLs
      const url = window.location.href;
      let sitekey = null;
      const ipAddress = await validate_ipaddress();
      console.log("Extracted IP Address:", ipAddress);

      if (url.includes("earn-pepe.com")) {
          sitekey = 1;
      } else if (url.includes("feyorra.site")) {
          sitekey = 2;
      } else if (url.includes("claimcoin.in")) {
          sitekey = 3;
      } else {
          console.log("Unsupported site.");
          return false;
      }

      // Get coin value regardless of captcha presence
      let coins = await getCoins(); // Wait for the result from getCoins
      console.log("Extracted Coins:", coins);

      // Example IP address retrieval (replace with actual IP logic if needed)


      // Check for captcha icons
      const captchaIcons = document.querySelectorAll('[class*="fas fa-"]');

      if (sitekey === 3) {
          console.log("No captcha icons found on this page.");
          // No captcha, still return coin and IP values
          const clipboardText = `${coins} and is is ${ipAddress}`;
          console.log("Clipboard Text:", clipboardText);

          // Copy to clipboard
          await navigator.clipboard.writeText(clipboardText)
              .then(() => {
                  console.log("Text copied to clipboard:", clipboardText);
                  createNotification(`Text copied: ${clipboardText}`);
              })
              .catch((err) => {
                  console.error("Failed to copy text to clipboard:", err);
              });

          return true;
      }else{

      // Process captcha if present
      for (const captchaIcon of captchaIcons) {
          if (captchaIcon.style.length > 0) continue;

          const captchaIconClasses = captchaIcon.className.split(' ').filter(cls => cls.startsWith("fa-"));
          if (!captchaIconClasses) continue;

          const captchaIconClass = captchaIconClasses[0];
          const iconOptions = document.querySelectorAll('i[class*="fas fa-"]');

          if (iconOptions.length === 0) {
              console.log("No icon options found on this page.");
              return false;
          }

          for (const option of iconOptions) {
              if (option.style.length > 0) continue;
              if (option.classList.contains(captchaIconClass)) {
                  try {
                      let index = 0;
                      for (const otherOption of iconOptions) {
                          if (otherOption === option) {
                              break;
                          }
                          index++;
                      }

                      const rect = option.getBoundingClientRect();
                      const coordinates = {
                          x: rect.left + window.scrollX,
                          y: rect.top + window.scrollY
                      };

                      console.log(`Matching icon found at index: ${index}`);
                      console.log(`Element coordinates: X=${coordinates.x}, Y=${coordinates.y}`);

                      // Prepare the text to copy
                      const clipboardText = `${coins} and x is ${coordinates.x} and ip is ${ipAddress}`;
                      console.log("Clipboard Text:", clipboardText);

                      // Copy to clipboard
                      await navigator.clipboard.writeText(clipboardText)
                          .then(() => {
                              console.log("Text copied to clipboard:", clipboardText);
                              createNotification(`Text copied: ${clipboardText}`);
                          })
                          .catch((err) => {
                              console.error("Failed to copy text to clipboard:", err);
                          });

                      return true; // Return after processing captcha
                  } catch (clickError) {
                      console.error("Error processing icon:", clickError);
                  }
              }
          }
      }}

      console.log("No matching icon found.");
      return false;
  } catch (error) {
      console.error("Error solving captcha:", error);
      return false;
  }
}

// Function to handle claims on Feyorra and Earn Pepe sites
function checkAndClaim() {
  
  handleAlerts(); // Check and handle alerts
  handle404Errors(); // Check and handle 404 errors
  solveIconCaptcha();

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








