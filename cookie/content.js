(function () {
    // Blocked host keywords
    const blockedHosts = [
        "huggingface.co",
        "huggingface",
        "mediafire.com",
        "gamemodding.com",
        "gamemodding",
        "gta5-mods.com",
        "gta5-mods",
        "aether.mom",
"limewire",
"dogegamer",
        "hianime.to",
        "hianime",
        "4anime.gg",
        "4anime",
        "simkl.com",
        "simkl",
        "aliexpress",
        "animekai.me",
        "animekai.to",
        "animekai",
        "animetosho.org",
        "codepen.io",
        "github.com",
        "megaup.site",
        "pastebin.com",
        "simkl.com",
        "vikingf1le.us.to",
        "vikingfile.com",

        "explore.org",
        "dynamicslab",
        "demo.dynamicslab.ai",
        "learn-anything",
        "hacksplaining",
        "ifixit.com",
        "human.biodigital",
        "photoskop.com",
        "typingclub",
        "myemulator",
        "remove.photos",
        "secretflixcodes",
        "3dtuning",
        "workout.cool",
        "x-minus",
        "buildcores",
        "yoprintables",
        "remusic.ai",
        "chronas",
        "faceonlive",

        "pointerpointer.com",
        "neal.fun",
        "onemillioncheckboxes.com",
        "staggeringbeauty.com",
        "eelslap.com",
        "shademap.co",
        "homicide.watch",
        "worldometers.info",
        "webwithoutwords.com",
        "cookingforengineers.com",
        "notalwaysright.com",
        "artofmanliness.com",
        "cracked.com",
        "quickdraw.withgoogle.com",
        "play2048.co",
        "9gag.com",
        "iwastesomuchtime.com",
        "stellarium-web.org",
        "fallingfalling.com",
        "zoomquilt.org",
        'mediafire',
        'filebin',
        "patreon.com",
        "getintopc.com",
        "mega.nz",
        "drive.google.com",
        "vidu.com",
        "drive.usercontent.google.com",
        "gtaxscripting.blogspot.com",

        "moewalls.com",
        "cursify.vercel.app",
        'contentcore.xyz',
        'pixelmotion.art',
        'catbox.moe',
        'litterbox.catbox.moe',
        'napkin.ai',
        'wolframalpha.com',
        'spline.design',
        'freesewing.eu',
        'chefgpt.xyz',
        'asciiart.eu',

        "docs.google.com",
        "thenewscasts.com"
        
    ];

    // Function to check if current hostname matches blocked list
    function shouldClose(hostname) {
        return blockedHosts.some(domain => hostname.includes(domain));
    }

    const currentHost = window.location.hostname.toLowerCase();

    if (shouldClose(currentHost)) {
        console.log("Blocked domain detected:", currentHost);



        // Close the tab (requires background.js to handle tab closing)
        chrome.runtime.sendMessage({ action: "closeTab" });
    }
})();
(function() {
  // 🔹 Define reusable site groups
  const siteGroups = {
    common: [
      'pubnotepad.com','telegram.org','reddit.com','quora.com','tiktok.com',
      'facebook.com','codepen.io','discourse.julialang.org','pinpaste.com','pinterest.com'
    ],
    anime: [
      'pubnotepad.com','animeforums.net','forums.animeuknews.net','telegram.org',
      'novanon.net','pinpaste.com','reddit.com','quora.com','site.trooporiginals.cloud',
      'discussions.unity.com','anime-planet.com','animekai.to','animetsu.to',
      'tiktok.com','blog.discoveruniversal.com'
    ],
    gaming: [
      'pubnotepad.com','telegram.org','novanon.net','pinpaste.com','reddit.com',
      'tiktok.com','memoryhackers.org','hey-gamer.com','joyfreak.com','hardforum.com'
    ],
  };

  // 🔹 Define links by type
  const linkTypes = {
    link1: [
{ url: 'https://gplinks.co/RrybixVq', sites: siteGroups.common },
{ url: 'https://gplinks.co/poPc7UDt', sites: siteGroups.common },
{ url: 'https://gplinks.co/B5ZRb', sites: siteGroups.common },
{ url: 'https://gplinks.co/BBzFo2Zj', sites: siteGroups.common },
{ url: 'https://gplinks.co/YrTaT', sites: siteGroups.common },
{ url: 'https://gplinks.co/WXiJT8V5', sites: siteGroups.common },
{ url: 'https://gplinks.co/Tm0V9Gh', sites: siteGroups.common },
{ url: 'https://gplinks.co/gGEhA2Rx', sites: siteGroups.common },
{ url: 'https://gplinks.co/mbhlzihK', sites: siteGroups.common },
{ url: 'https://gplinks.co/UBqgI3G', sites: siteGroups.common },
{ url: 'https://gplinks.co/VQZuFFpY', sites: siteGroups.common },
{ url: 'https://gplinks.co/fp7jnWT', sites: siteGroups.common },
    ],
    link2: [


{ url: 'https://shortxlinks.in/9rPEK', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/5iQXS', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/fOUX', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/SSUXU', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/i83Zv5S7', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/evnTk', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/zzOm', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/K0u1eM', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/NIjX', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/Q6LL8', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/DPLGfq', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/DL5R', sites: siteGroups.common },



    ],
    link3: [
        { url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/High-Probability-Trading', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/Crypto-vs-Forex-vs-Stocks-Choosing-Your-Battlefield', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/index?filter=strategies', sites: siteGroups.common },

{ url: 'https://hyperhustle.online/The-Triple-Threat-Strategy', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/Deploy-Applications', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/tools', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/which-exchange-has-the-best-liquidity-for-small-caps', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/which-exchange-has-the-best-liquidity-for-small-caps', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/?page=2', sites: siteGroups.common },


    ],
    link4: [
{ url: 'https://indiaearnx.com/rvad9V5', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/4JwV', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/4fZ', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/z8AB1', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/CIYG3D', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/GsDUC', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/UKh8', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/VDiSM', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/WkvBti', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/bu13X0Sz', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/yPbxqt', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/0dHmw', sites: siteGroups.common },
    ],
    link8: [
{ url: 'https://shrinkme.click/ueUBdyj', sites: siteGroups.common },
{ url: 'https://shrinkme.click/Qnsty', sites: siteGroups.common },
{ url: 'https://shrinkme.click/1b8kAl', sites: siteGroups.common },
{ url: 'https://shrinkme.click/9B3ARuT', sites: siteGroups.common },
{ url: 'https://shrinkme.click/2YlIIIz', sites: siteGroups.common },
{ url: 'https://shrinkme.click/sEY6', sites: siteGroups.common },
{ url: 'https://shrinkme.click/nQiz', sites: siteGroups.common },
{ url: 'https://shrinkme.click/rPiZ5v', sites: siteGroups.common },
{ url: 'https://shrinkme.click/0kxil', sites: siteGroups.common },
{ url: 'https://shrinkme.click/CkS9BwXk', sites: siteGroups.common },
    ],
    link5: [
{ url: 'https://tpi.li/PojXEQ9', sites: siteGroups.common },
{ url: 'https://tpi.li/PI1shh81mXr', sites: siteGroups.common },
{ url: 'https://tpi.li/AG6YBBUThlZ', sites: siteGroups.common },
{ url: 'https://tpi.li/gw9GJ1gdfp', sites: siteGroups.common },
{ url: 'https://tpi.li/uSYcuOZLb', sites: siteGroups.common },
{ url: 'https://tpi.li/GqW4eGR', sites: siteGroups.common },
{ url: 'https://tpi.li/u1e2W8fH', sites: siteGroups.common },
{ url: 'https://tpi.li/Wqoq', sites: siteGroups.common },
{ url: 'https://tpi.li/t7kzHVe4A4', sites: siteGroups.common },
{ url: 'https://tpi.li/5NAf', sites: siteGroups.common },
{ url: 'https://tpi.li/0W3Vypb', sites: siteGroups.common },
{ url: 'https://tpi.li/a8EiqdeDK', sites: siteGroups.common },
{ url: 'https://tpi.li/HRMkwGA', sites: siteGroups.common },
{ url: 'https://tpi.li/vAn', sites: siteGroups.common },
    ],

  };

  // 🔹 Get current site
  const currentHost = window.location.hostname.toLowerCase();

  // 🔹 Extract hash from URL (e.g., #link1)
  const hash = window.location.hash.replace('#', '').toLowerCase();

  if (hash && linkTypes[hash]) {
    // Filter links that are valid for currentHost
    const validLinks = linkTypes[hash].filter(entry => {
      return entry.sites.some(site => currentHost.includes(site));
    });

    if (validLinks.length > 0) {
      // Pick random link
      const randomIndex = Math.floor(Math.random() * validLinks.length);
      const chosen = validLinks[randomIndex];

      console.log("Valid links:", validLinks);
      console.log("Random index:", randomIndex);
      console.log("Chosen link:", chosen.url);
      // 🔹 If current host is pinpaste → direct redirect
      if (currentHost.includes('pinpaste.com')) {
        const a = document.createElement('a');
        a.href = chosen.url;
        a.rel = "noreferrer"; // hides referrer
        a.target = "_self";    // open in same tab
        document.body.appendChild(a);
        a.click();
        a.remove();

        return;
      }
      // Redirect via a simulated click
      const a = document.createElement('a');
      a.href = chosen.url;
      a.style.position = 'fixed';
      a.style.left = '-9999px';
      a.style.top = '-9999px';
      a.style.opacity = '0';
      a.target = '_self';
      document.body.appendChild(a);

      const clickEvent = new MouseEvent('click', { bubbles: true, cancelable: true, view: window });
      a.dispatchEvent(clickEvent);

      setTimeout(() => a.remove(), 1000);
    }
  }
})();



function checkAndDestroyBrokenPage() {
    const errorCodeEl = document.querySelector('.error-code');
    const mainMessage = document.querySelector('#main-message h1');

    const brokenMarkers = [
        'ERR_SSL_PROTOCOL_ERROR',
        'ERR_CONNECTION_REFUSED',
        'ERR_NAME_NOT_RESOLVED',
        'ERR_SSL_VERSION_OR_CIPHER_MISMATCH',
        'provide a secure connection',
        'invalid response'
    ];

    let isBroken = false;

    // 1. Check Error Code Element
    if (errorCodeEl && brokenMarkers.some(m => errorCodeEl.innerText.includes(m))) {
        isBroken = true;
    }

    // 2. Check Heading Message
    if (!isBroken && mainMessage && brokenMarkers.some(m => mainMessage.innerText.toLowerCase().includes(m.toLowerCase()))) {
        isBroken = true;
    }

    // 3. Execution
    if (isBroken) {
        console.log("Page is broken. Closing tab in 1 second...");
        
        setTimeout(() => {
            // Attempt standard close
            window.close();

            // Tampermonkey / Greasemonkey specific close
            if (typeof GM_closeWindow === "function") {
                GM_closeWindow();
            } else if (typeof window.GM_info !== "undefined") {
                // Some versions use this logic
                window.open('', '_self', ''); 
                window.close();
            }
        }, 1000);
        
        return true;
    }
    return false;
}

// Run it immediately
checkAndDestroyBrokenPage();



// --- STATE TRACKING ---
let lastMouseX = Math.floor(Math.random() * window.innerWidth);
let lastMouseY = Math.floor(Math.random() * window.innerHeight);
let lastUserActivity = Date.now();

window.addEventListener('mousemove', (e) => {
    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
    lastUserActivity = Date.now();
}, { passive: true });

window.addEventListener('mousedown', () => { lastUserActivity = Date.now(); });

// --- UTILITIES ---
function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

// --- CORE ACTIONS ---
async function naturalClick(element) {
    const idleTime = Date.now() - lastUserActivity;
    
    // Safety check: Don't hijack the mouse if the user is moving it
    if (idleTime < 1000) {
        setTimeout(() => naturalClick(element), 500);
        return;
    }

    const rect = element.getBoundingClientRect();
    const paddingX = rect.width * 0.2;
    const paddingY = rect.height * 0.2;
    
    const targetX = Math.floor(rect.left + paddingX + Math.random() * (rect.width - 2 * paddingX));
    const targetY = Math.floor(rect.top + paddingY + Math.random() * (rect.height - 2 * paddingY));
    if (!isTrueVisible2(element)) {
        console.log("click is not truly visible (honeypot/obstacle detected). Skipping click.");
        //console.log(el);
        //isLocked = false;
        return false;
    }
    chrome.runtime.sendMessage({
        action: "trustedClick",
        startX: lastMouseX,
        startY: lastMouseY,
        endX: targetX,
        endY: targetY
    });
    return true;
}
async function naturalClick2(element) {
    const idleTime = Date.now() - lastUserActivity;
    
    // Safety check: Don't hijack the mouse if the user is moving it
    if (idleTime < 1000) {
        setTimeout(() => naturalClick2(element), 500);
        return;
    }

    const rect = element.getBoundingClientRect();
    const paddingX = rect.width * 0.2;
    const paddingY = rect.height * 0.2;
    
    const targetX = Math.floor(rect.left + paddingX + Math.random() * (rect.width - 2 * paddingX));
    const targetY = Math.floor(rect.top + paddingY + Math.random() * (rect.height - 2 * paddingY));
    if (!isTrueVisible(element)) {
        console.log("click is not truly visible (honeypot/obstacle detected). Skipping click.");
        //console.log(el);
        //isLocked = false;
        return false;
    }
    chrome.runtime.sendMessage({
        action: "trustedClick",
        startX: lastMouseX,
        startY: lastMouseY,
        endX: targetX,
        endY: targetY
    });
    return true;
}
async function naturalScrollToElement(element) {
    let isCentered = false;
    let attempts = 0;

    while (!isCentered && attempts < 10) {
        const rect = element.getBoundingClientRect();
        const viewportHeight = window.innerHeight;
        const elementCenter = rect.top + rect.height / 2;
        const screenCenter = viewportHeight / 2;
        
        // Calculate how far we are from the center
        const diff = elementCenter - screenCenter;

        // If the button is within 100px of the center, we are good enough
        if (Math.abs(diff) < 100) {
            isCentered = true;
            break;
        }

        // Determine scroll chunk (don't scroll more than 300px at once)
        const scrollAmount = Math.sign(diff) * Math.min(Math.abs(diff), 300);

        chrome.runtime.sendMessage({
            action: "trustedScroll",
            x: lastMouseX,
            y: lastMouseY,
            distance: Math.floor(scrollAmount)
        });

        // Wait for the "momentum" of the scroll to finish before checking position again
        await delay(Math.random() * 600 + 200); 
        attempts++;
    }
}

function isTrueVisible(el) {
    if (!el) return false;

    const style = window.getComputedStyle(el);
    const rect = el.getBoundingClientRect();

    // 1. Basic Visibility Check (CSS)
    const isCSSVisible = (
        style.display !== 'none' && 
        style.visibility !== 'hidden' && 
        parseFloat(style.opacity) > 0.1 &&
        rect.width > 2 && 
        rect.height > 2
    );

    if (!isCSSVisible) {
        console.log("Element failed CSS visibility check:", el);
        return false;
    }

    // 2. Viewport Check (Is it even on screen?)
    const isWithinViewport = (
        rect.top < window.innerHeight &&
        rect.bottom > 0 &&
        rect.left < window.innerWidth &&
        rect.right > 0
    );

    if (!isWithinViewport) {
        console.log("Element is not within viewport:", el);
        return false;
    }

    // 3. THE "Honeypot & Obstacle" Check
    // We check the center of the element to see what's actually on top.
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Safety: elementFromPoint can return null if coordinates are off-screen
    const topEl = document.elementFromPoint(centerX, centerY);

    if (!topEl) {
        console.log("elementFromPoint returned null for coordinates:", centerX, centerY);

        return false;
    }
    // Check if the element at that point is our button OR a child of our button
    const isBlocked = !el.contains(topEl) && !topEl.contains(el);

    if (isBlocked) {
        // Optional: Log what is blocking it for debugging
        // console.log("Button is blocked by:", topEl);
        console.log("Button is blocked by another element. Possible honeypot or obstacle detected.", el, "Blocked by:", topEl);
        return false;
    }

    return true;
}


function isTrueVisible2(el) {
    if (!el) return false;

    const style = window.getComputedStyle(el);
    const rect = el.getBoundingClientRect();

    // 1. Basic Visibility Check (CSS)
    const isCSSVisible = (
        style.display !== 'none' && 
        style.visibility !== 'hidden' && 
        parseFloat(style.opacity) > 0.1 &&
        rect.width > 2 && 
        rect.height > 2
    );

    if (!isCSSVisible) {
        console.log("Element failed CSS visibility check:", el);
        return false;
    }

    // 2. Viewport Check (Is it even on screen?)
    const isWithinViewport = (
        rect.top < window.innerHeight &&
        rect.bottom > 0 &&
        rect.left < window.innerWidth &&
        rect.right > 0
    );

    if (!isWithinViewport) {
        console.log("Element is not within viewport:", el);
        return false;
    }



    return true;
}

// 1. ADD NEW SELECTORS FOR CONSENT BUTTONS

function handleConsentdsFirst() {
    // 1. Precise selectors for known CMPs
    const CONSENT_SELECTORS = [
        '.qc-cmp2-summary-buttons button[mode="primary"]', // Quantcast
        '.fc-agreement-dialog .fc-primary-button',         // Google Funding Choices
    ];

    // 2. Try specific selectors first
    for (const selector of CONSENT_SELECTORS) {
        const agreeBtn = document.querySelector(selector);
        if (agreeBtn && isTrueVisible2(agreeBtn)) {
            console.log("Known consent button found by selector:", selector);
            executeConsentClick(agreeBtn);
            return true;
        }
    }

    // 3. Fallback: Search ALL buttons for "AGREE" or "ACCEPT" text
    const allButtons = document.querySelectorAll('button, [role="button"]');
    for (const btn of allButtons) {
        if (isTrueVisible2(btn)) {
            const text = (btn.innerText || "").toUpperCase().trim();
            // Match "AGREE", "I AGREE", "ACCEPT", "ACCEPT ALL"
            if (text === "AGREE" || text === "ACCEPT" || text.includes("ACCEPT ALL")) {
                console.log("Consent button found by text matching:", text);
                executeConsentClick(btn);
                return true;
            }
        }
    }

    return false;
}

// Helper to ensure the click actually lands
function executeConsentClick(btn) {
    // Bring it to the absolute front
    btn.style.setProperty('z-index', '2147483647', 'important');
    btn.style.setProperty('position', 'relative', 'important');
    
    // Optional: Clear obstacles if naturalClick is being blocked
    // rescueAndPrepare(btn); 
    
    console.log("Clearing consent overlay...");
    naturalClick(btn);
}

async function clearStickies() {
    // We search for both IDs (#) and Classes (.) just in case
    const stickySelectors = [
        "#closeStickyBottom", 
        ".closeStickyBottom", 
        "#closeStickyTop", 
        ".closeStickyTop"
    ];
    
    for (const selector of stickySelectors) {
        const el = document.querySelector(selector);
        
        if (el) {
            //const style = window.getComputedStyle(el);
            //const rect = el.getBoundingClientRect();
            if (!isTrueVisible(el)) {
                //console.log("Sticky is not truly visible (honeypot/obstacle detected). Skipping click.", selector);
                //console.log(el);
                //isLocked = false;
                return;
            }

            console.log(`Sticky found: ${selector}. Clearing...`);
            
            // Human reaction time
            await new Promise(r => setTimeout(r, Math.floor(Math.random() * 400 + 400)));
            
            await naturalClick(el);
            
            // Wait for DOM to update
            await new Promise(r => setTimeout(r, 1000));
            //return true; 
            
        }
        //else {
        //    console.log(`No sticky found for selector: ${selector}`);
        //}
    }
    return false;
}


// --- MAIN LOOP --- #closeStickyBottom", "#closeStickyTop",
function indi2() {
    const clickSelectors = [  "#robotButton", "#robot", "#robot2", "#rtgli1", "#rtg-generate", "#robotContinueButton", "#open-continue-btn", "#rtg-snp2"];
    let isLocked = false;
    let clicked_btn = false;
    const blacklisted = new WeakSet(); 

    function isVisible(el) {

        if (!el || blacklisted.has(el)) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        // Check for honeypots: tiny size or hidden
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 2 && rect.height > 2);
    }
    setInterval(async () => {
        if (isLocked || (Date.now() - lastUserActivity < 2000)) return;
        clearStickies();
        //if (handledSticky) return;

        let foundButtons = [];
        clickSelectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(el => {
                if (isVisible(el)) foundButtons.push(el);
            });
        });

        if (foundButtons.length === 0) return;

        // Sort to find the most relevant button
        foundButtons.sort((a, b) => b.getBoundingClientRect().top - a.getBoundingClientRect().top);
        const btn = foundButtons[0];

        const rect = btn.getBoundingClientRect();

        // 1. If button is off-screen, use the trusted scroll
        // Inside your setInterval logic:
        if (rect.top < 0 || rect.bottom > window.innerHeight) {

        //if (rect.top < 100 || rect.bottom > (window.innerHeight - 100)) {
            isLocked = true;
            console.log("Button out of view. Starting precision scroll...ind", btn);
            
            //await naturalScrollToElement(btn);
            btn.scrollIntoView({ behavior: "smooth", block: "center" });
            
            // Short pause after scrolling to look "human"
            await delay(Math.random() * 1000 + 300);
            isLocked = false;
            //return; 
        }
        // 2. If button is visible, perform the human click
        isLocked = true;
        
        // Random "thinking" delay before moving to click
        await delay(Math.random() * 1000 + 300); 
        console.log("Button in view. Starting natural click...", btn);
        
        if (!isTrueVisible(btn)) {
            console.log("Button is not truly visible (honeypot/obstacle detected). Skipping click.");
            isLocked = false;
            return;
        }
        blacklisted.add(btn); 
        clicked_btn =  naturalClick(btn);
        if (!clicked_btn) {
            console.log("Click failed (possibly due to visibility issues). Blacklisting button for 2 seconds.", btn);
            await delay(2000); 
            clicked_btn =  naturalClick(btn);
            

        }
        setTimeout(() => blacklisted.delete(btn), 6000);
        
        // Lock for a few seconds to let page load/react
        setTimeout(() => { isLocked = false; }, 2000);
        
    }, 1000 + (Math.random() * 400)); // Randomized interval
}


function indi() {
    const clickSelectors = ["#robotButton", "#robot", "#robot2", "#rtgli1", "#rtg-generate", "#robotContinueButton", "#open-continue-btn", "#rtg-snp2"];
    const blacklisted = new WeakSet(); 
    let isLocked = false;

    function isVisible(el) {
        if (!el || blacklisted.has(el)) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && rect.width > 0);
    }

    async function naturalClick(element) {
        blacklisted.add(element); 
        const props = { view: window, bubbles: true, cancelable: true, buttons: 1 };
        element.dispatchEvent(new PointerEvent('pointerdown', props));
        element.dispatchEvent(new MouseEvent('mousedown', props));
        await new Promise(r => setTimeout(r, 100));
        element.dispatchEvent(new PointerEvent('pointerup', props));
        element.dispatchEvent(new MouseEvent('mouseup', props));
        element.dispatchEvent(new MouseEvent('click', props));
        setTimeout(() => blacklisted.delete(element), 15000);
    }

    setInterval(() => {
        if (isLocked) return;
        let foundButtons = [];

        clickSelectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(el => {
                if (isVisible(el)) foundButtons.push(el);
            });
        });

        if (foundButtons.length === 0) return;

        // Sort by bottom-most first
        foundButtons.sort((a, b) => b.getBoundingClientRect().top - a.getBoundingClientRect().top);

        const btn = foundButtons[0];
        const rect = btn.getBoundingClientRect();
        
        // Scroll if needed
        if (rect.top < 0 || rect.bottom > window.innerHeight) {
            btn.scrollIntoView({ behavior: "smooth", block: "center" });
            return; 
        }

        // Click logic
        isLocked = true;
        setTimeout(async () => {
            await naturalClick(btn);
            isLocked = false;
        }, 1000);
    }, 1500);
}



function gpscroll() {
    const scrollOnlySelectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"];
    const styleId = 'ui-helper-styles';
    if (!window.location.href.includes("powergam.online")) return;

    if (!document.getElementById(styleId)) {
        const style = document.createElement('style');
        style.id = styleId;
        style.innerHTML = `
            .btn-rescue-active { z-index: 2147483647 !important; position: relative !important; outline: 3px solid #00FF00 !important; }
            .obstacle-ghost { pointer-events: none !important; opacity: 0 !important; visibility: hidden !important; }
        `;
        document.head.appendChild(style);
    }

    const processedElements2 = new WeakSet();

    function rescueAndPrepare(btn) {
        
        if (!btn || processedElements2.has(btn)) return;
        const rect = btn.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;

        let topEl = document.elementFromPoint(x, y);
        let loopLimit = 0;
        while (topEl && topEl !== btn && !btn.contains(topEl) && topEl !== document.documentElement && loopLimit < 15) {
            topEl.classList.add('obstacle-ghost');
            topEl = document.elementFromPoint(x, y);
            loopLimit++; 
        }
        btn.classList.add('btn-rescue-active');
        processedElements2.add(btn);
        setTimeout(() => {
            processedElements2.delete(btn);
            btn.classList.remove('btn-rescue-active');
        }, 10000);
    }

    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0);
    }

    setInterval(() => {
        
        for (const selector of scrollOnlySelectors) {
            const btn = document.querySelector(selector);
            if (isVisible(btn)) {
                const btnText = (btn.innerText || "").toLowerCase();
                if (btnText.includes("wait") || btnText.includes("...")) continue;

                const rect = btn.getBoundingClientRect();
                if (rect.top < 0 || rect.bottom > window.innerHeight) {
                    console.log("gp-only button found but out of view. Scrolling into view...", btn);
                    btn.scrollIntoView({ behavior: "smooth", block: "center" });
                //    naturalScrollToElement(btn);
                    
                    // Short pause after scrolling to look "human"
                    delay(Math.random() * 300 + 300);
                }
                rescueAndPrepare(btn);
                naturalClick(btn);
                break; 
            }
        }
    }, 1500);
}




function shrtxlingo() {
    const scrollOnlySelectors = ["#wpsafelinkhuman", "#wpsafe-link", "#wpsafe-generate"];

    const processedElements3 = new WeakSet();
    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0);
    }

    setInterval(() => {
        for (const selector of scrollOnlySelectors) {
            const btn = document.querySelector(selector);
            if (isVisible(btn)) {
                
                const btnwait = document.querySelector('#wpsafe-wait2');
                if (isVisible(btnwait)) continue;

                //const rect = btn.getBoundingClientRect();
                //if (rect.top < 0 || rect.bottom > window.innerHeight) {
                    //console.log("shrtxlingo button found but out of view. Scrolling into view...", btn);
                    //btn.scrollIntoView({ behavior: "smooth", block: "center" });
                    //naturalScrollToElement(btn);
                    
                    // Short pause after scrolling to look "human"
                    //delay(Math.random() * 300 + 300);
                //}
                if (!btn || processedElements3.has(btn)) return;
                if (!isTrueVisible(btn)) return;

                //rescueAndPrepare(btn);
                naturalClick2(btn);
                processedElements3.add(btn);
                setTimeout(() => {
                    processedElements3.delete(btn);
                }, 10000);
                break; 
            }
        }
    }, 1500);
}

async function naturalClick55(element) {
    //blacklisted.add(element); 
    const props = { view: window, bubbles: true, cancelable: true, buttons: 1 };
    element.dispatchEvent(new PointerEvent('pointerdown', props));
    element.dispatchEvent(new MouseEvent('mousedown', props));
    await new Promise(r => setTimeout(r, 100));
    element.dispatchEvent(new PointerEvent('pointerup', props));
    element.dispatchEvent(new MouseEvent('mouseup', props));
    element.dispatchEvent(new MouseEvent('click', props));
    //setTimeout(() => blacklisted.delete(element), 15000);
}


// 1. MOVE THESE OUTSIDE so they don't reset every 1.5 seconds
const processedElements4 = new WeakSet();
let lastGetNavLinkClick = 0; 

function shinkern2() {
    const Countinue_btns = ["#startButton", "#message .wp2continuelink"];

    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0);
    }

    setInterval(() => {
        const pageTitle = document.title;
        const currentTime = Date.now();
        handleConsentdsFirst()

        // --- SECTION 1: Health Shield Logic ---
        if (pageTitle.includes("Health Shield")) {
            const getLinkBtn = document.querySelector('a.btn.btn-success.btn-lg.get-link');
            if (isVisible(getLinkBtn) && getLinkBtn.innerText.trim().toLowerCase() === "get link") {
                getLinkBtn.scrollIntoView({ behavior: "smooth", block: "center" });
                if (processedElements4.has(getLinkBtn)) {
                    console.log("Button #continue is ready but in 10s cooldown.");
                    return;
                }
                rescueAndPrepare(getLinkBtn);
                delay(700);
                naturalClick(getLinkBtn);
                processedElements4.add(getLinkBtn);
                setTimeout(() => {
                    processedElements4.delete(getLinkBtn);
                }, 10000);
                return;
                // We don't click here because your original code didn't have a click command here
            }
            const counti_btn = document.querySelector('button.btn.btn-primary.btn-captcha#continue');

            // 1. Check if the button exists and is visible
            if (isTrueVisible2(counti_btn)) {
                const btnText = counti_btn.innerText.trim().toLowerCase();
                // 2. Check text AND if the button is NOT disabled
                // If it has [disabled="disabled"], counti_btn.disabled will be true
                if (btnText === "continue" && !counti_btn.disabled) {
                    // 3. Check if we've already clicked this specific element in our 10s cooldown
                    if (processedElements4.has(counti_btn)) {
                        console.log("Button #continue is ready but in 10s cooldown.");
                        return;
                    }
                    console.log("Button #continue is active and clickable. Clicking now...");
                    // Mark as processed immediately to prevent spam
                    processedElements4.add(counti_btn);
                    // Perform the click
                    //naturalClick(counti_btn);
                    naturalClick55(counti_btn)

                    // Remove from processed set after 10 seconds
                    setTimeout(() => {
                        processedElements4.delete(counti_btn);
                    }, 5000);

                    return;
                } else if (counti_btn.disabled) {
                    console.log("Button #continue found, but it is currently DISABLED. Waiting...");
                }
            }

        }

        // --- SECTION 2: #getnewlink Logic (with 10s Cooldown) ---
        const btnwait = document.querySelector('#getnewlink');
        if (isVisible(btnwait)) {
            const currentUrl = window.location.href;
            //console.log(currentUrl); 
            if (currentUrl.includes("#getmylink") || currentUrl.includes("getmylink") || isTrueVisible2(btnwait)) {
                const btnwaitText = (btnwait.innerText || "").toLowerCase();
                
                if (btnwaitText.includes("get link")) {
                    // Now this comparison actually works because lastGetNavLinkClick is global
                    if (currentTime - lastGetNavLinkClick < 10000) {
                        console.log("GetNewLink is in 10s cooldown...");
                        return;
                    } else {
                        console.log(`Clicking #getnewlink...`);
                        btnwait.scrollIntoView({ behavior: "smooth", block: "center" });
                        lastGetNavLinkClick = currentTime; // Update the global timestamp
                        delay(Math.random() * 300 + 800)
                        setTimeout(() => {
                            naturalClick(btnwait);
                        }, 1000);
                        return;
                    
                    }
                    
                }
            }
        }

        // --- SECTION 3: Continue Buttons Logic ---
        for (const selector of Countinue_btns) {
            const btn = document.querySelector(selector);
            
            if (isVisible(btn)) {
                // If we already clicked this specific element in the last 10s, skip it
                if (processedElements4.has(btn)) continue;

                const btnText = (btn.innerText || "").toLowerCase();
                
                // Skip if it says "continue" (wait state)
                if (btnText.includes("continue")) {
                    // Ready to click
                    console.log(`Clicking ${selector}`);
                    btn.scrollIntoView({ behavior: "smooth", block: "center" });
                    delay(Math.random() * 300 + 800)
                    processedElements4.add(btn);
                    naturalClick(btn);

                    // Remove from "clicked" list after 10 seconds so it can be clicked again if needed
                    setTimeout(() => {
                        processedElements4.delete(btn);
                    }, 10000);
                    
                    
                }


            }
        }
    }, 1500);
}


function shinkern() {
    const Countinue_btns = ["#startButton", "#message .wp2continuelink"];
    async function rescueAndPrepare(btn) {
        if (!btn || processedElements2.has(btn)) return;

        // Force button to the very top immediately
        btn.style.setProperty('z-index', '2147483647', 'important');
        btn.style.setProperty('position', 'relative', 'important');
        btn.classList.add('btn-rescue-active');

        const rect = btn.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;

        // Clear any remaining obstacles that might be blocking 'naturalClick'
        let topEl = document.elementFromPoint(x, y);
        let loopLimit = 0;
        while (topEl && topEl !== btn && !btn.contains(topEl) && topEl !== document.documentElement && loopLimit < 15) {
            console.log("Removing obstacle covering button:", topEl);
            topEl.classList.add('obstacle-ghost');
            topEl = document.elementFromPoint(x, y);
            loopLimit++; 
        }

        processedElements2.add(btn);
        // Cleanup after 10s
        setTimeout(() => {
            processedElements2.delete(btn);
            btn.classList.remove('btn-rescue-active');
            btn.style.removeProperty('z-index');
        }, 10000);
    }
    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0);
    }

    // --- Redirect tracker (only active on fitnesstipz.com) ---
    const isFitnessTipz = window.location.hostname.includes("fitnesstipz.com");
    let lastButtonClickTime = isFitnessTipz ? Date.now() : null;

    if (isFitnessTipz) {
        setInterval(() => {
            if (Date.now() - lastButtonClickTime > 60000) {
                console.log("No buttons found/clicked in 60s on fitnesstipz.com. Redirecting...");
                window.location.href = "https://web.telegram.org/a/get#link5";
            }
        }, 5000); // Check every 5 seconds
    }

    function recordClick() {
        if (isFitnessTipz) lastButtonClickTime = Date.now();
    }

    setInterval(() => {
        const pageTitle = document.title;
        const currentTime = Date.now();
        handleConsentdsFirst();

        // --- SECTION 1: Health Shield Logic ---
        if (pageTitle.includes("Health Shield")) {
            const getLinkBtn = document.querySelector('a.btn.btn-success.btn-lg.get-link');
            if (isVisible(getLinkBtn) && getLinkBtn.innerText.trim().toLowerCase() === "get link") {
                getLinkBtn.scrollIntoView({ behavior: "smooth", block: "center" });
                if (processedElements4.has(getLinkBtn)) {
                    console.log("Button #continue is ready but in 10s cooldown.");
                    return;
                }
                rescueAndPrepare(getLinkBtn);
                delay(700);
                naturalClick(getLinkBtn);
                recordClick();
                processedElements4.add(getLinkBtn);
                setTimeout(() => {
                    processedElements4.delete(getLinkBtn);
                }, 5000);
                return;
            }

            const counti_btn = document.querySelector('button.btn.btn-primary.btn-captcha#continue');
            if (isTrueVisible2(counti_btn)) {
                const btnText = counti_btn.innerText.trim().toLowerCase();
                if (btnText === "continue" && !counti_btn.disabled) {
                    if (processedElements4.has(counti_btn)) {
                        console.log("Button #continue is ready but in 10s cooldown.");
                        return;
                    }
                    console.log("Button #continue is active and clickable. Clicking now...");
                    processedElements4.add(counti_btn);
                    naturalClick55(counti_btn);
                    recordClick();
                    setTimeout(() => {
                        processedElements4.delete(counti_btn);
                    }, 5000);
                    return;
                } else if (counti_btn.disabled) {
                    console.log("Button #continue found, but it is currently DISABLED. Waiting...");
                }
            }
        }

        // --- SECTION 2: #getnewlink Logic (with 10s Cooldown) ---
        const btnwait = document.querySelector('#getnewlink');
        if (isVisible(btnwait)) {
            const currentUrl = window.location.href;
            if (currentUrl.includes("#getmylink") || currentUrl.includes("getmylink") || isTrueVisible2(btnwait)) {
                const btnwaitText = (btnwait.innerText || "").toLowerCase();
                if (btnwaitText.includes("get link")) {
                    if (currentTime - lastGetNavLinkClick < 10000) {
                        console.log("GetNewLink is in 10s cooldown...");
                        return;
                    } else {
                        console.log(`Clicking #getnewlink...`);
                        btnwait.scrollIntoView({ behavior: "smooth", block: "center" });
                        lastGetNavLinkClick = currentTime;
                        delay(Math.random() * 300 + 800);
                        setTimeout(() => {
                            naturalClick(btnwait);
                            recordClick();
                        }, 1000);
                        return;
                    }
                }
            }
        }

        // --- SECTION 3: Continue Buttons Logic ---
        for (const selector of Countinue_btns) {
            const btn = document.querySelector(selector);
            if (isVisible(btn)) {
                if (processedElements4.has(btn)) continue;
                const btnText = (btn.innerText || "").toLowerCase();
                if (btnText.includes("continue")) {
                    console.log(`Clicking ${selector}`);
                    btn.scrollIntoView({ behavior: "smooth", block: "center" });
                    delay(Math.random() * 300 + 800);
                    processedElements4.add(btn);
                    naturalClick(btn);
                    recordClick();
                    setTimeout(() => {
                        processedElements4.delete(btn);
                    }, 10000);
                }
            }
        }
    }, 1500);
}

const processedElements5= new WeakSet();
const processedElementsgg= new WeakSet();

function shrkme() {
    const Countinue_btns = [".center-link-items #btn1", '#nextPage #btn2', ".center-link-items .tp-btn.tp-blue", ".center-link-items #btn2", "#tp-snp2" ];
    const isFitnessTipz2 = window.location.hostname.includes("shrinkme");
    let lastButtonClickTime2 = isFitnessTipz2 ? Date.now() : null;
    if (isFitnessTipz2) {
        setInterval(() => {
            if (Date.now() - lastButtonClickTime2 > 120000) {
                console.log("No buttons found/clicked in 60s on fitnesstipz.com. Redirecting...");
                window.location.href = "https://web.telegram.org/a/get#link8";
            }
        }, 5000); // Check every 5 seconds
    }
    function recordClick2() {
        if (isFitnessTipz2) lastButtonClickTime2 = Date.now();
    }
    // 1. Ensure the CSS is ready
    const styleId = 'priority-button-styles';
    if (!document.getElementById(styleId)) {
        const style = document.createElement('style');
        style.id = styleId;
        style.innerHTML = `
            /* Extreme z-index to stay above all overlays */
            .btn-rescue-active { 
                z-index: 2147483647 !important; 
                position: relative !important; 
                outline: 3px solid #00FF00 !important;
                pointer-events: auto !important;
                visibility: visible !important;
                opacity: 1 !important;
            }
            .obstacle-ghost { 
                pointer-events: none !important; 
                opacity: 0 !important; 
                visibility: hidden !important; 
            }
        `;
        document.head.appendChild(style);
    }

    const processedElements2 = new WeakSet();

    // 2. Updated Rescue function with Z-Index Force
    async function rescueAndPrepare(btn) {
        if (!btn || processedElements2.has(btn)) return;

        // Force button to the very top immediately
        btn.style.setProperty('z-index', '2147483647', 'important');
        btn.style.setProperty('position', 'relative', 'important');
        btn.classList.add('btn-rescue-active');

        const rect = btn.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;

        // Clear any remaining obstacles that might be blocking 'naturalClick'
        let topEl = document.elementFromPoint(x, y);
        let loopLimit = 0;
        while (topEl && topEl !== btn && !btn.contains(topEl) && topEl !== document.documentElement && loopLimit < 15) {
            console.log("Removing obstacle covering button:", topEl);
            topEl.classList.add('obstacle-ghost');
            topEl = document.elementFromPoint(x, y);
            loopLimit++; 
        }

        processedElements2.add(btn);
        // Cleanup after 10s
        setTimeout(() => {
            processedElements2.delete(btn);
            btn.classList.remove('btn-rescue-active');
            btn.style.removeProperty('z-index');
        }, 10000);
    }


    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0);
    }

    setInterval(() => {
        handleConsentdsFirst()
        const pageTitle = document.title;

        // --- SECTION 1: Health Shield Logic ---
        if (pageTitle.includes("PolicyBuzz") || pageTitle.includes("ShrinkMe.io")){
            //console.log("Detected PolicyBuzz/ShrinkMe page. Running specific logic...");
            
            const getLinkBtn = document.querySelector('.btn.btn-success.btn-lg.get-link');
            if (isVisible(getLinkBtn) && getLinkBtn.innerText.trim().toLowerCase() === "get link") {
                getLinkBtn.scrollIntoView({ behavior: "smooth", block: "center" });
                if (processedElements5.has(getLinkBtn)) {
                    console.log("Button #continue is ready but in 10s cooldown.");
                    return;
                }
                recordClick2();
                rescueAndPrepare(getLinkBtn);
                delay(700);
                naturalClick(getLinkBtn);
                processedElements5.add(getLinkBtn);
                setTimeout(() => {
                    processedElements5.delete(getLinkBtn);
                }, 10000);
                
                return;
                // We don't click here because your original code didn't have a click command here
            }
            const counti_btn = document.querySelector('button.btn.btn-primary');

            // 1. Check if the button exists and is visible
            if (isTrueVisible2(counti_btn)) {
                const btnText = counti_btn.innerText.trim().toLowerCase();
                // 2. Check text AND if the button is NOT disabled
                // If it has [disabled="disabled"], counti_btn.disabled will be true
                if (btnText === "click here to continue" && !counti_btn.disabled) {
                    // 3. Check if we've already clicked this specific element in our 10s cooldown
                    if (processedElements5.has(counti_btn)) {
                        console.log("Button #continue is ready but in 10s cooldown.");
                        return;
                    }
                    console.log("Button #continue is active and clickable. Clicking now...");
                    // Mark as processed immediately to prevent spam
                    processedElements5.add(counti_btn);
                    // Perform the click
                    recordClick2();
                    rescueAndPrepare(counti_btn);
                    delay(700);

                    //naturalClick(counti_btn);
                    //counti_btn.click();
                    naturalClick55(counti_btn)


                    // Remove from processed set after 10 seconds
                    setTimeout(() => {
                        processedElements5.delete(counti_btn);
                    }, 5000);

                    return;
                } else if (counti_btn.disabled) {
                    console.log("Button #continue found, but it is currently DISABLED. Waiting...");
                }
            }

        }



        // 1. Collect all valid, visible buttons first
        //const validButtons = [];

        //for (const selector of Countinue_btns) {

        // 1. Collect all valid, visible buttons first
        const validButtons = [];

        for (const selector of Countinue_btns) {
            const btn = document.querySelector(selector);
            if (isVisible(btn)) {
                const btnText = (btn.innerText || "").toLowerCase();
                
                // Skip buttons in a wait state
                if (btnText.includes("please") || btnText.includes("wait")) {
                    console.log("shrkme button found but in wait state. Skipping for now...", btn);
                    recordClick2();
                    return;
                }
                
                // Store button and its position
                validButtons.push({
                    element: btn,
                    top: btn.getBoundingClientRect().top
                });
            }
        }

        // 2. Sort buttons: Bottom to Top (highest 'top' value first)
        validButtons.sort((a, b) => b.top - a.top);

        // 3. Process the prioritized list
        for (const item of validButtons) {
            const btn = item.element;
            const rect = btn.getBoundingClientRect();

            // Scroll into view if necessary
            if (rect.top < 0 || rect.bottom > window.innerHeight) {
                console.log("Button found out of view. Scrolling...", btn);
                btn.scrollIntoView({ behavior: "smooth", block: "center" });
                
                // Human-like delay after scroll
                delay(Math.random() * 300 + 300);
            }

            console.log("Clicking prioritized button (Bottom -> Top strategy):", btn);
            rescueAndPrepare(btn);
            delay(1000);
            naturalClick(btn);
            processedElements5.add(btn);
            setTimeout(() => {
                processedElements5.delete(btn);
            }, 7000);
            // Break after the first successful prioritized click
            break; 
        }

    }, 1500);
}







/**
 * SCRIPT 2: THE EXECUTOR (indi)
 * Focused strictly on sorting and clicking "Active" buttons.
 */

// Start both
shrkme();
shinkern();
shrtxlingo();
gpscroll();
indi();
function setupDeadEndRedirect() {
    if (!window.location.href.includes("powergam.online")) return;

    let secondsMissing = 0;

    const checkStatus = () => {
        // SAFETY: If the browser is still spinning/loading, don't count yet
        if (document.readyState !== 'complete') return; 

        const timerDiv = document.querySelector("#myTimerDiv");
        const scrollSelectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"];
        
        const anyButtonVisible = scrollSelectors.some(selector => {
            const el = document.querySelector(selector);
            return el && el.offsetHeight > 0; // Check if it's actually drawn on screen
        });

        // If something is happening, reset the timer
        if (timerDiv || anyButtonVisible) {
            secondsMissing = 0; 
        } else {
            secondsMissing++;
        }

        if (secondsMissing >= 5) {
            window.location.href = "https://web.telegram.org/a/get#link1";
        }
    };

    setInterval(checkStatus, 1000);
}
setupDeadEndRedirect()
