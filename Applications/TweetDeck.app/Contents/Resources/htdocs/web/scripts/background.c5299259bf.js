function handlePageChange(e){var t=chrome.extension.getURL("");e.url.substr(0,t.length)===t&&-1!==e.url.indexOf(TD.bg.MAIN_APP_PAGE_LOCATION)?theTab?e.id!=theTab.id&&(console.log("Duplicate TweetDeck page"),chrome.tabs.remove(e.id),TD.bg.utils.showTDTab()):(console.log("TweetDeck page created"),theTab=e):theTab&&e.id==theTab.id&&(console.log("User has navigated away"),handlePageDeath(e.id))}function handlePageDeath(e){theTab&&e==theTab.id&&(console.log("TweetDeck page closed"),theTab=null)}TD={bg:{},util:{}},TD.util.isChromeApp=function(){return!0},TD.bg.init=function(){TD.bg.contextMenu.init(),TD.bg.MAIN_APP_PAGE_LOCATION="web/templates/default.html"};var theTab=null;chrome.tabs.onCreated.addListener(function(e){handlePageChange(e)}),chrome.tabs.onUpdated.addListener(function(e,t,n){t.url&&handlePageChange(n)}),chrome.tabs.onRemoved.addListener(function(e){handlePageDeath(e)}),TD.buildID="LOCAL",TD.buildIDShort="LOCAL",TD.version="10.101.0",TD.config={debug_level:0,debug_checks:!0,debug_menu:!0,scribe_debug_level:1,api_root:"https://smfd-akc-08-sr1.devel.twitter.com:8443",td_create_key:"WYhuRGOFl3cf82xzL5qB",td_create_secret:"Ob4DxpijlICA+cb3h5Ca5My3CEYp/lgMg84nly+5k2A=",sync_name:"blackbird",client_name:"blackbird",internal_build:!0,custom_timelines:!0,force_dm_photos:!0,touchdeck:!0,twogin:!0,i18n_test:!1,i18n_test_length_ratio:.65,i18n_test_padding_char:"d"},function(e,t){"function"==typeof define&&define.amd?define([],t):e.TD.util.i18n=t()}(this,function(){var e,t={};return t.getMessage=function(e){if("undefined"==typeof TD_locale_messages)return void 0;var t=TD_locale_messages[e];return t&&t.message?t.message:void 0},t.getLocale=function(){return e?e:(TD.util.isChromeApp()&&(e=t.getMessage("@@ui_locale")),e)},t}),function(e,t){"function"==typeof define&&define.amd?define(["scripts/utils/i18n"],t):e.TD.i=t(TD.util.i18n)}(this,function(e){var t=/[^A-Za-z0-9_]/g,n={};return function(i,a,o){var c,r,l,u=TD.config.i18n_test_length_ratio||.2,s=TD.config.i18n_test_padding_char||"d";return"string"==typeof i&&(i={text:i}),"en_US"===e.getLocale()?r=i.text:(c=n[i.text],void 0===c&&(c=i.text.replace(t,""),n[i.text]=c),r=e.getMessage(c)||i.text),o||(r=TD.ui.template.toHtml(r,a)),TD.config.i18n_test&&(l=Math.round(r.length*u),r+=Array(l+1).join(s)),r}}),TD.bg.utils={},TD.bg.utils.getActiveTabWindow=function(){for(var e,t=chrome.extension.getViews(),n=0;n<t.length;n++)if(e=t[n],e.location.href==theTab.url)return e},TD.bg.utils.showTDTab=function(){if(theTab){var e=function(e){theTab=e,chrome.windows.get(e.windowId,t)},t=function(e){e.focused||chrome.windows.update(e.id,{focused:!0})};chrome.tabs.get(theTab.id,e),chrome.tabs.update(theTab.id,{selected:!0})}},TD.bg.utils.focusOrOpenTDTab=function(e){var t=function(){var t=TD.bg.utils.getActiveTabWindow(),n=function(){return t.TD&&t.TD.ready?(e(t),void 0):(setTimeout(n,500),void 0)};n()};theTab&&theTab.id?(TD.bg.utils.showTDTab(),t()):chrome.tabs.create({url:TD.bg.MAIN_APP_PAGE_LOCATION},function(){setTimeout(function(){t()},100)})},TD.bg.contextMenu=function(){var e={},t=chrome.contextMenus,n=(chrome.i18n.getMessage,function(e,t){var n;e.linkUrl?n=e.linkUrl:(t&&t.title&&(n=t.title,n.length>100&&(n=n.substr(0,100)+"…"),n+=" "),n+=e.pageUrl),TD.bg.utils.focusOrOpenTDTab(function(e){e.jQuery(e.document).trigger("uiComposeTweet",{text:n.trim()+" "})})});return e.init=function(){t.create({title:TD.i("Share page with TweetDeck",null,!0),onclick:n}),t.create({title:TD.i("Share link with TweetDeck",null,!0),onclick:n,contexts:["link"]})},e}(),TD.bg.init();