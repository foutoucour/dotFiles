var getSessionInfo = function(e) {
    var NEW_DOMAIN = 'https://tweetdeck.twitter.com';
    var session;
    var accountInfo;
    var uid;
    var data = {};

    if (e.origin === NEW_DOMAIN && e.data === 'getSession') {
        try {
            storage = localStorage;
        } catch (e) {
            storage = null;
        }

        if (storage) {
            session = localStorage.getItem('_session');
            accountInfo = localStorage.getItem('tweetdeckAccount') ||
                localStorage.getItem('tweetdeck_account');
            if (accountInfo) {
                if (accountInfo.charAt(0) === '{') {
                    // Old style account info
                    accountInfo = JSON.parse(accountInfo);
                    uid = accountInfo.email;
                } else {
                    uid = accountInfo;
                }
            }

            // Clear local storage
            storage.clear();
        }

        if (uid) {
            data = {
                session : session,
                uid : uid,
                sessionExists : true,
                staySignedIn : true
            }
        }

        e.source.postMessage(data, NEW_DOMAIN);
    }
};

window.addEventListener('message', getSessionInfo, false);