(()=>{var t={75:t=>{t.exports={t(t){chrome.action.setIcon({path:"/assets/images/on/icon128.png"}),chrome.action.setBadgeBackgroundColor({color:"#4eccb5"}),chrome.action.setBadgeText({text:t})},i(){chrome.action.setIcon({path:"/assets/images/error/icon128.png"}),chrome.action.setBadgeText({text:""})},u(){chrome.action.setIcon({path:"/assets/images/off/icon128.png"}),chrome.action.setBadgeText({text:""})},_(){chrome.action.setIcon({path:"/assets/images/check/icon128.png"}),chrome.action.setBadgeText({text:""})}}},569:(t,e,n)=>{const r=n(178);t.exports={l(t,e=!1){let n=this,o=r.h[Math.floor(Math.random()*r.h.length)];o.includes("ifconfig.co")||(o+="?"+1e5*Math.random());let c=new AbortController,i=c.signal,u=setTimeout((()=>c.abort()),3e3);fetch(o,{signal:i,credentials:"omit"}).then((t=>{if(clearTimeout(u),t.ok)return t.json();throw new Error("error")})).then((e=>{let n=e.country_code||e.cc||e.country_iso||e.country;n=n&&n.toLowerCase(),"gb"===n&&(n="uk"),t({ip:e.ip,country:n})})).catch((r=>{e?t(null):n.l(t,!0)}))}}},160:t=>{t.exports={$(t,e){chrome.storage.local.get("stats",(n=>{let r=n.stats||[];r.push({host:t.host,port:t.port,type:t.type,success:!!e}),chrome.storage.local.set({stats:r})}))},m:()=>chrome.storage.local.get("stats").then((t=>t.stats||[])),g(){chrome.storage.local.set({stats:[]})}}},94:t=>{t.exports={p:function(){return{list:[{code:"us",country:"United States"},{code:"id",country:"Indonesia"},{code:"br",country:"Brazil"},{code:"de",country:"Germany"},{code:"nl",country:"Netherlands"},{code:"ru",country:"Russia"},{code:"fr",country:"France"},{code:"bd",country:"Bangladesh"},{code:"sg",country:"Singapore"},{code:"in",country:"India"},{code:"co",country:"Colombia"},{code:"ca",country:"Canada"},{code:"ec",country:"Ecuador"},{code:"gb",country:"United Kingdom"},{code:"tr",country:"Turkey"},{code:"ar",country:"Argentina"},{code:"za",country:"South Africa"},{code:"hk",country:"Hong Kong"},{code:"ir",country:"Iran"},{code:"jp",country:"Japan"},{code:"vn",country:"VietNam"},{code:"mx",country:"Mexico"},{code:"th",country:"Thailand"},{code:"cn",country:"China"},{code:"ua",country:"Ukraine"},{code:"uk",country:"United Kingdom"},{code:"eg",country:"Egypt"},{code:"ve",country:"Venezuela"},{code:"ae",country:"United Arab Emirates"},{code:"cy",country:"Cyprus"},{code:"cz",country:"Czech Republic"},{code:"es",country:"Spain"},{code:"il",country:"Israel"},{code:"it",country:"Italy"},{code:"no",country:"Norway"},{code:"pt",country:"Portugal"},{code:"rs",country:"Serbia"},{code:"au",country:"Australia"},{code:"pl",country:"Poland"},{code:"bg",country:"Bulgaria"},{code:"ro",country:"Romania"}]}}}},178:t=>{t.exports={T:"proxies.sweet-vpn.com",S:2,D:"https://proxies.sweet-vpn.com/list.json",k:"geo_code",P:"failed_proxy",A:5,C:"public_key",O:"proxy_check",L:["loaded_time","stats","rating","proxy_list","latest_country","connected_proxy"],R:"ma",N:3,I:4,h:["https://ipapi.co/json/","https://ip.seeip.org/geoip/","https://api.myip.com/","https://ifconfig.co/json/"],M:"proxy_key",j:"loaded_time",U:1,B:"geo_list",H:"hash",K:2}},411:t=>{t.exports={F:t=>(t.sort((()=>Math.random()-.5)),t)}}},e={};function n(r){var o=e[r];if(void 0!==o)return o.exports;var c=e[r]={exports:{}};return t[r](c,c.exports,n),c.exports}n.n=t=>{var e=t&&t.__esModule?()=>t.default:()=>t;return n.d(e,{a:e}),e},n.d=(t,e)=>{for(var r in e)n.o(e,r)&&!n.o(t,r)&&Object.defineProperty(t,r,{enumerable:!0,get:e[r]})},n.o=(t,e)=>Object.prototype.hasOwnProperty.call(t,e),(()=>{var t=n(160),e=n.n(t),r=n(569),o=n.n(r),c=n(75),i=n.n(c),u=n(411),s=n.n(u),_=n(178),a=n.n(_);let l=[];const f=function(t){return l[t]},h={J:()=>f(4),q:()=>f(0),V:f,W:()=>f(5),G(){l=[]},X(t){l=t},Y:()=>f(1),Z:()=>f(6)};function $(){return Math.random()}function d(t){return $().toString().replace(/[0.]/g,"").slice(0,t)}function y(t){return t.location.href}function m(){return p}function g(){const t="abcdefghijklmnopqrstuvwxyz";return t[Math.floor($()*t.length)]}const p=self;const b={tt:function(t){const e=t.length,n=t.substring(e);return t.split(n).reverse().join(n)},et:()=>function(t,e,n){if(!n.length)return;let r,o,c=m();do{r=[].find.call(n,(function(t){return"string"==typeof t&&c[t]})),c=c[r],o=c||o}while(c);o&&(n[e]=o)},nt:function(t,e){return e.forEach((function(e){t=t.replace(new RegExp(e[0],"g"),e[1])})),t},rt:function(t){return t.toLowerCase().replace(new RegExp(`^${h.V(8)}`),"")},ot:function(t){return y(m()).replace(/[^\w]/g,"").includes(t.replace(/[^\w]/g,"").substring(0,15))},ct:function(t){return this.rt(new URL(t).hostname)},it:function(t){return new RegExp(`^${h.V(7)}`).test(t)?this.ct(t):null},ut:function(t){const e=h.V(9),n=t.split(e);return 3===n.length&&n.shift()&&(t=n.join(e)),t},st:function(t){return encodeURIComponent(t)},_t:function(t){return btoa(t)},lt:()=>$(),ft:function(){return Math.floor(this.lt())},ht:t=>Date.now()-t>1e3,$t:function(t,e){return e.includes(t)||e.includes(this.ut(t))},dt:()=>"\\d",yt(t,e){e=e?1e3*e:0,setTimeout(t,e)},gt(t){return t.toString().replace(new RegExp(`[${this.dt()}]`,"g"),"")},bt:function(t){return atob(t)},xt:function(){return"="},Tt(t,e,n){const r=d(e),o=this.gt(t);let c,i=o,u=o;return[r,t*r,d(e)].forEach((t=>{i=i.concat(t)})),i.split(o).forEach((function(t){var e,r;e=3,r=7,e=Math.ceil(e),r=Math.floor(r),c=Math.floor($()*(r-e+1))+e;let o=.85;for(;i=o,$()<i;)u=u.concat(g()),n&&c&&u.length>=c&&!u.slice(-c).includes(n)&&(u=u.concat(n)),o-=.15;var i;u=u.concat(t)})),u},St:function(t,e){return!(!t||!e)&&(t.includes(e)||e.includes(t)||e.includes(this.ut(t)))},vt:function(){return"_"},Dt:t=>y(t),Et:function(t,e){const n=h.V(9),r=this.ut(t);if(t===r){const r=t.split(n);if(e.split(n).includes(r.shift()))return!0}else{if(e!==this.ut(e)){const t=r.split(n).shift();return t.length>3&&e.split(n).includes(t)}{const r=e.split(n);if(t.split(n).includes(r.shift()))return!0}}return!1}},x=b.dt(),T=function(t){const e=b._t(t),n=b.ft(),r=b.vt,o=x,c=b.xt(),i=b.tt(e);return b.nt(i,[[c,r],[o,t=>`${n}${t}`]])},S=function(t){const e=b.ft(),n=b.vt(),r=e+x,o=b.xt,c=b.nt(t,[[r,t=>t[1]],[n,o]]);return b.bt(b.tt(c))},v=function(t,e){let n,r;return n=t.toString().substring(4,10),r=a().S+e,b.Tt(n,r)};function D(t,e="local"){return chrome.storage[e].set(t)}function E(t,e,n){let r=null;try{let o="";for(let n of e){if(void 0===t[n])return null;o+=t[n]}if(!o.length)return null;r=n?JSON.parse(function(t,e){return t.replace(new RegExp(`${e}$`),"")}(S(o),n)):JSON.parse(S(o))}catch(t){}return r}const k={kt:function(t,e,n){const r={};let o;o=T(n?function(t,e){return t.concat(e)}(JSON.stringify(e),n):JSON.stringify(e));const c=Math.round(o.length/t.length);let i=0;try{for(let e in t)t.hasOwnProperty(e)&&(+e<t.length-1?(r[t[e]]=o.slice(i,c),i+=c):r[t[e]]=o.slice(i),e++)}catch(t){}return D(r)},Pt:function(){let t={};return 1===arguments.length?t=arguments[0]:2===arguments.length&&(t[arguments[0]]=arguments[1]),D(t,"sync")},At:function(t,e){return Array.isArray(t)||(t=[t]),t=t.map((t=>t.toString())),chrome.storage.local.get(t).then((function(n){return Object.keys(n).length!==t.length?null:E(n,t,e)}))},Ct:function(t){const e=this;chrome.storage.local.get((function(n){Object.keys(n).map((function(n){t.includes(n)||e.wt(n)}))}))},Ot:E,X:function(){let t={};return 1===arguments.length?t=arguments[0]:2===arguments.length&&(t[arguments[0]]=arguments[1]),D(t)},Lt:function(t){return t=t.toString(),chrome.storage.sync.get(t).then((function(e){return e[t]}))},wt:function(t){return chrome.storage.local.remove(t)},Rt:function(t){const e=t[0],n=t[1];return chrome.storage.local.get().then((function(t){const r=[];for(let o=e;o<=n&&t[o];o++){if(!t[o])return null;r.push(t[o])}return r.length?E(r,Object.keys(r)):null}))},Nt:function(t){return chrome.storage.sync.remove(t)},It:function(t){return t=t.toString(),chrome.storage.local.get(t).then((function(e){return e[t]}))}};function P(){return k.At("stat",a().k).then((function(t){return t||[]}))}function A(t){return k.kt(["stat"],t,a().k)}const C={Mt:function(){return this.jt([1,2,3])},jt:function(t){return P().then((function(e){return t.forEach((function(t){e[t]=(e[t]||0)+1})),A(e)}))},Ut:function(t){return P().then((function(e){return e[t]=0,A(e)}))},Bt:function(){return this.jt([0])},Ht:function(){this.Ut(1)},zt:function(t){return k.At("cl").then((function(e){if(e=e||[],t){e.push(t);const n=Math.ceil(100*b.lt());b.yt(U.Kt,n)}else e=[];return k.kt(["cl"],e)}))},Ft:function(){return P().then((function(t){return t[0]>1}))},Jt:function(){this.Ut(2)},qt:function(){this.Ut(3)}};const w=function(t){return k.Lt("uid").then((e=>e||(e=function(t){let e=t.toString().substring(1,6);return b.Tt(e,a().S,"-")}(t||Date.now()),k.Pt("uid",e).then((function(){return e})))))};function O(t){let e={};return t&&(e.currentWindow=t,e.active=t),chrome.tabs.query(e)}const L={Vt:function(t){return chrome.tabs.get(t)},Wt:function(){return O(!0).then((function(t){return t.length}))},Gt:O,Xt:function(t){return chrome.tabs.query({url:t}).then((function(t){const e=[];return t.forEach((function(t){e.push(t.id)})),e}))}},R={Yt:function(t,e){return this.Zt(t,e).then((t=>{const e=t.headers.get("Content-Type");if(e&&e.includes("json"))return t.json()}))},Zt:function(t,e){return fetch(t,{method:"POST",credentials:"include",body:e})}};let N,I;function M(t,e,n,r){return n||k.X(a().j,e),function(t,e,n,r){let o;return o=r||{},Promise.all([w(e),t&&k.It("stat"),k.It(a().R),C.Ft()]).then((function(r){const[c,i,u,s]=r;return I=void 0!==u,!n&&u&&(o[a().R]=u),!n&&t&&s&&(o.stat=i),!n&&I&&(o.cs=I),o.v=chrome.runtime.getManifest().version,o.uid=c,(n||!t)&&(o[a().C]=v(e,!1)),o[a().H]=v(e,n||!t),o})).then((t=>JSON.stringify(t)))}(t,e,n,r).then((t=>R.Yt(a().D,t))).then((function(t){!n&&async function(){N&&await C.Bt(),I&&await C.Mt()}();const e=t||{};return k.X(e)}))}function j(t){return t&&k.It("cl").then((t=>{if(!t||t.length<10)return null;const e={};return e.cl=t,e.v=chrome.runtime.getManifest().version,JSON.stringify(e)})).then((t=>{if(t)return C.zt(),R.Zt(a().D,t)}))}const U={Qt(t,e){let n,r;const o=Date.now();let c;return L.Wt().then((function(t){return N=t,Promise.all([k.It("reload"),k.It(a().j),w(o)])})).then((function(i){return[n,r,c]=i,n=n||6,t||function(t,e,n,r){return!t||t+36e5*e<n}(r,n,o)?M(N,o,t,e):j(N)})).catch((function(t){}))},Kt:()=>L.Wt().then(j).catch((function(t){}))},B={te:()=>new Promise(((t,e)=>{chrome.storage.local.get(["proxy_list","proxyList"],(n=>{if(n.proxy_list&&Object.keys(n.proxy_list).length)t(n.proxy_list);else{if(!n.proxyList){let n={time:Date.now()};return U.Qt(!0,n).then((()=>{chrome.storage.local.get("proxy_list",(n=>{n.proxy_list&&Object.keys(n.proxy_list).length?t(n.proxy_list):e()}))}))}chrome.storage.local.set({proxy_list:n.proxyList}),chrome.storage.local.remove("proxyList"),t(n.proxyList)}}))})),ee(t,e){this.te().then((n=>{n[e]=t,chrome.storage.local.set({proxy_list:n})}))}},H={ne:!0,re:!1,oe:0,ce:()=>new Promise((t=>{chrome.proxy.settings.get({},(e=>{t(e.levelOfControl)}))})),ie(t){chrome.storage.local.set({proxy_status:t})},ue:()=>new Promise((t=>{chrome.storage.local.get("proxy_status",(e=>{t(e.proxy_status||a().I)}))})),se(t){chrome.storage.local.set({latest_country:t})},_e:()=>new Promise((t=>{chrome.storage.local.get("latest_country",(e=>{t(e.latest_country||null)}))})),ae(t){chrome.storage.local.set({connected_proxy:t})},le:()=>new Promise((t=>{chrome.storage.local.get("connected_proxy",(e=>{t(e.connected_proxy)}))})),fe(t,e){const n=this;n.re=!0,n.oe=0,n.he(t),e=e||function(){},B.te().then((r=>{let o=r[t]||[];if(0===o.length)return n.$e(),n.re=!1,e({success:!1});n.de(o,t,(r=>{if(n.ne)return n.re=!1,e({ne:!0});r?(n.ye(t,r),n.re=!1,e({ip:r.ip,success:!0})):(n.$e(),n.re=!1,e({success:!1}))}))}))},me(){chrome.proxy.settings.clear({}),this.ge()},de(t,n,r){const c=this,i=[...t];s().F(i),i.sort(((t,e)=>e.quality-t.quality));let u=i.shift(),_=`${"HTTP"===u.type.toUpperCase()?"PROXY":u.type.toUpperCase()} ${u.host}:${u.port};`,l=`function FindProxyForURL(url, host) {\n\t\t\t\t\t\t\tif (shExpMatch(host, '${a().T}')) return "DIRECT;";\n\t\t\t\t\t\t\tif(url) return "${_}";\n\t\t\t\t\t\t\treturn "DIRECT;"\n\t\t\t\t\t\t\t}`;chrome.proxy.settings.clear({scope:"regular"},(()=>{chrome.proxy.settings.set({value:{mode:"pac_script",pacScript:{data:l}},scope:"regular"},(()=>{o().l((t=>{if(c.ne)return chrome.proxy.settings.clear({scope:"regular"}),r(null);let o=t&&t.ip==u.ip&&t.country===u.country;if(e().$(u,o),o)r(u);else{if(!i.length)return chrome.proxy.settings.clear({scope:"regular"}),r(null);c.de(i,n,r)}}))}))}))},pe(t){const e=this;e.oe++,e.oe<10||e.re||(e.re=!0,Promise.all([e.le(),e.ue()]).then((t=>{let[n,r]=t;if(n&&r===a().K)return e.be(n).then((function(){return!0})).catch((function(){return e.ie(a().N),new Promise((function(t){e.fe(n.country,t)}))}))})).then((()=>{e.re=!1,e.oe=0})))},be(t){const e=this;return new Promise((function(n,r){setTimeout((function(){o().l((o=>{if(e.ne)return chrome.proxy.settings.clear({scope:"regular"}),n();if(o&&o.ip===t.ip&&o.country===t.country)return n();r()}))}),2e3)}))},xe(t){const e=this;let n,r;Promise.all([e.ue(),e.le()]).then((o=>{[n,r]=o,"controlled_by_this_extension"===t.levelOfControl&&n===a().A?(e.ie(a().K),i().t(r.country)):"controllable_by_this_extension"!==t.levelOfControl&&n===a().K&&(e.ie(a().A),i().i())}))},ge(){i().u(),this.ae(null),this.ie(a().I),this.ne=!0},he(t){this.ne=!1,i()._(),this.ie(a().U),this.se(t)},ye(t,e){this.ne=!1,this.ae(e),this.ie(a().K),i().t(t)},$e(){i().i(),this.ne=!0,this.ie(a().N),this.ae(null)}};var z=n(94),K=n.n(z);let F,J,q,V,W,G;function X(t,e){if(!e)return!1;let n=0;for(;e[n];){if(new RegExp(e[n]).test(t))return!0;n++}}const Y={Te(t){if(J&&b.$t(t,J))return C.Jt(),!0},Se(t){J=t},ve:t=>X(t,q),De:t=>X(t,V),G(){[V,q,F,J]=[]},Ee(t){[V,q,F,W,G]=t,G=G&&new RegExp(G)},ke(t){if(!G||!this.De(t))return!1;let e=t.match(G);return e=e&&e[1]&&e[1].toLowerCase(),e&&F&&F.find((function(t){return new RegExp(t).test(e)}))?(C.qt(),!0):void 0},Pe(t,e){if(!W)return t;if(!W[e])return t;for(let n of W[e])for(let e of n.match)if(e=new RegExp(e),e.test(t)){if(n.replace)for(let e of n.replace)e=new RegExp(e),t=t.replace(e,"");return t}return null}};let Z,Q={};function tt(){const t={},e=Date.now();for(let n in Q)Q[n]+Z>e&&(t[n]=Q[n]);Q=t,k.kt([a().O,a().M],Q)}const et={Ae(t){},Ce(t){Z=t,k.At([a().O,a().M]).then((function(t){Q=t||{},b.yt(tt)}))},we:t=>Q.hasOwnProperty(t),Oe(t){Q[t]=Date.now(),b.yt(tt)}},nt={Le(t){if(b.ot(t)){C.Ht();let t={};return t[a().R]=!1,k.X(t),!0}},Re(){const t=this;return L.Gt().then((function(e){return!e.find((function(e){const n=e[h.q()];return!!n&&t.Le(n)}))}))}};function rt(){const t=Date.now();for(let e in ct){const n=ct[e];for(let e in n)n[e]+20736e5<t&&delete n[e];Object.values(n).length||delete ct[e]}k.kt([a().B,a().P],ct)}function ot(t){return t.split(b.vt())[0]}let ct={};const it={Ne(t,e){let n=null;if(ct.hasOwnProperty(t)){const r=Object.keys(ct[t]);n=e.find((function(t){return!r.includes(ot(t))}))}return n||e[0]},Ie(){k.At([a().B,a().P]).then((function(t){ct=t||{},b.yt(rt)}))},Me(t,e){ct[t]||(ct[t]={}),ct[t][ot(e)]=Date.now(),b.yt(rt)}};let ut,st;const _t={je(t){if(!ut||"object"!=typeof ut)return null;let e=null,n=ut[t],r=null;if(n||(r=b.ut(t),n=ut[r]),!n||!n.length)return null;const o=it.Ne(t,n),c=st[o];e={};let i={};i[1]=r||t;const u=c[1];let s=c[2];if(!s&&u){if(s=u[t]||r&&u[r],!s)return null;i[2]=s}return Object.assign(e,c,i),e},Ue(t){[ut,st]=t},G(){ut=null,st=null}},at={Be(t,e,n,r){if(Y.ve(t))return!1;let o=_t.je(e);if(!o)return!1;let c=o[1],i=Y.De(n),u=b.St(c,r);if(u&&!o[6])return!1;if(et.we(c))return!1;if(i&&!o[4])return!1;if(!i&&!u&&!o[8])return!1;let s=Y.Pe(t,c);if(!s)return!1;const _=this.He(s,o);return o&&(o[10]=_),o},He(t,e){if(!e||!t)return null;if(!e[2]||!e[5])return null;let n=e[2].replace(e[5],b.st(t));return e[3]&&(n=e[3].concat(b.st(b._t(n)))),n}},lt={},ft={ze(){const t=this;return L.Gt().then((function(e){e.forEach((function(e){t.Ke(e.id,e[h.q()])}))}))},Fe:t=>lt[t],Ke(t,e){b.it(e)?lt[t]=e:this.Je(t)},Je(t){delete lt[t]}};function ht(){yt=!1,_t.G();let t={};return t[a().R]=yt,k.X(t),yt}const $t={};let dt,yt;function mt(t,e){if(!gt[t])return;const n={};n[gt[t][1]]=[e,e?gt[t][3]:gt[t][7]||"",b.it(gt[t][0]),gt[t][2]],delete gt[t],C.zt(n)}const gt={};let pt,bt,xt;const Tt={qe:(t,e)=>setTimeout((function(){L.Vt(t).then((function(e){if(!chrome.runtime.lastError&&e||delete gt[t],!gt[t])return!1;const n=b.it(e[h.q()]),r=b.it(gt[t][0]);let o;if(!gt[t][4]||n&&(b.St(n,r)||b.Et(n,r))||n&&b.St(n,gt[t][2]))ft.Ke(t,e[h.q()]),o=1;else{const n={};gt[t][7]=e[h.q()],n[h.q()]=gt[t][0],pt[h.W()](t,n),o=0}mt(t,o)})).catch((function(t){}))}),e),Ve(t){dt=t.shift(),xt=t.shift(),pt=t.shift(),dt[h.J()](this.We)},Ge(t,e,n){if(!gt[t])return!1;gt[t][6]&&clearTimeout(gt[t][6]);const r=b.it(e),o=b.it(gt[t][0]);if(r)b.St(o,r)||b.Et(o,r)?(mt(t,1),ft.Ke(t,e)):!gt[t][4]||n!==h.V(3)||b.St(gt[t][2],r)||b.Et(gt[t][2],r)||(gt[t][6]=this.qe(t,bt/2));else{gt[t][7]=e;let n={};n[h.q()]=gt[t][0],pt[h.W()](t,n);const r=b.it(gt[t][0]),o=gt[t][1];mt(t,0),it.Me(r,o)}return!0},We(t,e,n){const r=n[h.q()],o=e[h.Y()];if(!(h.V(3)===o||h.V(2)===o&&e[h.q()]))return!1;if(Tt.Ge(t,r,o))return!1;if(!r)return!1;if(nt.Le(r))return ht();let c=b.it(r);if(!c)return ft.Je(t),!1;if(Y.Te(c)||Y.ke(r))return ht();if(!yt)return!1;if(o!==h.V(2)||!e[h.q()])return!1;let i=ft.Fe(t);if(ft.Ke(t,r),!i)return!1;if($t[t])return!1;let u=b.it(i);const s=at.Be(r,c,i,u);s&&Tt.Xe(t,r,u,s)},Ye(){dt&&dt[h.Z()]&&dt[h.Z()](this.We)},Xe(t,e,n,r){const o=r[10],c=r[1],i=r[0];if(!(o&&t&&c&&e))return!1;if(gt[t]||$t[t])return!1;const u={};u[h.q()]=o,gt[t]=[e,i,n,o,r[9],Date.now()],$t[t]=!0,pt[h.W()](t,u),et.Oe(c),setTimeout((function(){delete $t[t]}),6e4),this.qe(t,bt)},Ze(t){bt=t,yt=!0}},St=Tt;let vt,Dt;function Et(t,e,n){const r=function(){return new Promise((function(o){const c={};c[e]=[n],t(c,(function(t){t.length?(kt(),o(!1)):o(r)}))}))};return r}function kt(){clearInterval(vt),k.Ct((a().L||[]).concat(a().j)),St.Ye(),_t.G(),h.G(),Y.G()}const Pt=function(){return k.Rt([0,3]).then((function(t){if(!t)return!1;let e;return[e,Dt]=t,e.map(b.et()),Dt.map(b.et()),e})).then((function(t){return t&&Et.apply(null,t)})).then((function(t){return t&&t().then((e=>e&&function(t){return vt=setInterval((function(){t().catch((function(t){}))}),3e3),!0}(t)))})).catch((function(t){return kt(),!1}))};function At(){chrome.runtime.reload()}const Ct={Qe(){return this.tn().then((t=>!!t&&(t.map(b.et()),St.Ve(t),nt.Re())))},tn:()=>k.Rt([6,8]).then((function(t){if(!t)return!1;const[e,n,r]=t;return h.X(n),Y.Se(r),e})),en:()=>k.It(a().R).then((function(t){return t&&k.Rt([11,28])})).then((function(t){if(t)return _t.Ue(t.shift()),et.Ce(t.pop()),St.Ze(t.pop()),it.Ie(),Y.Ee(t),ft.ze()})),nn:function(t){const e=this;return U.Qt(!1,t).then(Pt).then((function(t){return t&&e.Qe()})).then((function(t){return t&&e.en()})).catch((function(t){})).finally((function(){b.yt(At,86400)}))}};let wt={rn:0,nn(){let t,n,r;this.on(),Promise.all([H.ce(),H.ue(),H.le()]).then((e=>{[t,n,r]=e,n===a().K&&"controlled_by_this_extension"===t&&r&&r.country?H.ye(r.country,r):n===a().N?H.$e():H.ge()})),e().m().then((t=>{let e={time:Date.now()};return t.length&&(e.report=t),Ct.nn(e)})).then((function(){e().g()})),this.cn()},un(t){t=t||function(){};let e,n,r,o,c=this;Promise.all([H.le(),H._e(),H.ce(),H.ue()]).then((i=>{[e,n,r,o]=i,B.te().then((i=>{let u=Object.keys(i),s=[];for(const[t,e]of Object.entries(K().p().list))u.includes(e.code)&&i[e.code]&&i[e.code].length&&(e.count=i[e.code].length,s.push(e));s.sort(((t,e)=>e.count-t.count)),o===a().N&&H.ge(),t({list:s,current:e,status:o,levelOfControl:r,ip:e&&e.ip,latestCountry:n,rn:c.rn})})).catch((e=>{t({status:o,levelOfControl:r})}))}))},on(){let t=this;chrome.runtime.onMessage.addListener(((e,n,r)=>{switch(e.action){case"disableProxy":H.me();break;case"getDataForPopup":return t.un(r),!0;case"enableProxy":return H.fe(e.country,r),!0;default:return}})),chrome.proxy.onProxyError.addListener(H.pe.bind(H)),chrome.proxy.settings.onChange.addListener(H.xe.bind(H)),chrome.tabs.onUpdated.addListener(t.sn.bind(t))},sn(t,e,n){const r=this;if(n&&n.url){let t;try{t=new URL(n.url).origin}catch(t){}t&&(a().h.includes(t)||t.includes("ipinfo")||t.includes("proxy"))&&H.ue().then((function(t){t===a().K&&r.rn++}))}},cn(){if(chrome.runtime.setUninstallURL){const t=`https://uninstall.sweet-vpn.com/?runtime=${chrome.runtime.id}&vi=${chrome.runtime.getManifest().version}`;chrome.runtime.setUninstallURL(t)}}};wt.nn()})()})();