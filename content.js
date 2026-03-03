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
    if (idleTime < 2000) {
        setTimeout(() => naturalClick(element), 1500);
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
        return;
    }
    chrome.runtime.sendMessage({
        action: "trustedClick",
        startX: lastMouseX,
        startY: lastMouseY,
        endX: targetX,
        endY: targetY
    });
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
                console.log("Sticky is not truly visible (honeypot/obstacle detected). Skipping click.", selector);
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
function indi() {
    const clickSelectors = [  "#robotButton", "#robot", "#robot2", "#rtgli1", "#rtg-generate", "#robotContinueButton", "#open-continue-btn", "#rtg-snp2"];
    let isLocked = false;

    function isVisible(el) {
        if (!el) return false;
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
            console.log("Button out of view. Starting precision scroll...");
            
            await naturalScrollToElement(btn);
            
            // Short pause after scrolling to look "human"
            await delay(Math.random() * 500 + 500);
            isLocked = false;
            return; 
        }
        // 2. If button is visible, perform the human click
        isLocked = true;
        
        // Random "thinking" delay before moving to click
        await delay(Math.random() * 1000 + 500); 
        console.log("Button in view. Starting natural click...", btn);
        
        if (!isTrueVisible(btn)) {
            console.log("Button is not truly visible (honeypot/obstacle detected). Skipping click.");
            isLocked = false;
            return;
        }
        await naturalClick(btn);
        
        // Lock for a few seconds to let page load/react
        setTimeout(() => { isLocked = false; }, 4000);
        
    }, 2000 + (Math.random() * 1000)); // Randomized interval
}



function shrinkearnscroll() {
    const mainSelectors = ["#getnewlink", "#startButton", ".wp2continuelink"];
    const styleId = 'shrinkearn-helper-styles';

    // 1. Setup CSS for highlighting and clearing obstacles
    if (!document.getElementById(styleId)) {
        const style = document.createElement('style');
        style.id = styleId;
        style.innerHTML = `
            .btn-rescue-active { z-index: 2147483647 !important; position: relative !important; outline: 3px solid #00FF00 !important; }
            .obstacle-ghost { pointer-events: none !important; opacity: 0 !important; visibility: hidden !important; }
        `;
        document.head.appendChild(style);
    }

    const processedElements = new WeakSet();
    function rescueAndPrepare(btn) {
        if (!btn || processedElements.has(btn)) return;

        // Safely boost the button without making it a "ghost"
        btn.style.setProperty('z-index', '2147483647', 'important');
        btn.style.setProperty('position', 'relative', 'important');
        btn.style.setProperty('pointer-events', 'auto', 'important'); // Forces clickability
        
        const rect = btn.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;

        // Only ghost elements that are NOT the button or its children
        let topEl = document.elementFromPoint(x, y);
        if (topEl && topEl !== btn && !btn.contains(topEl)) {
            topEl.style.pointerEvents = 'none';
            topEl.style.opacity = '0';
            console.log("Cleared obstacle from button");
        }

        processedElements.add(btn);
    }
    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        // Check if it exists in DOM and is not hidden via CSS
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.height > 0);
    }

    setInterval(() => {
        const pageTitle = document.title;
        let targetBtn = null;

        // 2. Logic for "Health Shield" page
        if (pageTitle.includes("Health Shield")) {
            const getLinkBtn = document.querySelector('a.btn.btn-success.btn-lg.get-link');
            
            // Check if button exists, is visible, and contains the text "Get Link"
            if (isVisible(getLinkBtn)) {
                const btnText = getLinkBtn.innerText.trim().toLowerCase();
                if (btnText === "get link") {
                    const rect = getLinkBtn.getBoundingClientRect();
                    // Scroll if button is not in the current viewport
                    if (rect.top < 0 || rect.bottom > window.innerHeight) {
                        getLinkBtn.scrollIntoView({ behavior: "smooth", block: "center" });
                    }
                }
            }
        }
        // 3. Logic for standard selectors if Health Shield specific button isn't found
        if (!targetBtn) {
            for (const selector of mainSelectors) {
                const btn = document.querySelector(selector);
                if (isVisible(btn)) {
                    targetBtn = btn;
                    break; // Priority found, stop searching
                }
            }
        }

        // 4. Execution: Scroll and Rescue
        if (targetBtn) {
            const rect = targetBtn.getBoundingClientRect();
            // Scroll if button is not in the current viewport
            if (rect.top < 0 || rect.bottom > window.innerHeight) {
                targetBtn.scrollIntoView({ behavior: "smooth", block: "center" });
            }
            rescueAndPrepare(targetBtn);
        }
    }, 1500);
}

// Start the function
shrinkearnscroll();



function gpscroll() {
    const scrollOnlySelectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"];
    const styleId = 'ui-helper-styles';

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
                //    btn.scrollIntoView({ behavior: "smooth", block: "center" });
                    naturalScrollToElement(btn);
                    
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

                const rect = btn.getBoundingClientRect();
                if (rect.top < 0 || rect.bottom > window.innerHeight) {
                //    btn.scrollIntoView({ behavior: "smooth", block: "center" });
                    naturalScrollToElement(btn);
                    
                    // Short pause after scrolling to look "human"
                    delay(Math.random() * 300 + 300);
                }
                if (!btn || processedElements3.has(btn)) return;
                //rescueAndPrepare(btn);
                naturalClick(btn);
                processedElements3.add(btn);
                setTimeout(() => {
                    processedElements3.delete(btn);
                    btn.classList.remove('btn-rescue-active');
                }, 10000);
                break; 
            }
        }
    }, 1500);
}



/**
 * SCRIPT 2: THE EXECUTOR (indi)
 * Focused strictly on sorting and clicking "Active" buttons.
 */

// Start both
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
